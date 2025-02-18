def luas_lingkaran(radius):
	return 3.14 * radius * radius

r = float(input("Masukkan jari-jari: "))
hasil = float(luas_lingkaran(r))
print(f"Luas lingkaran untuk jari-jari {r} adalah {hasil:.2f}")

