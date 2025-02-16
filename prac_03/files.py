# 1) Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.

# user_name = input("Enter Your Name: ")
# out_file = open("name.txt", "w")
# print(user_name, file=out_file)
# out_file.close()

# 2) In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output), Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable! Use open and close for this question.

# out_file = open("name.txt", "r")
# user = out_file.readline()
# print(f"Hi {user}!")
# out_file.close()

# 3)
#
# first_number = 0
# second_number = 0
#
# with open("numbers.txt", "r") as out_file:
#     for i in range(2):
#         lines = out_file.readline()
#         if i == 0:
#             first_number = int(lines.strip())
#         elif i == 1:
#             second_number = int(lines.strip())
# total_number = first_number + second_number
# print(total_number)

# 4)

total_number = 0

with open("numbers.txt", "r") as out_file:
    for i in out_file:
        total_number += int(i.strip())
print(total_number)