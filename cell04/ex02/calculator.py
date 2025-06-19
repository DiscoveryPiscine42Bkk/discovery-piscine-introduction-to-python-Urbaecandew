num1 = int(input("Give me that first number:"))
num2 = int(input("Give me that second number:"))
print('Thank You')
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1}-{num2} = {num1 - num2}")
div = num1 / num2
if div == int(div):
    print(f"{num1} / {num2} = {int(num1 / num2)}")
else:
    print(f"{num1} / {num2} = {div}")
print(f"{num1} * {num2} = {num1 * num2}")
