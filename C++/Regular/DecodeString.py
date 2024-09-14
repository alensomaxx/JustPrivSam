''' Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

'''

def search(string):
    i = 0
    while i < len(string):
        if string[i] == "[":
            brak = i  
            num = i - 1  
            while num >= 0 and string[num].isdigit():
                num -= 1
            
            k = int(string[num + 1: brak])
            
            for j in range(i, len(string)):
                if string[j] == "]":
                    brEnd = j  
                    break
            
            encoded_str = string[brak + 1: brEnd]
            
            string = string[:num + 1] + k * encoded_str + string[brEnd + 1:]
            
            i = num + 1 + k * len(encoded_str) - 1  
        
        i += 1
    
    return string


print(search("3[a]2[bc]10[okk]"))  
