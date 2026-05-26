pole = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]

schet_x = 0
schet_o = 0

tekushiy_igrok = 0

def pokazat_pole():
    print("\n    1   2   3   4")
    print("  +---+---+---+---+")
    for i in range(4):
        print(f"{i + 1} | {pole[i][0]} | {pole[i][1]} | {pole[i][2]} | {pole[i][3]} |")
        print("  +---+---+---+---+")
    print()


def proverit_pobedu(simvol):
    for i in range(4):
        if pole[i][0] == simvol and pole[i][1] == simvol and pole[i][2] == simvol and pole[i][3] == simvol:
            return True
    for j in range(4):
        if pole[0][j] == simvol and pole[1][j] == simvol and pole[2][j] == simvol and pole[3][j] == simvol:
            return True
    if pole[0][0] == simvol and pole[1][1] == simvol and pole[2][2] == simvol and pole[3][3] == simvol:
        return True
    if pole[0][3] == simvol and pole[1][2] == simvol and pole[2][1] == simvol and pole[3][0] == simvol:
        return True
    return False


def proverit_nichyu():
    for i in range(4):
        for j in range(4):
            if pole[i][j] == ' ':
                return False
    return True


def ochistit_pole():
    for i in range(4):
        for j in range(4):
            pole[i][j] = ' '

print("=" * 50)
print("КРЕСТИКИ-НОЛИКИ 4x4")
print("=" * 50)
print("Правила: нужно собрать 4 одинаковых символа в строку, столбец или диагональ")
print("Координаты: строка и столбец от 1 до 4")
print("Пример: 2 3")
print("=" * 50)

while True:
    ochistit_pole()
    tekushiy_igrok = 0
    igra_aktivna = True
    while igra_aktivna:
        pokazat_pole()
        if tekushiy_igrok == 0:
            simvol = 'X'
            print("Ход игрока X")
        else:
            simvol = 'O'
            print("Ход игрока O")
        while True:
            try:
                stroka = int(input("Введите номер строки (1-4): "))
                stolbec = int(input("Введите номер столбца (1-4): "))
                if stroka < 1 or stroka > 4 or stolbec < 1 or stolbec > 4:
                    print("Ошибка! Числа должны быть от 1 до 4")
                    continue
                if pole[stroka - 1][stolbec - 1] != ' ':
                    print("Ошибка! Эта клетка уже занята")
                    continue
                pole[stroka - 1][stolbec - 1] = simvol
                break
            except ValueError:
                print("Ошибка! Введите целые числа")
        if proverit_pobedu(simvol):
            pokazat_pole()
            print(f"\nПОБЕДИЛ ИГРОК {simvol}!")
            if simvol == 'X':
                schet_x += 1
            else:
                schet_o += 1

            print(f"Счёт: X - {schet_x} : {schet_o} - O")
            igra_aktivna = False

        elif proverit_nichyu():
            pokazat_pole()
            print("\nНИЧЬЯ!")
            print(f"Счёт: X - {schet_x} : {schet_o} - O")
            igra_aktivna = False

        else:
            if tekushiy_igrok == 0:
                tekushiy_igrok = 1
            else:
                tekushiy_igrok = 0

    while True:
        otvet = input("\nХотите сыграть ещё? (да/нет): ").strip().lower()
        if otvet == "да" or otvet == "yes" or otvet == "д":
            print("\nНовая игра!")
            break
        elif otvet == "нет" or otvet == "no" or otvet == "н":
            print("\nСпасибо за игру!")
            exit()
        else:
            print("Введите 'да' или 'нет'")