import os
import math

# 1. Imprimir el directorio de trabajo actual
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# 2. Pedir un entero al usuario
num = int(input("Enter an integer: "))

# Calcular log base 2
log_val = math.log2(num)
print(f"Log base 2 of {num} is: {log_val}")

# 3. Imprimir piso y techo
print(f"Floor: {math.floor(log_val)}")
print(f"Ceiling: {math.ceil(log_val)}")