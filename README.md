Description

Ce projet contient deux fichiers Python démontrant différents concepts de programmation :

fibonacci.py : Ce fichier contient une implémentation de la suite de Fibonacci en utilisant une approche récursive. Une approche itérative est également incluse, mais commentée.

Activite20.py : Ce fichier illustre la manipulation des adresses IP dans une liste et un dictionnaire. Il permet de réaliser plusieurs opérations comme la recherche d'adresses, l'ajout, la suppression et le tri des adresses IP.

Fichiers
1. fibonacci.py

Ce fichier contient une fonction pour calculer les nombres de la suite de Fibonacci de manière récursive. La fonction f7(n) utilise la récursivité pour calculer le n-ème terme de la suite de Fibonacci.

Fonctionnalité :

Récursif : Calcul du n-ème terme de la suite de Fibonacci.

La fonction f7(n) vérifie si n est égal à 0 ou 1 et retourne 1 dans ce cas. Sinon, elle effectue une somme récursive des deux termes précédents.

Exécution :

L'utilisateur doit entrer un nombre entier n, et le programme affiche le n-ème terme de la suite de Fibonacci.
Exemple d'exécution :
$ python fibonacci.py
donner un n: 5
fibonacci(5) = 5
Code :
# manière récursive
def f7(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return f7(n-1) + f7(n-2)
    else:
        return 0

# test
m = int(input("donner un n"))
print(f"fibonacci({m}) = {f7(m)}")
Activite20.py
Ce fichier permet de travailler avec une liste d'adresses IP et un dictionnaire qui associe des adresses IP à des classes d'adresses. Il permet d'effectuer plusieurs opérations de manipulation de données.
Liste d'adresses IP : Recherche de la première, dernière, et troisième adresse dans la liste.

Ajout et suppression d'adresses IP.

Vérification de la présence d'une adresse IP dans la liste.

Dictionnaire d'adresses IP : Trie des adresses IP par ordre croissant et vérification de leur classe.
Exécution :
Le programme affiche les résultats des opérations sur la liste d'adresses IP et le dictionnaire.
$ python Activite20.py
192.168.0.1
169.254.0.1
172.16.0.1
Ils restent maintenant 6 adresses dans la liste
Oui l'adresse "192.168.0.1" est présente
La classe de l'adresse IP de "10.0.0.1" est classe A
Code :
# On déclare la liste d'adresses IP
adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

# Opérations sur la liste
print(adresses_ip[0])  # Premier élément
print(adresses_ip[-1])  # Dernier élément
print(adresses_ip[2])  # Troisième élément
adresses_ip.append("172.31.0.1")  # Ajout d'une adresse
adresses_ip.remove("200.100.50.1")  # Suppression d'une adresse

print(f"Ils restent maintenant {len(adresses_ip)} adresses dans la liste")

if "192.168.0.1" in adresses_ip:
    print("Oui l'adresse \"192.168.0.1\" est présente")
else:
    print("Non l'adresse \"192.168.0.1\" n'existe pas")

# Dictionnaire d'adresses IP et leurs classes
adresses_ip = {
    "192.168.0.1": "classe C",
    "10.0.0.1": "classe A",
    "172.16.0.1": "classe B",
    "200.100.50.1": "adresses IP publique",
    "169.254.0.1": "adresse IP de lien local (APIPA)"
}

print("La classe de l'adresse IP de \"10.0.0.1\" est ", adresses_ip["10.0.0.1"])

# Tri des adresses IP
adresses_ip = dict(sorted(adresses_ip.items()))
print(adresses_ip)

# Vérification des classes
d = True
for i in adresses_ip.values():
    if i != "Classe C":
        d = False
        break
print(f"Toutes les adresses IP de la liste appartiennent à la classe C : {d}")

d = 0
for i in adresses_ip.values():
    if i == "adresses IP publique":
        d += 1
print(f"On a {d} adresses IP publique dans la liste")
Installation
Clonez ce dépôt :
https://github.com/chefaouiOthman/fibonacci_etActivite20
Assurez-vous que Python est installé (version 3.x recommandée).
Exécutez les fichiers Python avec la commande suivante :
python fibonacci.py
python Activite20.py


Contribution
Si vous souhaitez contribuer à ce projet, vous pouvez envoyer des pull requests ou ouvrir des issues pour discuter des améliorations possibles.
