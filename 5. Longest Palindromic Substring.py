def longestPalindrome(s: str) -> str:
    n = len(s)
    bool_table = [[0 for _ in range(n)] for _ in range(n)]
    # all substrings of length 1 are palindromes
    max_len = 1
    i = 0
    while i < n:
        bool_table[i][i] = True
        i += 1
        start = i
    # check for substring of length 2
    start = 0
    i = 0
    while i < n - 1:
        if s[i] == s[i + 1]:
            bool_table[i][i + 1] = True
            start = i
            max_len = 2
        i += 1
    # check for lengths greater than 2.
    # k is the length of substring
    k = 3
    while k <= n:
        # fix the starting index
        i = 0
        while i < (n - k + 1):
            # get the ending index of substring
            # from starting index i and length k
            j = i + k - 1
            # checking for sub-string from ith
            # index to jth index iff s[i + 1] to
            # s[j - 1] is a palindrome
            if bool_table[i + 1][j - 1] and s[i] == s[j]:
                bool_table[i][j] = True
                if k >= max_len:
                    start = i
                    max_len = k
            i += 1
        k += 1
    return s[start: start + max_len]


#print(longestPalindrome("babad"))
#print(longestPalindrome("cbbd"))
print(longestPalindrome("caba"))
