# 6. Files

# 1.
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print("Your name is {}".format(name))

# 3.
in_file = open("numbers.txt", "r")
number_one = int(in_file.readline())
number_two = int(in_file.readline())
in_file.close()
result = number_one + number_two
print(result)

# 4.
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)