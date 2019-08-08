ui = input("Please enter a 4-digit number... ")
while int(ui) < 1000 or int(ui) > 9999:
    ui = input(
        "Number is not 4-digit, please try again... "
    )
    continue
digits = list((map(int, ui)))


def multiply_func(number):
    total = 1
    for x in number:
        total *= x
    print(total)


ui_reversed = ui[::-1]
ui_sorted = "".join(sorted(ui))

multiply_func(digits)
print(ui_reversed)
print(ui_sorted)
