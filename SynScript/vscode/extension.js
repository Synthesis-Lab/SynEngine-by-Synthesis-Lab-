const vscode = require('vscode');
const { DebugAdapterExecutable } = require('vscode');
const path = require('path');
const fs = require('fs');

let extensionContext;

/**
 * Activation function - called when the extension is activated
 */
function activate(context) {
  extensionContext = context;
  
  console.log('SynScript Language Support v0.3.2 activated');

  // Command: Start Debugging
  let debugCommand = vscode.commands.registerCommand('synscript.debug.start', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage('Please open a SynScript file first');
      return;
    }

    if (!editor.document.fileName.endsWith('.syn')) {
      vscode.window.showErrorMessage('Current file is not a SynScript file (.syn)');
      return;
    }

    // Start debugging the current file
    await vscode.debug.startDebugging(
      vscode.workspace.getWorkspaceFolder(editor.document.uri),
      {
        name: 'SynScript: Debug Current File',
        type: 'synscript',
        request: 'launch',
        program: editor.document.fileName,
        args: [],
        console: 'integratedTerminal'
      }
    );
  });

  // Command: Run File
  let runCommand = vscode.commands.registerCommand('synscript.run.file', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage('Please open a SynScript file first');
      return;
    }

    if (!editor.document.fileName.endsWith('.syn')) {
      vscode.window.showErrorMessage('Current file is not a SynScript file (.syn)');
      return;
    }

    // Show launch configuration options
    const option = await vscode.window.showQuickPick(
      ['Run with Debugger', 'Run without Debugger'],
      { placeHolder: 'Select run mode' }
    );

    if (!option) return;

    if (option === 'Run with Debugger') {
      await vscode.debug.startDebugging(
        vscode.workspace.getWorkspaceFolder(editor.document.uri),
        {
          name: 'SynScript: Run with Debugger',
          type: 'synscript',
          request: 'launch',
          program: editor.document.fileName,
          args: [],
          console: 'integratedTerminal'
        }
      );
    } else {
      // Run without debugger (would need SynScript runtime)
      vscode.window.showInformationMessage(
        'Running without debugger. Make sure you have SynScript runtime installed.'
      );
    }
  });

  // Command: Stop Debugging
  let stopCommand = vscode.commands.registerCommand('synscript.debug.stop', async () => {
    await vscode.debug.stopDebugging();
  });

  // Debug adapter factory
  const factory = new SynScriptDebugAdapterFactory();
  context.subscriptions.push(
    vscode.debug.registerDebugAdapterDescriptorFactory('synscript', factory)
  );

  // Register commands
  context.subscriptions.push(debugCommand);
  context.subscriptions.push(runCommand);
  context.subscriptions.push(stopCommand);

  // Show quick info message
  vscode.window.showInformationMessage('SynScript v0.3.2 ready! Use F5 to start debugging or click Run button');
}

/**
 * Debug Adapter Factory
 */
class SynScriptDebugAdapterFactory {
  createDebugAdapterDescriptor(session, executable) {
    const adapterPath = path.join(
      extensionContext.extensionPath,
      'debugger',
      'adapter.js'
    );

    return new DebugAdapterExecutable('node', [adapterPath]);
  }
}

/**
 * Deactivation function
 */
function deactivate() {
  console.log('SynScript Language Support deactivated');
}

module.exports = {
  activate,
  deactivate
};
