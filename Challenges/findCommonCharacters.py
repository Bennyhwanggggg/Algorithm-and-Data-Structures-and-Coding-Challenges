class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        letters = set()
        for word in A:
            for letter in word:
                letters.add(letter)
        repeats = []
        for l in letters:
            occurance = min([word.count(l) for word in A])
            repeats.extend([l]*occurance)
        return repeats
