# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = True
for X in True, False:
    for Y in True, False:
        for Z in True, False:
            result = result and (not(X or Y or Z)==(not X and not Y and not Z))
            print(f'X={X}   Y={Y}   Z={Z} -->   {result}')

