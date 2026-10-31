def sum_of_integers_in_string(stroke):
    total = 0        # здесь копим сумму
    current = ""     # здесь собираем текущее число по цифрам

    for num in stroke:
        if num.isdigit():
            current += num         # цифра — добавляем к текущему числу
        else:
            if current:            # встретили не-цифру, а число уже накоплено
                total += int(current)  # добавляем его к сумме
                current = ""       # сбрасываем буфер

    if current:              # если строка закончилась числом — не забываем его
        total += int(current)

    return total


# Проверка
s = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"
print(sum_of_integers_in_string(stroke))  # 3635