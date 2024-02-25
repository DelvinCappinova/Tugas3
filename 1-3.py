try:
    bilangan1 = int(input("Masukkan Bilangan 1 ="))
    bilangan2 = int(input("Masukkan Bilangan 2 ="))
    bilangan3 = int(input("Masukkan Bilangan 3 ="))
    
    if bilangan1 > bilangan2 and bilangan1 > bilangan3:
        print ("Bilangan 1 adalah yang terbesar")
    elif bilangan2 > bilangan1 and bilangan2 > bilangan3:
        print ("Bilangan 2 adalah yang terbesar")
    elif bilangan3 > bilangan1 and bilangan3 > bilangan2:
        print ("Bilangan 3 adalah yang terbesar")
except:
    print ("Salah Format Bro")