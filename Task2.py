# mengambil batas atas rentang dari input pengguna
num = int(input("Enter a number: "))

# Menginisialisasikan produk dari 1
product = 1

# menghitung hasil kali semua nilai dari 1 hingga angka input
for i in range(1, num+1):
  product *= i

# Menampilkan hasil produk
print("The product of all the values from 1 to {} is: {}".format(num, product))