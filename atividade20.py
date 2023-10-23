import random
random_int=random.randint(0, 5)
numero=int(input("numero: "))
if numero == random_int:
    print("voce acertou")
else: 
    print(f"numero errado , o certo era {random_int}")