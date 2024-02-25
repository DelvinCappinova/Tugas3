try:
    
    bilangan1 = int(input("Masukkan Bilangan 1 ="))
    bilangan2 = int(input("Masukkan Bilangan 2 ="))
    bilangan3 = int(input("Masukkan Bilangan 3 ="))

    if bilangan1 == bilangan2 == bilangan3:
        print ("Ketiga sisi sama")
    elif bilangan1 == bilangan2 != bilangan3:
        print ("Kedua bilangan sama")
    elif bilangan2 == bilangan3 != bilangan1:
        print ("Kedua bilangan sama")
    elif bilangan3 == bilangan1 != bilangan2:
        print ("Kedua bilangan sama")
    else :
        print ("Tidak ada sisi yang sama")
except:
    print ("salah format bro")