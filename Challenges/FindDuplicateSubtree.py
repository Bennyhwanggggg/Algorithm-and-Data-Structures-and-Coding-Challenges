class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.d = {}
        self.ans = []
        self.count = 0

        def rec(self, root):
            if not root:
                return None
            t = (root.val, rec(self, root.left), rec(self, root.right))
            if t in self.d:
                if self.d[t][1] == 0:
                    self.ans.append(root)
                self.d[t][1] += 1
                return self.d[t][0]
            else:
                self.d[t] = [self.count, 0]
                self.count += 1
                return self.d[t][0]

        rec(self, root)
        return self.ans


class Solution2:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        st = []
        self.postorder(root, {}, st)
        return st

    def postorder(self, root, m, st):
        if root is None:
            return ''
        order = self.postorder(root.left, m, st) + ',' + self.postorder(root.right, m, st) + ',' + str(root.val)
        if order not in m:
            m[order] = 1
        elif m[order] == 1:
            st.append(root)
            m[order] += 1
        return order


