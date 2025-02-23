numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = [3]
# numbers[-1] = [2]
# numbers[3] = [1]
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten" # 1. Change The First Element Of Numbers To "ten"
numbers[-1] = 1 # 2. Change The Last Element Of Numbers to 1
print(numbers[2:]) # 3. Print All The Elements From numbers Except The First Two
print(9 in numbers) # 4. Print Whether 9 Is An Element Of Numbers