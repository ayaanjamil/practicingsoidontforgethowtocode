from datetime import datetime as dt

t1 = input("T1 - ")
t2 = input("T2 - ")

f = "%a %d %b %Y %H:%M:%S %z"

t1 = dt.strptime(t1, f)
t2 = dt.strptime(t2, f)
print(int(abs((t1 - t2).total_seconds())))