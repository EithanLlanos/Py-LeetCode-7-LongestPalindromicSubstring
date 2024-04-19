# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

############################################################################################################################

class Solution(object):
    def longestPalindrome(self, s):
        ret = ""
        for i,e in enumerate(s):
            i1,i2 = i,i
            it,it2 = 1,2
            le = len(s)
            while i2+1 < le and s[i2+1] == e:
                i2 +=1
                p=e*it2
                ret = max(ret,(p),key = len)
                it2+=1 
            while True:
                if i1-it ==-1 or i2 + it >= le: break
                if s[i1-it]==s[i2+it]: ret = max(ret,s[i1 - it : i2 + it + 1],key = len) 
                else: break
                it += 1
        if not ret: return s[0]
        return ret
        #Runtime ≈ 1124 | > 41.94%
        #Memory ≈ 11.68 | > 91.84