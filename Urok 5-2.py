with open("bom.txt", "r") as b:
    elems = b.readlines()
    str_num = len(elems)
    print(f"Количество строк в файле: {str_num}")
    for i in range(str_num):
        print(f"{i + 1} строка: {len(elems[i].split(''))} слов")