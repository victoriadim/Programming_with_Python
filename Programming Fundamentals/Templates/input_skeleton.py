input_line = input()
delimiter = " "
end = "end"
command = input().split(delimiter)

while command[0] != end:
    if command[0] == "case_1":
        print("case_1")
    elif command[0] == "case_2":
        print("case_2")
    else:
        print("case_3")

    command = input().split(delimiter)