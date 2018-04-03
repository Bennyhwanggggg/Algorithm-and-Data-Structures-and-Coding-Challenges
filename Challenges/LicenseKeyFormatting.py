# Regex version
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = S.replace("-","",len(S)).upper()[::-1]
        formatted = re.sub(r'(\w{' + str(K) + r'})', r'\1-', formatted)
        formatted = formatted[::-1]
        formatted = re.sub(r'^-',r'', formatted)
        return formatted


def licenseKeyFormatting(S, K):
    # Convert all to upper case first
    S = S.upper()

    temp = ""

    pos = 0
    for i in range(len(S)-1, -1, -1):
        if S[i] != "-":
            if pos and not pos%K:
                temp = "-"+temp
            temp = S[i]+temp
            pos += 1

    return temp

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '')[::-1]
        S = ''.join(map(lambda x: x.upper(), S))
        return '-'.join(reversed([S[i:i+K][::-1] for i in range(0, len(S), K)]))
S = "5F3Z-2e-9-w"
K = 4



print(licenseKeyFormatting(S, K))

S = "2-5g-3-J"
K = 2
print(licenseKeyFormatting(S, K))

S = "2Ac-5g-3-J"
K = 3
print(licenseKeyFormatting(S, K))