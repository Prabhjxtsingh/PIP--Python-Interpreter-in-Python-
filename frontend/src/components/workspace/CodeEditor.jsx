import React from 'react';
import Editor from '@monaco-editor/react';
import { useWorkspaceStore } from '../../store';

export default function CodeEditor() {
  const { files, activeFileId, updateFileContent } = useWorkspaceStore();
  
  const activeFile = files.find(f => f.id === activeFileId);

  if (!activeFile) {
    return <div className="flex h-full items-center justify-center text-gray-500">Select a file to edit</div>;
  }

  const handleEditorChange = (value) => {
    updateFileContent(activeFileId, value);
  };

  return (
    <Editor
      height="100%"
      language="python"
      theme="vs-dark"
      value={activeFile.content}
      path={activeFile.name}
      onChange={handleEditorChange}
      options={{
        minimap: { enabled: false },
        fontSize: 14,
        wordWrap: 'on',
        padding: { top: 16 }
      }}
    />
  );
}
