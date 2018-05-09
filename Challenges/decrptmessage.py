"""
Let me know if you have any question!



Question is asking me to convert every letter to ASCII val, add 1 to first letter, add the ascii val of the previous from second
val and so on.. . Subtract 26 until it is a in range of a-z in ASCII then convert back
How abt the subtraction
Okey. Keep going

to convert from char to ASCII:
use ord(int), convert back use chr(char)

Cool!
But,
question doesn't ask you convert likes above.
question did that, then give you the result (encrypted message)
Your task is decrypt the result ~ convert back only

So the task is to convert a string of ASCII value to characters?
Hm... The input and output string are in the same format (ASCII characters)
Eg:
input = "dnotq"
you need to return output = "crime"

so since d's ascii is 100, to convert back, 100-1 then ord(99) = c
then chr(n) = 110, 110 +26+26+26+26 = 214 = ord(214-100) = r is this correct?

Yes!
The key of problem is just the way you implement it, I think.~

So I think the approach would be to start from the first character so you have the
val to add for remaining characters

and start a for loop from the beginning
and add the decrpyted character by doing the computation
then keep track of the number you have to add for the next character

any problem ?
do you need any help?
How do i find out the range of all lower case ASCII?
ord('z') - ord('a') + 1 = 26
When to stop adding 26, Ok i got it

will there be cases when the asicc of the word - prev is > ord(z)?

When you can deduct the previous value and still get a valid ASCII character
It is a naive way, but still good enough for this problem

Cool!
How about time complex ?
Time complexity is O(n) since we are just going through each character
How abt the While? Does it count? The while loop run time is constant as its not affected by input size

Oke. You did a good job. The solution is correct now.
However, I just suggest a shorter way to implement
ok!!
Space complexity is O(1)

That's all
"""


def decrypt(word):
    charmap = "hijklmnopqrstuvwxyzabcdefg"

    if not word:
        return word
    prev = ord(word[0])
    res = chr(prev - 1)
    start = ord('a')
    end = ord('z')
    for i in range(1, len(word)):
        v = ord(word[i])
        res += charmap[(v - prev) % 26]
        prev = v
        continue
        """    
        while (v - prev) > end or (v - prev) < start:   
          v += 26
        res += chr(v-prev)
        """
    return res


def decrypt(word):
    charmap = "hijklmnopqrstuvwxyzabcdefg"

    if not word:
        return word
    prev = ord(word[0])
    res = chr(prev - 1)
    start = ord('a')
    end = ord('z')
    for i in range(1, len(word)):
        v = ord(word[i])
        while (v - prev) > end or (v - prev) < start:
            v += 26
        res += chr(v - prev)
        prev = v
    return res


print(decrypt('dnotq'))


def decrypt(word):
    if not word:
        return ''

    #

    a = ord('a')
    ans = [ord(c) for c in word]

    for i in range(len(word) - 1, -1, -1):
        # -2 % 26 == 24
        if i > 0:
            ans[i] = chr((ans[i] - ans[i - 1] - a) % 26 + a)
        else:
            # i == 0
            ans[i] = chr((ans[i] - 1 - a) % 26 + a)

    return ''.join(ans)


print(decrypt('dnotq'))
