import React from 'react';
import FileTree from '../workspace/FileTree';
import CodeEditor from '../workspace/CodeEditor';
import TerminalWindow from '../workspace/TerminalWindow';
import { Play } from 'lucide-react';

export default function WorkspaceLayout() {
  return (
    <div className="flex h-screen w-full flex-col bg-[#1e1e1e] text-white">
      {/* Top Navbar */}
      <div className="flex h-12 items-center justify-between border-b border-gray-700 bg-[#252526] px-4">
        <div className="font-bold">PIP IDE</div>
        <div className="flex items-center gap-4">
          <a href="/api/download-desktop/" className="text-sm font-medium text-blue-400 hover:text-blue-300">
            Download Desktop App
          </a>
          <button className="flex items-center gap-2 rounded bg-green-600 px-3 py-1 text-sm font-medium hover:bg-green-700">
            <Play size={16} /> Run
          </button>
        </div>
      </div>

      {/* Main Content Area */}
      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <div className="w-64 flex-none border-r border-gray-700 bg-[#252526] overflow-y-auto">
          <FileTree />
        </div>

        {/* Center Pane (Editor + Terminal) */}
        <div className="flex flex-1 flex-col overflow-hidden">
          {/* Editor */}
          <div className="flex-1 overflow-hidden">
            <CodeEditor />
          </div>

          {/* Terminal */}
          <div className="h-64 flex-none border-t border-gray-700 bg-[#1e1e1e]">
            <div className="flex h-8 items-center border-b border-gray-700 bg-[#252526] px-4 text-xs font-semibold text-gray-400">
              TERMINAL
            </div>
            <div className="h-[calc(100%-2rem)] p-2">
                <TerminalWindow />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
