#q1
# l= [5,6,77,45,22,12,24]
# t= [p for p in l if p%2 == 1]
# print(t)

# #q2
# s = [12,24,35,70,88,120,155]
# o = [v for v in s if v%5 !=0 and v%7 !=0]
# print(o)

#q3
# a= [12,24,35,70,88,120,155]
# b = [(c, value) for c, value in enumerate(a,0) if c%2 == 0]
# print(b)

#q4


#q5
c = [12,24,35,70,88,120,155]
d = [(e, value) for e, value in enumerate(c, 0) if (e, value) == (0,12) or (4,88) or (5,120)]
print(d)
