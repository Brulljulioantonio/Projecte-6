# Què fa el programa: demana una sèrie de números i mostra el més gran
# Autor: Biel Rull Simon
# Data:  8/10/25

# Versió 1.0

nums = input("Introdueix numeros separats per espais: ")
nums = nums.split()
maxim = float(nums[0])
for i in nums:
    if float(i) > maxim:
        maxim = float(i)
print("El numero mes gran es:", maxim)