/**
 * SynScript CLI Terminal Integration
 * Apache License 2.0 - Copyright © 2026 Synthesis Lab
 * 
 * Real-time syntax validation, transpiler preview, and StdLib reference
 */

const vscode = require('vscode');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

class SynCLI {
    constructor(context) {
        this.context = context;
        this.terminal = null;
        this.lastValidationTime = 0;
    }

    /**
     * Create or get the SynScript terminal
     */
    getTerminal() {
        if (!this.terminal || this.terminal.exitStatus !== undefined) {
            this.terminal = vscode.window.createTerminal('SynScript CLI');
        }
        return this.terminal;
    }

    /**
     * Validate SynScript syntax in real-time
     * @param {string} synCode - SynScript source code
     * @returns {Promise<Object>} Validation result {isValid, errors, warnings}
     */
    async validateSyntax(synCode) {
        return new Promise((resolve) => {
            const errors = [];
            const warnings = [];
            
            // State block validation
            const stateMatches = synCode.match(/state\s+([A-Za-z_][A-Za-z0-9_]*)\s*:/g);
            if (stateMatches) {
                stateMatches.forEach(match => {
                    const stateName = match.match(/state\s+([A-Za-z_][A-Za-z0-9_]*)/)[1];
                    
                    // Check for required methods
                    const stateBlock = synCode.substring(synCode.indexOf(match));
                    const hasOnEnter = /fn\s+on_enter\s*\(\)\s*:/.test(stateBlock);
                    const hasTick = /fn\s+tick\s*\(\s*delta\s*:\s*float\s*\)\s*:/.test(stateBlock);
                    
                    if (!hasOnEnter) {
                        warnings.push(`State '${stateName}' missing on_enter() method`);
                    }
                    if (!hasTick) {
                        warnings.push(`State '${stateName}' missing tick() method`);
                    }
                });
            }

            // Signal validation
            const signalMatches = synCode.match(/signal\s+([A-Za-z_][A-Za-z0-9_]*)\s*\([^)]*\)/g);
            if (signalMatches) {
                signalMatches.forEach(match => {
                    const signalName = match.match(/signal\s+([A-Za-z_][A-Za-z0-9_]*)/)[1];
                    
                    // Check if signal is emitted
                    const emitPattern = new RegExp(`emit_signal\\s*\\(\\s*["']${signalName}["']`);
                    if (!emitPattern.test(synCode)) {
                        warnings.push(`Signal '${signalName}' declared but never emitted`);
                    }
                });
            }

            // Syntax bracket validation
            let parenCount = 0, bracketCount = 0, braceCount = 0;
            for (let char of synCode) {
                if (char === '(') parenCount++;
                else if (char === ')') parenCount--;
                else if (char === '[') bracketCount++;
                else if (char === ']') bracketCount--;
                else if (char === '{') braceCount++;
                else if (char === '}') braceCount--;

                if (parenCount < 0 || bracketCount < 0 || braceCount < 0) {
                    errors.push('Unmatched closing bracket/parenthesis/brace');
                    break;
                }
            }

            if (parenCount > 0) errors.push('Unclosed parenthesis');
            if (bracketCount > 0) errors.push('Unclosed bracket');
            if (braceCount > 0) errors.push('Unclosed brace');

            resolve({
                isValid: errors.length === 0,
                errors,
                warnings,
                timestamp: new Date().toLocaleTimeString()
            });
        });
    }

    /**
     * Transpile SynScript to Python and show preview
     * @param {string} synCode - SynScript source code
     * @returns {Promise<string>} Python code
     */
    async transpilePreview(synCode) {
        return new Promise((resolve) => {
            const terminal = this.getTerminal();
            
            // Convert @operators to native calls
            let pythonCode = synCode;
            
            pythonCode = pythonCode.replace(/@vector\.add\s*\(/g, 'native_vector_add(');
            pythonCode = pythonCode.replace(/@math\.sin\s*\(/g, 'native_math_sin(');
            pythonCode = pythonCode.replace(/@math\.cos\s*\(/g, 'native_math_cos(');
            pythonCode = pythonCode.replace(/@math\.sqrt\s*\(/g, 'native_math_sqrt(');
            
            // Convert signal binding to connect
            pythonCode = pythonCode.replace(/(\w+)\s*=>\s*(\w+\.\w+)/g, '$1.connect($2)');
            
            // Convert state blocks
            pythonCode = pythonCode.replace(/state\s+([A-Za-z_][A-Za-z0-9_]*)\s*:/g, 'class $1(State):');
            
            // Convert fn to def
            pythonCode = pythonCode.replace(/fn\s+/g, 'def ');
            
            // Convert var to simple assignment
            pythonCode = pythonCode.replace(/var\s+/g, '');
            
            // Add StdLib imports at top
            const imports = [
                "# ===== SynScript StdLib (Transpiled) =====",
                "from synstate import State",
                "from synsignal import Signal",
                "from synactor import Actor",
                "from synmath import SynMath",
                "from synvector import Vector2, Vector3",
                "# ===== End StdLib =====",
                ""
            ].join('\n');
            
            pythonCode = imports + pythonCode;
            
            resolve(pythonCode);
        });
    }

    /**
     * Show StdLib method/class reference
     * @param {string} libraryName - E.g., "SynMath", "Vector2", "State"
     */
    showLibraryReference(libraryName) {
        const references = {
            'SynMath': `
SynMath Functions (v0.2):
├── sin(angle: float) -> float
├── cos(angle: float) -> float
├── tan(angle: float) -> float
├── sqrt(value: float) -> float
├── pow(base: float, exp: float) -> float
├── clamp(value: float, min: float, max: float) -> float
├── lerp(a: float, b: float, t: float) -> float
├── PI: 3.14159...
├── TAU: 6.28318...
└── E: 2.71828...
            `,
            'Vector2': `
Vector2 Methods (v0.2):
├── length() -> float
├── distance_to(other: Vector2) -> float
├── normalized() -> Vector2
├── dot(other: Vector2) -> float
├── lerp(other: Vector2, t: float) -> Vector2
├── x: float (property)
└── y: float (property)
            `,
            'State': `
State Class (v0.2):
├── on_enter() - Called when entering state
├── tick(delta: float) - Called every frame
├── on_exit() - Called when exiting state
├── is_active: bool (property)
└── parent: Actor (property)
            `,
            'Signal': `
Signal Class (v0.2):
├── connect(callback) - Bind callback to signal
├── disconnect(callback) - Unbind callback
├── emit(*args, **kwargs) - Trigger all callbacks
├── clear() - Remove all connections
└── connected_count: int (property)
            `,
            'Actor': `
Actor Class (v0.2):
├── add_state(name: str, state: State)
├── change_state(name: str) -> bool
├── add_signal(name: str, signal: Signal)
├── emit_signal(name: str, *args)
├── current_state: State (property)
├── state_count: int (property)
└── signal_count: int (property)
            `
        };

        const terminal = this.getTerminal();
        terminal.show();
        
        const reference = references[libraryName] || `Unknown library: ${libraryName}`;
        terminal.sendText(`echo "${reference}"`);
    }

    /**
     * Register VS Code commands
     */
    registerCommands() {
        this.context.subscriptions.push(
            vscode.commands.registerCommand('synscript.cli.validate', async () => {
                const editor = vscode.window.activeTextEditor;
                if (!editor || !editor.document.languageId.includes('syn')) {
                    vscode.window.showWarningMessage('Open a .syn file first!');
                    return;
                }

                const synCode = editor.document.getText();
                const result = await this.validateSyntax(synCode);
                
                const terminal = this.getTerminal();
                terminal.show();
                
                const output = [
                    `[SynScript CLI] Validation @ ${result.timestamp}`,
                    result.isValid ? '✅ Syntax Valid!' : '❌ Syntax Errors:',
                    ...result.errors.map(e => `  ERROR: ${e}`),
                    ...result.warnings.map(w => `  ⚠️  WARNING: ${w}`)
                ].join('\n');
                
                terminal.sendText(`echo "${output}"`);
            }),

            vscode.commands.registerCommand('synscript.cli.preview', async () => {
                const editor = vscode.window.activeTextEditor;
                if (!editor || !editor.document.languageId.includes('syn')) {
                    vscode.window.showWarningMessage('Open a .syn file first!');
                    return;
                }

                const synCode = editor.document.getText();
                const pythonCode = await this.transpilePreview(synCode);
                
                // Create output channel
                const outputChannel = vscode.window.createOutputChannel('SynScript Transpiler');
                outputChannel.clear();
                outputChannel.appendLine(`=== Transpiled Python (v0.2.0) ===`);
                outputChannel.appendLine(pythonCode);
                outputChannel.show();
            }),

            vscode.commands.registerCommand('synscript.cli.reference', async () => {
                const quickPick = vscode.window.createQuickPick();
                quickPick.items = [
                    { label: 'SynMath', description: 'Mathematical functions' },
                    { label: 'Vector2', description: '2D Vectors' },
                    { label: 'Vector3', description: '3D Vectors' },
                    { label: 'State', description: 'State Machine base class' },
                    { label: 'Signal', description: 'Event/Signal system' },
                    { label: 'Actor', description: 'Actor scope isolation' }
                ];
                quickPick.onDidChangeSelection(selection => {
                    if (selection[0]) {
                        this.showLibraryReference(selection[0].label);
                        quickPick.dispose();
                    }
                });
                quickPick.onDidHide(() => quickPick.dispose());
                quickPick.show();
            })
        );
    }

    /**
     * Activate the CLI integration
     */
    activate() {
        this.registerCommands();
        
        vscode.window.showInformationMessage('🎮 SynScript CLI v0.2.0 activated!');
    }
}

module.exports = SynCLI;
