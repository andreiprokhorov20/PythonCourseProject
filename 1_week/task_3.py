"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        ans=['']
        digits_to_letters={'2':'abc', '3': 'def', '4':'ghi','5':'jkl','6':'mno', '7':'pqrs', '8': 'tuv', '9': 'wxyz'}
        for digit in digits:
            new_combs=[]
            for comb in ans:
                for letter in digits_to_letters[digit]:
                    new_combs.append(comb+letter)
            ans=new_combs
        return ans
