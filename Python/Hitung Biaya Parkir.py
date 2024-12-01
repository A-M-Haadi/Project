while True:
    try:
        jam = int(input("Masukkan durasi parkir (dalam jam): "))
        break
    except:
        print("Maaf, input tidak valid. Silakan masukkan angka saja.")

harga = 0

if jam == 1:
    harga += 5.000
else:
    harga = 5000 + (jam - 1) * 3000

print(f"Biaya parkir yang harus dibayar: Rp {harga}")