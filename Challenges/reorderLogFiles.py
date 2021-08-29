"""
Reorder Log files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key = lambda x: x.split()[0])  # when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[1:])  # sort by suffix
        result = letters + digits  # put digit logs after letter logs
        return result

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def func(x,y):
            if x[1].isdigit() or y[1].isdigit():
                return 1 if x[1].isdigit() else -1 # digits always come after letters
            for i in range(1, min(len(x), len(y))):
                if x[i] != y[i]:
                    return 1 if x[i] > y[i] else -1 # sort logs lexicographically by contents
            if len(x) != len(y):
                return len(x)-len(y) # if contents are the same but different length, return the longer one
            return 1 if x[0] > y[0] else -1 # if contents are the same, sort by key
            
        logs = [log.split(' ') for log in logs] # split by space
        logs = sorted(logs, key=cmp_to_key(func)) # sort using custom function
		return [' '.join(log) for log in logs]  # return original strings
