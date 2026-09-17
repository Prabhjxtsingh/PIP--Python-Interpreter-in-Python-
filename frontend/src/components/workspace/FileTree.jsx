import React from 'react';
import { useWorkspaceStore } from '../../store';
import { File, Folder } from 'lucide-react';

export default function FileTree() {
  const { files, activeFileId, setActiveFile } = useWorkspaceStore();

  return (
    <div className="p-2 text-sm">
      <div className="mb-2 font-semibold text-gray-400">EXPLORER</div>
      <div className="space-y-1">
        {files.map(file => (
          <div 
            key={file.id}
            onClick={() => setActiveFile(file.id)}
            className={\lex cursor-pointer items-center gap-2 rounded px-2 py-1 hover:bg-[#37373d] \\}
          >
            {file.isDirectory ? <Folder size={16} className="text-blue-400"/> : <File size={16} className="text-gray-400"/>}
            {file.name}
          </div>
        ))}
      </div>
    </div>
  );
}
