import React, { useEffect, useRef } from 'react';
import { Terminal } from '@xterm/xterm';
import { FitAddon } from '@xterm/addon-fit';
import '@xterm/xterm/css/xterm.css';

export default function TerminalWindow() {
  const terminalRef = useRef(null);
  
  useEffect(() => {
    if (!terminalRef.current) return;
    
    const term = new Terminal({
      theme: {
        background: '#1e1e1e',
      },
      fontFamily: 'monospace',
      cursorBlink: true,
    });
    
    const fitAddon = new FitAddon();
    term.loadAddon(fitAddon);
    
    term.open(terminalRef.current);
    fitAddon.fit();
    
    term.writeln('Welcome to PIP Terminal');
    term.writeln('Connecting to sandbox...');
    
    // Resize terminal on window resize
    const handleResize = () => {
      fitAddon.fit();
    };
    window.addEventListener('resize', handleResize);
    
    // Mock echo for now
    term.onData(data => {
        // Just echo for now until websocket is wired
        if (data === '\r') {
            term.write('\r\n$ ');
        } else if (data === '\u007f') { // backspace
            term.write('\b \b');
        } else {
            term.write(data);
        }
    });

    term.write('\r\n$ ');
    
    return () => {
      window.removeEventListener('resize', handleResize);
      term.dispose();
    };
  }, []);

  return <div ref={terminalRef} className="h-full w-full" />;
}
