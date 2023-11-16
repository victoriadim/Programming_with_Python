products = input()
products_list = products.split()
products_dict = dict()
key_backup = None

# for index, item in enumerate(products_list):
#     if index % 2 == 0:
#         key_backup = item
#     else:
#         products_dict[key_backup] = int(item)

for i in range(0, len(products_list), 2):
    key = products_list[i]
    values = products_list[i + 1]
    products_dict[key] = int(values)

print(products_dict)