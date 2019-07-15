"""
Sentence Similarity II

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""

"""
DFS
Two words are similar if they are the same, or there is a path connecting them from edges represented by pairs.

We can check whether this path exists by performing a depth-first search from a word and seeing if we reach the other word. The search is performed on the underlying graph specified by the edges in pairs.

Time: O(NP) where NN is the maximum length of words1 and words2, and PP is the length of pairs. Each of NN searches could search the entire graph.

Space: O(P) the size of pairs
"""
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        similarity = collections.defaultdict(list)
        
        for pair in pairs:
            a, b = pair
            similarity[a].append(b)
            similarity[b].append(a)
         
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and (w1 not in similarity or w2 not in similarity):
                return False
            stack = [w1]
            seen = {w1}
            similar = False
            while stack:
                word = stack.pop()
                if word == w2:
                    similar = True
                    break
                if word not in similarity:
                    return False
                for sim in similarity[word]:
                    if sim not in seen:
                        seen.add(sim)
                        stack.append(sim)
            if not similar:
                return False
        return True

