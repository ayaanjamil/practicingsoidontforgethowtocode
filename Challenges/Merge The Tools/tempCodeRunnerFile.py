s = "AAABBBCCC"

for i in range(len(s)):
    if s[i] in s[i+1:len(s)]:
        s = s[i] + s[i+1:len(s)].replace(s[i], "")

print(s)