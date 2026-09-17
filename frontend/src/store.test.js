import { describe, it, expect, beforeEach } from 'vitest'
import { useWorkspaceStore } from './store'

describe('Zustand Store', () => {
  beforeEach(() => {
    useWorkspaceStore.setState({ activeFileId: null })
  })

  it('should set the active file correctly', () => {
    const { setActiveFile } = useWorkspaceStore.getState()
    
    setActiveFile('main.py')
    expect(useWorkspaceStore.getState().activeFileId).toBe('main.py')
  })
})
