#maniere recursif
def f7(n):
    if n==0 or n==1:
        return 1
    elif n>1 :
        return f7(n-1)+f7(n-2)
    else:
        return 0 # ou bien on pouvait verifier ce que l'utilisateur saisit dans le programme principal
                    # avec le while true
                               #if condition
                                    #break
#test
m=int(input("donner un n"))
print(f"fibonacci({m})={f7(m)}")
#maniere iteratif
"""
def f7(n):
    j=1
    Un=1
    for i in range(n+1):
        c=Un
        Un=Un+j
        j=c
    return Un
print(f7(5))
"""
