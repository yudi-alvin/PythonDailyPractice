s = "4,5,6,7;4,4,5,6,7"
l=list(",".join(s.split(";")).split(","))

res=[]
current=0
for x in sorted(l):
    if current != x:
        current = x
    else:
        res.append(x)
res = list(dict.fromkeys(res))
print(res)