# fibonacci_etActivite20
Realisation de la suite de fibonacci de maniere recursif et la realisation des taches de l'activite 20
#ACTIVITE19_QUESTION7
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
#ACTIVITE20

#On declare la liste

adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]

#Quel est la premier adresse de la liste
print(adresses_ip[0])

##Quel est la derniere adresse de la liste
print(adresses_ip[-1])

#Quel est la troisieme adresse dans la liste
print(adresses_ip[2])

#Ajout de l'adresse "172.31.0.1" a la liste
adresses_ip.append("172.31.0.1")

#supprimer l'adresse IP "200.100.50.1"
adresses_ip.remove("200.100.50.1")
                #ou on pouvait faire adresses_ip.pop(3) ou del adresses_ip[3]

#combien d'adresses restent maintenant ?
print(f"Ils restent maintenant {len(adresses_ip)} adresses dans la liste")

#verifier si l'adresse "192.168.0.1" est presente
if "192.168.0.1" in adresses_ip:
    print("Oui l'adresse \"192.168.0.1\" est presente")
else :
    print("Non l'adresse \"192.168.0.1\" n'existe pas")

#quelle est la classe de l'adresse IP de "10.0.0.1"
    #Maintenant on va travailler avec le dictionnaire pour que cela aura un sens

adresses_ip={
    "192.168.0.1":"classe C",
    "10.0.0.1":"classe A",
    "172.16.0.1":"classe B",
    "200.100.50.1":"adresses IP publique",
    "169.254.0.1":"adresse IP de lien local(APIPA)"
            }
    #on pouvait creer le dictionnaire avec adresses_ip=dict.fromkeys(adresses_ip) mais ca va etre dans plus de lignes de code
    #  et on devait aussi modifier la liste avant d'execute dict.fromkeys

print("La classe de l'adresse IP de \"10.0.0.1\" est ",adresses_ip["10.0.0.1"])

#trie des adresses par ordre croissant
adresses_ip=dict(sorted(adresses_ip.items()))
print(adresses_ip)

#verifions si toutes les adresses IP de la liste appartiennent a la classe C
d=True
for i in adresses_ip.values():
    if i!="Classe C":
        d=False
        break
print(f"toutes les adresses IP de la liste appartiennent a la classe C est {d}")

d=0
for i in adresses_ip.values():
    if i=="adresses IP publique":
        d+=1
print(f"on a {d} adresses IP publique dans la liste")




