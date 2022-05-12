scoreKevin = 0
scoreStuart = 0
s = input("Enter a word - ")
s = s.upper()

for i in range(len(s)):
    if s[i] in "AEIOU":
        scoreKevin += (len(s)-i)
    else:
        scoreStuart += (len(s)-i)

if scoreKevin > scoreStuart:
    print("Kevin",str(scoreKevin))
elif scoreKevin < scoreStuart:
    print("Stuart",str(scoreStuart))
else:
    print("Draw")