class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = 0
        index = 0
        while index < len(chars):
            curr = chars[index]
            count = 0
            while index < len(chars) and chars[index] == curr:
                index += 1
                count += 1

            chars[result] = curr
            result += 1
            if count != 1:
                for c in str(count):
                    chars[result] = c
                    result += 1
        return result


