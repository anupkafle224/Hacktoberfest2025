def kmp_search(text, pattern):
    # Preprocess pattern to get LPS array
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    
    # Search
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j  # Found at index
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # Not found

# Example
print(kmp_search("abxabcabcaby", "abcaby"))  # 6
