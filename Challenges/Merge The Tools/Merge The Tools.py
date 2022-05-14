def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s1 = ""
        for j in range(len((string[i:i+k]))):
            if (string[i:i+k])[j] not in s1:
                s1 = s1 + (string[i:i+k])[j]
        print(s1)
#did not want to name the variable "string" but stupid hackerrank