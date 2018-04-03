class TrieNode(object):
    def __init__(self, value):
        self.nxt = [None] * 26
        self.value = value
        return


class PrefixTrieTable(object):
    def __init__(self, words):
        self.root = TrieNode(None)
        for w in words:
            self.add_to_trie(w)
        return

    def add_to_trie(self, w):
        root = self.root
        for ch in w:
            offset = ord(ch) - ord('a')
            if root.nxt[offset] != None:
                root = root.nxt[offset]
            else:
                root.nxt[offset] = TrieNode(None)
                root = root.nxt[offset]
        root.value = w
        return

    def collect(self, root, candidates):
        if root.value:
            candidates.append(root.value)
        else:
            for i in range(26):
                if root.nxt[i]:
                    self.collect(root.nxt[i], candidates)
        return

    def get_prefix_matches(self, prefix):
        candidates, root = [], self.root
        for ch in prefix:
            offset = ord(ch) - ord('a')
            root = root.nxt[offset]
            if root == None:
                return candidates
        self.collect(root, candidates)
        return candidates


class Solution(object):
    def helper(self, so_far, N, words, results, table):
        if len(so_far) == N:
            results.append([x for x in so_far])
        else:
            prefix = "".join([x[len(so_far)] for x in so_far])
            for c in table.get_prefix_matches(prefix):
                so_far.append(c)
                self.helper(so_far, N, words, results, table)
                so_far.pop()
        return

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        results = []
        if words:
            table = PrefixTrieTable(words)
            self.helper([], len(words[0]), words, results, table)
        return results