class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Logic: Sort and Linear Scan

        Time: O((n+max(folder))*logn)
        Space: O(n)
        """
        folder.sort(key=lambda x: len(x))
        parent_folders = []

        for f in folder:
            for i in range(len(f)):
                if f[i] == '/' and f[:i] in parent_folders:
                    break
            else:
                if f not in parent_folders:
                    parent_folders.append(f)
        
        return parent_folders
