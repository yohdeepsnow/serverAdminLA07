def calculator():
	
	print("Ini kalkulator buat 2 angka")
	print("Yang basic-basic aja: +, -, *, /")
	
	try:
		num1 = float(input("Num 1: "))
		operator = input("Masukkan operator: ")
		num2 = float(input("Num 2: "))

		if operator == '+':
			result = num1 + num2
		elif operator == '-':
			result = num1 - num2
		elif operator == '*':
			result = num1 * num2
		elif operator == '/':
			result = num1 / num2
		else:
			print("Operator salah")
			return

		print(f"Hasil: {result}")
	except ValueError:
		print("Input lu gajelas ga valid, masukin angka")

calculator()
