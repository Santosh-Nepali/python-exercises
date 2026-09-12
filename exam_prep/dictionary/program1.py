numbers = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numbers["Olga"] = "050-1011012"
numbers["Mary"] = "0401-2132139"

print(numbers)

name = input("Enter name: ")
if name in numbers:
    print(f"{name}'s phone number is {numbers[name]}.")
else:
    numbers[name]=input('Enter you phone number ::')

print(numbers)


x=int(5)
print(x=)
