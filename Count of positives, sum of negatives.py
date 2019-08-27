def count_positives_sum_negatives(arr):
    y = 0
    z = 0
    if arr == []:
        return arr
    for x in arr:
        if x <= 0:
            z += x
        else:
            y += 1
    return [y, z] 