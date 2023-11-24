sk = int(input("Ievadiet skaitli: "))

if sk % 3 == 0 and sk % 7 == 0:
    print(f"{sk} dalās ar 3 un 7")
else:
    print(f"{sk} nedalās ar 3 un 7 vai dalās tikai ar vienu no tiem")
