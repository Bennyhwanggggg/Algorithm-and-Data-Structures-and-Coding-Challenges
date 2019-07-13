"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Approach:
Random Numbers
Generate a random integer to be used as the code. In case the generated code happens to be already mapped to some previous \text{longURL}longURL, we generate a new random integer to be used as the code. The data is again stored in a HashMap to help in the decoding process.

**Performance Analysis**
The number of URLs that can be encoded is limited by the range of \text{int}int.

The average length of the codes generated is independent of the \text{longURL}longURL's length, since a random integer is used.

The length of the URL isn't necessarily shorter than the incoming \text{longURL}longURL. It is only dependent on the relative order in which the URLs are encoded.

Since a random number is used for coding, again, as in the previous case, the number of collisions could increase with the increasing number of input strings, leading to performance degradation.

Determining the encoded URL isn't possible in this scheme, since we make use of random numbers.
"""
import random
import string

"""
This code is not very scalable, but it works well within the scope of this problem ;). It generates a random 6 character string and checks if it exists in dict values. But once the dict becomes extremely large our while loop in encode will become very slow. This may be improved by dynamically increasing the string length returned by generate_shortUrl as it detects the number of values in our dict.
"""
class Codec:
    
    def __init__(self):
        # dict to store all longUrl to shortUrl mappings
        self.long_to_short = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # Test if mapping already exists
        if longUrl in self.long_to_short.keys():
            return self.long_to_short[longUrl]
        
		# Generate random 6 character string for tinyUrl
        def generate_shortUrl():
            all_chars = string.ascii_letters + string.digits
            shortUrl = "".join(random.choice(all_chars) for x in range(6))
            return shortUrl
        
		# Keep generating new shortUrl till it finds one that doesn't exist in our dict
        shortUrl = generate_shortUrl()
        while shortUrl in self.long_to_short.values():
            shortUrl = generate_shortUrl()
        
		# map
        self.long_to_short[longUrl] = shortUrl
        
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # Simple mapping
        for k, v in self.long_to_short.items():
            if v == shortUrl:
                return k
        return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
