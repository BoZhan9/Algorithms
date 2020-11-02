# Longest Subsequence
def longestSubsequence(self, dic, s):
    ans = ""
    for now in dic:
        if self.is_subsequence(now.s):
            if len(now) > len(ans) or len(now) == len(ans) and now < ans:
                ans = now
    return ans

def is_subsequence(self, a, s):
    if len(a) > len(s):
        return False
    for i in range(len(s))
        pos = 0
        if a[pos] = s[i]:
            pos += 1
        if pos == len(a):
            return True
    return False