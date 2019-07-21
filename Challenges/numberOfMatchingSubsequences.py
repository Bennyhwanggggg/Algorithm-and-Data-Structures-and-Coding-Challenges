"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""

"""
Next Letter Pointers

Intuition

Since the length of S is large, let's think about ways to iterate through S only once, instead of many times as in the brute force solution.

We can put words into buckets by starting character. If for example we have words = ['dog', 'cat', 'cop'], then we can group them 'c' : ('cat', 'cop'), 'd' : ('dog',). This groups words by what letter they are currently waiting for. Then, while iterating through letters of S, we will move our words through different buckets.

For example, if we have a string like S = 'dcaog':

heads = 'c' : ('cat', 'cop'), 'd' : ('dog',) at beginning;
heads = 'c' : ('cat', 'cop'), 'o' : ('og',) after S[0] = 'd';
heads = 'a' : ('at',), 'o' : ('og', 'op') after S[0] = 'c';
heads = 'o' : ('og', 'op'), 't': ('t',) after S[0] = 'a';
heads = 'g' : ('g',), 'p': ('p',), 't': ('t',) after S[0] = 'o';
heads = 'p': ('p',), 't': ('t',) after S[0] = 'g';

Time: O(S.length + sum(words[i].length))
Space: O(words.length)
"""
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        res = 0
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None]) # only the Nones are the ones where words has become empty

"""
 begin by creating a default dictionary of 'list' objects. The main benefit of a default dictionary is that when you access an entry that does not yet exist, the entry is created automatically (in this case, the value for the entry is an empty list when it is created). I then create a 'count' variable to keep track of the number of words that are subsequences of the given string.

The first thing I do with the dictionary is populate it with all the words in the list of words. The key for each entry is the first letter of the word. The value is the list of words that start with that letter. Using the example in the problem, the dictionary would look like the following:

{'a': ['a', 'acd', 'ace'], 'b': ['bb']}

The next step is to iterate through each character in the given string. For each character, I access the dictionary to retrieve the list of words that start with that character. I reset the value of the entry to an empty list and then iterate through the list of words I retrieved. If the word is only a single letter, then I conclude that we have successfully found a completed subsequence and increase our 'count' by one. Otherwise, I slice off the first character and add the sliced word back to the dictionary. This time, it is added to the entry for which the key is equal to the first letter of the sliced word.

This process continues until we have iterated through all characters in the string. At the end, I return the count.
"""
from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count



"""
The idea is to use the String S and build a dictionary of indexes for each character in the string.
Then for each word, we can go character by character and see if it is a subsequence, by using the corresponding index dictionary, but just making sure that the index of the current character occurs after the index where the previous character was seen. To speed up the processing, we should use binary search in the index dictionary.

As an example for S = "aacbacbde"
the
dict_idxs =
{a: [0, 1, 4]
b: [3, 6]
c: [2, 5]
d: [7]
e: [8]
}
Now for the word say "abcb", starting with d_i = 0,
a => get list for a in the dict_idxs which is [0, 1, 4], and in the list, find the index of a >= d_i which is 0. After this update d_i to +1 => 1
b => get list for b in the dict_idxs [3, 6], and in the list, find the index of b >= d_i => >= 1, which is at index 0 => 3, after this update d_i to 4+1 => 4
c => in the list for c, [3, 5], find the index of c >= 4, which is 5. update d_i to 5+1 = 6
b => in the list for b, [3, 6], fund the index of b >= 6, which is 6, update d_i to 7, since this is the end of the word, and we have found all characters in the word in the index dictionary, we return True for this word.
"""
class Solution:
	def numMatchingSubseq(self, S, words):
        	def isMatch(word, w_i, d_i):
            		if w_i == len(word): 
				return True
            		l = dict_idxs[word[w_i]]
            		if len(l) == 0 or d_i > l[-1]:
				return False
            		i = l[bisect_left(l, d_i)]
            		return isMatch(word, w_i + 1, i + 1)

        	dict_idxs = defaultdict(list)
        	for i in range(len(S)):
            		dict_idxs[S[i]].append(i)
        	return sum(isMatch(word, 0, 0) for word in words)


"""
Brute force
"""
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        
        for word in words:
            i = 0
            j = 0
            while j < len(word) and i < len(S):
                if S[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                count += 1
        
        return count
        

