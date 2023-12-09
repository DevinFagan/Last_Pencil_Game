import random

num = 0
while num < 1:
    try:
        num = int(input("How many pencils would you like to use:"))
        if num < 1:
            print("The number of pencils should be positive")
    except ValueError:
        print("The number of pencils should be numeric")

name = ["John", "Jack"]
player = "not_names"
while player not in name:
    player = input(f"Who will be the first (John, Jack):")
    if player not in name:
        print("Choose between 'John' and 'Jack'")

print(num * "|")
num_only = [1, 2, 3]
while num != 0:
    if player == name[0]:
        print(f"{player}'s turn!")
        player = name[1]
    else:
        print(f"{player}'s turn:")
        player = name[0]

    pencil = 'not_nums'
    while pencil not in num_only:
        if player == 'Jack':
            try:
                pencil = int(input())
                if pencil not in num_only:
                    print("Possible values: '1', '2' or '3'")

            except ValueError:
                print("Possible values: '1', '2' or '3'")

        elif player == 'John':
            if num % 4 == 0:
                pencil = 3
                print(pencil)

            elif num == 1:
                pencil = 1
                print(pencil)
            elif num % 2 == 1:
                pencil = 2
                print(pencil)

            elif num % 2 == 0:
                pencil = 1
                print(pencil)

            elif num % 4 == 1:
                pencil = random.randint(1, 3)
                print(pencil)

    while True:
        if pencil > num:
            if player == "Jack":
                print("Too many pencils were taken")
                print("John's turn:")
                try:
                    pencil = int(input())
                    if pencil not in num_only:
                        print("Possible values: '1', '2' or '3'")

                except ValueError:
                    print("Possible values: '1', '2' or '3'")

                if pencil <= num:
                    num -= pencil
                    break

            elif pencil <= num:
                if player == "John":
                    num -= pencil
                    break

        elif num > 0:
            num -= pencil
            print(num * "|")
            break

print(f"{player} won!")
