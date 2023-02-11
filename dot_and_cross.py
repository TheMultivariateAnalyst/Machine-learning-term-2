def dot_product(list1, list2):
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]
    return result

def cross_product(list1, list2):
    i = (list1[1]*list2[2]) - (list1[2]*list2[1])
    j = (list1[2]*list2[0]) - (list1[0]*list2[2])
    k = (list1[0]*list2[1]) - (list1[1]*list2[0])
    return [i, j, k]

# test dot product
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Dot product:", dot_product(list1, list2))

# test cross product
list3 = [2, 3, 4]
list4 = [5, 6, 7]
print("Cross product:", cross_product(list3, list4))
