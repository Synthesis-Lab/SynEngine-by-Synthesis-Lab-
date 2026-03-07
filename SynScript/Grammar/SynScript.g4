// Copyright © 2026 Synthesis Lab
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// SynScript Grammar - ANTLR 4
// Oyun motoru için Python-like betiğine özgü çatı

grammar SynScript;

// ========== PROGRAM STRUCTURE ==========
program
    : (statement 
     | functionDecl 
     | varDecl 
     | stateDecl       // v0.2: State Machine block
     | signalDecl      // v0.2: Signal/Slot event
     | actorDecl)      // v0.2: Actor scope isolation
    * EOF
    ;

// ========== STATEMENTS ==========
statement
    : expressionStmt
    | block
    | ifStmt
    | whileStmt
    | forStmt
    | returnStmt
    | breakStmt
    | continueStmt
    | asyncStmt       // v0.2: Async/await support
    ;

expressionStmt: expression NEWLINE?;
asyncStmt: 'async' statement;  // v0.2: async fn _process(): ...
block: INDENT statement* DEDENT;

// ========== CONTROL FLOW ==========
ifStmt: 'if' expression ':' NEWLINE block ('elif' expression ':' NEWLINE block)* ('else' ':' NEWLINE block)?;
whileStmt: 'while' expression ':' NEWLINE block;
forStmt: 'for' ID 'in' expression ':' NEWLINE block;

returnStmt: 'return' expression? NEWLINE?;
breakStmt: 'break' NEWLINE?;
continueStmt: 'continue' NEWLINE?;

// ========== FUNCTION DECLARATION ==========
functionDecl: decorator* 'function' ID '(' paramList? ')' (':' type)? ':' NEWLINE block;
paramList: ID (':' type)? (',' ID (':' type)?)*;
decorator: '@' (ID | operatorDecorator);        // v0.2: @operator support

// v0.2 DECORATORS & OPERATORS ==========
operatorDecorator: 'vector' | 'math' | 'native' | 'color' | 'export' | 'on_ready' | 'process' | 'signal';

// ========== v0.2 STATE MACHINE BLOCKS ==========
stateDecl: 'state' ID ':' NEWLINE block;  // State sınıfı deklarasyonu
// State içinde on_enter(), tick(delta), on_exit() methodları var

// ========== v0.2 SIGNAL DECLARATIONS ==========
signalDecl: 'signal' ID '(' signalParamList? ')' NEWLINE?;
signalParamList: ID ':' type (',' ID ':' type)*;

// ========== v0.2 ACTOR SCOPE ISOLATION ==========
actorDecl: 'actor' ID ':' NEWLINE block;  // Actor sınıfı deklarasyonu (scope isolation)

// ========== VARIABLE DECLARATION ==========
varDecl: 'var' ID (':' type)? ('=' expression)? NEWLINE?;
type: 'int' 
    | 'float' 
    | 'string' 
    | 'bool' 
    | 'Vector2' 
    | 'Vector3' 
    | 'Color'
    | 'State'         // v0.2: State machine type
    | 'Signal'        // v0.2: Event signal type
    | 'Actor'         // v0.2: Game object type
    | 'Dict'          // Dictionary/map type
    | 'List'          // Array/list type
    | ID              // Custom types
    ;

// ========== EXPRESSIONS ==========
expression
    : signalBinding
    ;

// v0.2: Signal binding (source => target)
signalBinding
    : assignment ('=>' assignment)*
    ;

assignment
    : logicalOr (('=' | '+=' | '-=' | '*=' | '/=') assignment)?
    ;

logicalOr
    : logicalAnd ('or' logicalAnd)*
    ;

logicalAnd
    : equality ('and' equality)*
    ;

equality
    : comparison (('==' | '!=') comparison)*
    ;

comparison
    : addition (('<' | '<=' | '>' | '>=') addition)*
    ;

addition
    : multiplication (('+' | '-') multiplication)*
    ;

multiplication
    : unary (('*' | '/' | '%') unary)*
    ;

unary
    : ('not' | '-' | '+') unary
    | power
    ;

power
    : postfix ('**' unary)?
    ;

postfix
    : primary (postfixOp)*
    ;

postfixOp
    : '(' argList? ')'           # FunctionCall
    | '.' ID                      # MemberAccess
    | '[' expression ']'          # ArrayAccess
    ;

primary
    : NUMBER                          # NumberLiteral
    | STRING                          # StringLiteral
    | 'true'                          # BoolLiteral
    | 'false'                         # BoolLiteral
    | 'null'                          # NullLiteral
    | ID                              # Identifier
    | '(' expression ')'              # ParenthesizedExpr
    | ID '(' argList? ')'             # FunctionCallExpr
    | vectorLiteral                   # Vector
    | colorLiteral                    # Color
    | listLiteral                     # List
    | 'await' primary                 # v0.2: Await expression
    | 'emit_signal' '(' STRING (',' argList)? ')'  # v0.2: Emit signal
    | operatorAccess                  # v0.2: @operator.method
    ;

// v0.2: @operator namespace access (@vector.add, @math.sin, etc.)
operatorAccess
    : '@' ID '.' ID '(' argList? ')'
    ;

argList: expression (',' expression)*;
vectorLiteral: 'Vector2' '(' expression ',' expression ')' | 'Vector3' '(' expression ',' expression ',' expression ')';
colorLiteral: 'Color' '(' NUMBER ',' NUMBER ',' NUMBER (',' NUMBER)? ')';
listLiteral: '[' (expression (',' expression)*)? ']';

// ========== LITERALS ==========
NUMBER: [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;
STRING: '"' (~["\\\n\r] | '\\' .)* '"' | '\'' (~['\\\n\r] | '\\' .)* '\'';
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

// ========== WHITESPACE & CONTROL ==========
NEWLINE: '\n' | '\r\n';
INDENT: '    ' | '\t';  // 4 spaces or tab
DEDENT: '';

WS: [ \t\r]+ -> skip;
COMMENT: '#' ~[\n\r]* -> skip;
