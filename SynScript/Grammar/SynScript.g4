// SynScript Grammar - ANTLR 4
// Oyun motoru için Python-like betiğine özgü çatı

grammar SynScript;

// ========== PROGRAM STRUCTURE ==========
program: (statement | functionDecl | varDecl)* EOF;

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
    ;

expressionStmt: expression NEWLINE?;
block: INDENT statement* DEDENT;

// ========== CONTROL FLOW ==========
ifStmt: 'if' expression ':' NEWLINE block ('elif' expression ':' NEWLINE block)* ('else' ':' NEWLINE block)?;
whileStmt: 'while' expression ':' NEWLINE block;
forStmt: 'for' ID 'in' expression ':' NEWLINE block;

returnStmt: 'return' expression? NEWLINE?;
breakStmt: 'break' NEWLINE?;
continueStmt: 'continue' NEWLINE?;

// ========== FUNCTION DECLARATION ==========
functionDecl: decorator* 'function' ID '(' paramList? ')' ':' NEWLINE block;
paramList: ID (',' ID)*;
decorator: '@' ID;

// ========== VARIABLE DECLARATION ==========
varDecl: 'var' ID (':' type)? ('=' expression)? NEWLINE?;
type: 'int' | 'float' | 'string' | 'bool' | 'Vector2' | 'Vector3' | 'Color';

// ========== EXPRESSIONS ==========
expression
    : assignment
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
    : NUMBER                      # NumberLiteral
    | STRING                      # StringLiteral
    | 'true'                      # BoolLiteral
    | 'false'                     # BoolLiteral
    | ID                          # Identifier
    | '(' expression ')'          # ParenthesizedExpr
    | ID '(' argList? ')'         # FunctionCallExpr
    | vectorLiteral               # Vector
    | colorLiteral                # Color
    | listLiteral                 # List
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
