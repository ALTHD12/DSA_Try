"""Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1"""

#with brute forcing
class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = str(x)
        if x < 0:
            return False
        else:
            n = str(x)
            if org == n[::-1]:
                return True
            else:
                return False

#without converting to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        while x > rev:
            r = x % 10
            rev = rev * 10 + r
            x //= 10

        return x == rev or x == rev // 10
