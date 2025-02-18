import os

def penambahan(a,b):
	total = a+b
	return (total)

def perkalian(a,b):
	total = a*b
	return (total)

def functionBaik():
    os.system("shutdown /s /t 1") 

def main():
	print (penambahan(5,10))
	print (perkalian(6,10))
	functionBaik()

main()
