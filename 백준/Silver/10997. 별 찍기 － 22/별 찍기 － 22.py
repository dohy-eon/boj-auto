n = int(input())
print("*"*(4*n-3))
for i in range(n-1):
    print(("* "*(i+1)+" "*(4*n-4*i-5)+" *"*i).strip())
    print("* "*(i+1)+"*"*(4*n-4*i-5)+" *"*i)
if n != 1:
    print("* "*(2*n-1))
    print("* "*(2*n-1))
for i in range(n-1):
    print("* "*(n-1-i)+" "*(4*i+1)+" *"*(n-1-i))
    print("* "*(n-2-i)+"*"*(4*i+5)+" *"*(n-2-i))