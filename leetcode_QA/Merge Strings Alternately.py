"""
title: Merge Strings Alternately

You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.

If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r

Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b 
    word2:    p   q   r   s
    merged: a p b q   r   s

Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q 
    merged: a p b q c   d
"""




class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1:
            return word2
        elif not word2:
            return word1
        

        result = ""
        len_1 = len(word1)
        len_2 = len(word2)

        n = min(len_1, len_2)

        for i in range(n):
            result += word1[i] + word2[i]
        
        if n == len_1:
            result += word2[i+1:]
        elif n == len_2:
            result += word1[i+1:]

        return result


solution = Solution()

word1 = "abc"
word2 = "pqr"
result = solution.mergeAlternately(word1, word2)
print(result)

word1 = "ab"
word2 = 'pqrs'
result = solution.mergeAlternately(word1, word2)
print(result)

word1 = "abcd"
word2 = "pq"
result = solution.mergeAlternately(word1, word2)
print(result)