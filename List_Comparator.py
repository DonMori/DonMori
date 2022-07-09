List = [1, 3, 1, 5, 2, 10, 5, 6, 4, 5]

num = 0
previous_num = 999

for value in List :
    if value > previous_num :
        num += 1
    previous_num = value

print("The amount of times that an element of the list grew is :",num )