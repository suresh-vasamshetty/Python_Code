List = [1,2,4,6,3,6]
n = int(input("enter the number: "))

position = []

for index, value in enumerate(List):
    if value == n:
        position.append(index+1)

if position:
    print(f"Number {n} is found at position {position}")
else:
    print(f"Number {n} not found")
