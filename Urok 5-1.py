with open("somefile.txt", "w") as b:
    while True:
        f = input("Введите строку: ")
        if f != " ":
            b.write(s + "\n")
        else:
            break