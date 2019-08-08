var_list = [
    "Please enter variable ",
    "A... ",
    "B... ",
    "Please enter a number, not a word or symbol" 
]

var_a = input(var_list[0] + var_list[1])
while var_a.isdigit() == False:
    print(var_list[3])
    var_a = input(var_list[0] + var_list[1])
    continue
var_b = input(var_list[0] + var_list[2])
while var_b.isdigit() == False:
    print(var_list[3])
    var_b = input(var_list[0] + var_list[2])
    continue
var_a_f = float(var_a)
var_b_f = float(var_b)
print("",
    "A = " + str(var_a_f),
    "B = " + str(var_b_f),
    "A + B = " + str(var_a_f + var_b_f),
    "A - B = " + str(var_a_f - var_b_f),
    "A * B = " + str(var_a_f * var_b_f),
    "A / B = " + str(var_a_f / var_b_f),
    sep="\n",
)
