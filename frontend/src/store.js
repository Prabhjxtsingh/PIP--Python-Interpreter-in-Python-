import { create } from 'zustand'

export const useWorkspaceStore = create((set) => ({
  files: [
    { id: '1', name: 'main.py', content: 'print("Hello, PIP!")', isDirectory: false },
    { id: '2', name: 'utils.py', content: 'def add(a, b):\n    return a + b', isDirectory: false },
  ],
  activeFileId: '1',
  setActiveFile: (id) => set({ activeFileId: id }),
  updateFileContent: (id, content) => set((state) => ({
    files: state.files.map(f => f.id === id ? { ...f, content } : f)
  })),
}))
