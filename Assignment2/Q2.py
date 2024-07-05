arr = []

while True:
    user_input = input("Enter an element:-")
    arr.append(user_input)

    c = input("Continue(Y/N):-")
    if c == "n" or c == "N":
        break
    elif c == "y" or c == "Y":
        continue
    else:
        print("Wrong Input!")
        break

print(arr)