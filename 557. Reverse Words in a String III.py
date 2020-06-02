def reverseWords(s: str) -> str:
    return " ".join([i[::-1] for i in s.split()])


print(reverseWords("Let's take LeetCode contest"))
