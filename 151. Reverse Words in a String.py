def reverseWords(s: str) -> str:
    return ' '.join(reversed(s.split()))


print(reverseWords("the sky is blue"))