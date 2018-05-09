class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [word]
        res = []
        abbreviations = self.generateAbbreviations(word[1:])
        for a in abbreviations:
            res.append(word[0] + a)
            if a and a[0].isdigit():
                leadingInt = re.search(r'\d+', a).group()
                res.append(str(1 + int(leadingInt)) + a[len(leadingInt):])
            else:
                res.append('1' + a)
        return res
