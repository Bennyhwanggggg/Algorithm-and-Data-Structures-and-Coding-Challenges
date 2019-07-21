"""
Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
"""

"""
Given [‘AB’, ‘CDE’, ‘F’, …, ‘YZ’]
Width: w

join the words with empty space
get the index of the end of a screen line w - 1
there are 3 cases:

Case 1:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to the space before F

Case 2:
“AB-CDE-F-…._YZ” (‘-’ denotes a space)
reach to exactly E

Case 3:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to D

case 1, I can count one more bit and go to next line
case 2, I can count two more bits and go to next line
case 3, I have to move the cursor back until it reach to some space, and go to next line

When I go through all the rows, how many bits did I counted? Let’s say L, then the answer should be L / length of the string
"""
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        start = 0
        for i in range(rows):
            start += cols - 1
            if s[start % len(s)] == ' ':
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start//len(s)
        
public class Solution {
    public int wordsTyping(String[] sentence, int rows, int cols) {
        int sum = 0, ans = 0, which = 0;
        for (String s : sentence) sum += s.length();
        for (int i = 0; i < rows; i++) {
            int remaining = cols + 1; // reserve an extra space for the dummy space to the left of the first letter
            while (which < sentence.length && sentence[which].length() + 1 <= remaining)
                remaining -= sentence[which++].length() + 1;
            if (which >= sentence.length) {
                which = 0;
                ans = ans + 1 + remaining / (sum + sentence.length);
                remaining %= sum + sentence.length;
                while (which < sentence.length && sentence[which].length() + 1 <= remaining)
                    remaining -= sentence[which++].length() + 1;
            }
        }
        return ans;
    }
}

"""
Optimized
"""
class Solution:
    def wordsTyping(self, words, rows, cols):
        sentence = " ".join(words) + ' '
        sentence_len = len(sentence)
        
        prev = -1
        backtrack = [0] * len(sentence)
        for i in range(sentence_len):
            if sentence[i] == ' ':
                prev = i
            backtrack[i] = i - (prev + 1)
        
        pos = 0
        for _ in range(rows):
            pos += cols
            pos -= backtrack[pos % sentence_len]
    
        return (pos + 1) // sentence_len

class Solution:
    def wordsTyping(self, words, rows, cols):
        sentence = " ".join(words) + ' '
        sentence_len = len(sentence)
        
        res = 0
        pos = 0
        for _ in range(rows):
            pos += cols
            while pos > 0 and sentence[pos % sentence_len] != ' ':
                pos -= 1
            if sentence[pos % sentence_len] == ' ':
                pos += 1
                
        return (pos + 1) // sentence_len
