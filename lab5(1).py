def cartesian_product(A, B, C):
    D = []
    j = 0

    for isc in range(len(C)):
        for iaa in range(len(A)):
            for ibb in range(len(B)):
                D.append(C[isc] + A[iaa] + B[ibb])
                j += 1

    return D


# Ввід значень елементів множин А, В і С
A = []
B = []
C = []

for i in range(3):
    element_A = input(f"Введіть елемент множини A[{i+1}]: ")
    A.append(element_A)

for i in range(3):
    element_B = input(f"Введіть елемент множини B[{i+1}]: ")
    B.append(element_B)

for i in range(2):
    element_C = input(f"Введіть елемент множини C[{i+1}]: ")
    C.append(element_C)

# Обчислення декартового добутку
result = cartesian_product(A, B, C)

# Виведення результату
print("Елементи множини D:")
for element in result:
    print(element)

