filepath = input().split("\\")
filename_and_axtension = filepath[-1]
filename, extension = filename_and_axtension.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")