import sys
import subprocess

#import ModulFact
#print(ModulFact.main(5))

a = str(subprocess.check_output([sys.executable, "ModulFact.py", input("Введите число: ")]))
a = a[2:]
a = a[:-5]
print("Факториал: ", a)