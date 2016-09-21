list_of_numbers = [9, 10, 5, 100, 23, 2]

half_values = []

for x in list_of_numbers:
    half_of_x = x
    # // is floor division 1/2 = .5 10/5 = 5.0
    half_values.append(half_of_x)

print(half_values)

#####################

list_of_numbers = [5, 2, 8, 2, 10, 5]

half_values = tuple(x / 2 for number in list_of_numbers)
print(half_values)

#####################

list_of_numbers = [100, 67, 23, 45, 11]

square_numbers = {}

for number in list_of_numbers:
    square_numbers[number] = number ** 2

    print(square_numbers)
#####################
# dictionary comprhenesion way of doing above

list_of_numbers = [9, 67, 23, 45, 11]

square_numbers = {number: number ** 2
                  for number in list_of_numbers}
print(square_numbers)

#####################

matrix = [["_", "x", "_"],
          ["o", "x", "o"],
          ["o", "x", "o"]]

target_column = []


for row in matrix:
    target_column.append(row[1])
    print(target_column)

####################

matrix = [["_", "x", "_"],
          ["o", "x", "o"],
          ["o", "x", "o"]]
target_column = [row[1]for row in matrix]
print(target_column)
