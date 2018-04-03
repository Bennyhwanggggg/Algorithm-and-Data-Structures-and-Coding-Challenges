class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        status = [False] * len(s)
        final = ""
        for word in dict:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    status[i] = True
                start = s.find(word, start + 1)

        i = 0
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final

