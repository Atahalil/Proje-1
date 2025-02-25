#1. Proje
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

# Örnek kullanım
input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten(input_list)
print(output_list)

#2. Proje
def reverse_elements(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_list.append(reverse_elements(item)[::-1])
        else:
            reversed_list.append(item)
    return reversed_list

# Örnek kullanım
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_elements(input_list[::-1])
print(output_list)
