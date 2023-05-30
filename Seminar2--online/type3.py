temper = [-20, 30, 50, 35, -40, 50, 10, -10]
schet = 0
max_dlina = 0

for i in temper:
    if i > 0:
        schet += 1
    else:
        if schet > max_dlina:
            max_dlina = schet
        schet = 0


if schet > max_dlina:
    max_dlina = schet

print("Максимальное количество дней: ", max_dlina)