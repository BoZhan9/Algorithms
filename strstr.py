strStr | Time: O(n^2)
def strStr(self, source, target):
    if not target:
        return 0
    for i in range(len(source) - len(target) + 1):
        for j in range(target):
            if source[i] != target[j]
            break
        else:
            return i
    return -1


