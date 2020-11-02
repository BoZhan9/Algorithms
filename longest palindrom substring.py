# Longest Palindromic Substring
# Brute force | Time: O(n^3)
def longestPalindrome(self, s):
    if s is None:
        return None
        
    for length in range(len(s), 0, -1):
        for i in range(len(s) - length + 1):
            if self.is_palindrome(s, i, i + length -1):
                return s[i: i + length]
    
    return ""
        
def is_palindrome(self, s, left, right):
    while left < right and s[left] == s[right]:
        left += 1
        right -= 1
    
    return left >= right

# Center point enumeration｜Time: O(n^2) Space: O(n^2)
def longestPalindrome(self, s):
    if s is None:
        return None

    answer = (0, 0) #(length, start)
    for mid in range(len(s)):
        answer = max(answer, self.get_palindrome_from(s, mid, mid))
        answer = max(answer, self.get_palindrome_from(s, mid, mid + 1))

    return s[answer[1]: answer[1] + answer[0]]
    
def get_palindrome_from(self, s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left += 1
        right -= 1
    return right - left - 1, left + 1 # abcbx (4-0-1, 0+1)

# Dynamic programming｜Time: O(n^2)
def longestPalindrome(self, s):
    if not s:
        return ""
    
    n = len(s)
    is_palindrome = [[False] * n] for _ in range(n)
    for i in range(n):
        is_palindrome[n][n] = True
    for i in range(1, n):
        is_palindrome[n][n -1] = True
    start, longest = 0, 1
    for length in range(2, n + 1): #長度枚舉
        for i in range(n - length + 1) #abcde 5-2+1=4 [n-2][n-1]是最後一組
        j = i + length - 1 #i=0, j=1
        is_palindrome[i][j] = is_palindrome[i+1][j-1] and s[i] == s[j]
        if is_palindrome[i][j] and length > longest:
            longest = length
            start = i
    return s[start: start + longest]
