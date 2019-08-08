var_dict = {
    "Q" : "Please enter variable ",
    "A" : "A... ",
    "B" : "B... ",
    "E" : "Please enter a number, not a word or symbol" 
}

var_a = input(var_dict["Q"] + var_dict["A"])
while (var_a.isdigit() == False):
    print(var_dict["E"])
    var_a = input(var_dict["Q"] + var_dict["A"])
    continue
var_b = input(var_dict["Q"] + var_dict["B"])
while (var_b.isdigit() == False):
    print(var_dict["E"])
    var_b = input(var_dict["Q"] + var_dict["B"])
    continue
var_a_f = float(var_a)
var_b_f = float(var_b)
print(
    "A = " + str(var_a_f),
    "B = " + str(var_b_f),
    "A + B = " + str(var_a_f + var_b_f),
    "A - B = " + str(var_a_f - var_b_f),
    "A * B = " + str(var_a_f * var_b_f),
    "A / B = " + str(var_a_f / var_b_f),
    sep="\n"
)