word = input()
dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

print(sum(i+3 for w in word for i,d in enumerate(dial) if w in d))