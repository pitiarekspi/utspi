import datetime

try:
    days = int(input("Masukkan jumlah hari dari sekarang: "))
    date_from_now = datetime.datetime.now() + datetime.timedelta(days=days)
    formatted_date = date_from_now.strftime("%A, %B %d, %Y")
    print(formatted_date)

except ValueError:
    print("Data yang anda masukkan tidak valid.")