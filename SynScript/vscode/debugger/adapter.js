#!/usr/bin/env node

/**
 * SynScript Debugger Adapter
 * Debug Adapter Protocol implementation for SynScript
 * Provides basic debugging capabilities for .syn files
 */

const { Server } = require('net');
const { DebugSession, BreakpointEvent, TerminatedEvent, StoppedEvent, OutputEvent, InitializedEvent } = require('vscode-debugadapter');
const path = require('path');
const fs = require('fs');

/**
 * SynScript Debug Adapter Session
 */
class SynScriptDebugSession extends DebugSession {
  
  constructor() {
    super();
    
    this.variableHandles = new Map();
    this.breakpoints = new Map();
    this.threads = new Map();
    this.threadId = 0;
    this.variableHandle = 0;
  }

  /**
   * Initialize request
   */
  initializeRequest(response, args) {
    response.body = {
      supportsConfigurationDoneRequest: true,
      supportsEvaluateForHovers: true,
      supportsSetVariable: true,
      supportsStepInTargetsRequest: false,
      supportsLogPoints: true,
      supportsConditionalBreakpoints: true
    };
    this.sendResponse(response);
    this.sendEvent(new InitializedEvent());
  }

  /**
   * Launch request
   */
  launchRequest(response, args) {
    const program = args.program;
    const console = args.console || 'integratedTerminal';
    
    if (!program || !fs.existsSync(program)) {
      this.sendErrorResponse(response, {
        id: 1001,
        format: `Program file not found: ${program}`,
        showUser: true
      });
      return;
    }

    this.sendResponse(response);
    
    // Simulate program start
    const thread = {
      id: this.threadId++,
      name: `SynScript Thread 0`,
      state: 'stopped'
    };
    
    this.threads.set(thread.id, thread);
    
    // Send stopped event at program entry
    this.sendEvent(new StoppedEvent('entry', thread.id));
    
    // Send output event with program info
    this.sendEvent(new OutputEvent(`SynScript Debug: Loaded ${path.basename(program)}\n`, 'console'));
  }

  /**
   * Threads request
   */
  threadsRequest(response) {
    const threads = Array.from(this.threads.values()).map(t => ({
      id: t.id,
      name: t.name
    }));
    
    response.body = { threads };
    this.sendResponse(response);
  }

  /**
   * Stack trace request
   */
  stackTraceRequest(response, args) {
    const threadId = args.threadId;
    
    response.body = {
      stackFrames: [
        {
          id: 0,
          name: 'main',
          source: {
            path: args.context || ''
          },
          line: 1,
          column: 0
        }
      ],
      totalFrames: 1
    };
    
    this.sendResponse(response);
  }

  /**
   * Scopes request
   */
  scopesRequest(response, args) {
    const frameId = args.frameId;
    
    const scopes = [
      {
        name: 'Local',
        variablesReference: frameId * 1000 + 1,
        expensive: false
      },
      {
        name: 'Global',
        variablesReference: frameId * 1000 + 2,
        expensive: false
      }
    ];
    
    response.body = { scopes };
    this.sendResponse(response);
  }

  /**
   * Variables request
   */
  variablesRequest(response, args) {
    const ref = args.variablesReference;
    const variables = [];
    
    // Placeholder variables
    variables.push({
      name: 'example_var',
      value: '0',
      variablesReference: 0,
      type: 'integer'
    });
    
    response.body = { variables };
    this.sendResponse(response);
  }

  /**
   * Continue request
   */
  continueRequest(response, args) {
    const threadId = args.threadId;
    const thread = this.threads.get(threadId);
    
    if (thread) {
      thread.state = 'running';
    }
    
    response.body = { allThreadsContinued: false };
    this.sendResponse(response);
  }

  /**
   * Next request
   */
  nextRequest(response, args) {
    this.continueRequest(response, args);
  }

  /**
   * Step in request
   */
  stepInRequest(response, args) {
    this.continueRequest(response, args);
  }

  /**
   * Step out request
   */
  stepOutRequest(response, args) {
    this.continueRequest(response, args);
  }

  /**
   * Evaluate request
   */
  evaluateRequest(response, args) {
    response.body = {
      result: `${args.expression} = 0`,
      variablesReference: 0,
      type: 'integer'
    };
    this.sendResponse(response);
  }

  /**
   * Set breakpoint request
   */
  setBreakPointsRequest(response, args) {
    const source = args.source.path;
    const breakpoints = args.breakpoints || [];
    
    const verified = breakpoints.map(bp => ({
      verified: true,
      line: bp.line,
      column: bp.column || 0,
      source: args.source
    }));
    
    response.body = { breakpoints: verified };
    this.sendResponse(response);
  }

  /**
   * Pause request
   */
  pauseRequest(response, args) {
    const threadId = args.threadId;
    const thread = this.threads.get(threadId);
    
    if (thread) {
      thread.state = 'stopped';
      this.sendEvent(new StoppedEvent('pause', threadId));
    }
    
    this.sendResponse(response);
  }

  /**
   * Evaluate expression at hover
   */
  evaluateForHovers(response, args) {
    this.evaluateRequest(response, args);
  }
}

// Start debug session over stdin/stdout
DebugSession.run(SynScriptDebugSession);
