sk1 = int(input("Ievadiet skaitli: "))

if sk1 < 0:
    print("Faktoriāls šādam skaitlim nepastāv!")
else:
    fakt = 1
    for i in range(1, sk1 + 1):
        fakt *= i

    print(f"Faktoriāls skaitilm {sk1} ir {fakt}")
