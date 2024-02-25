try:
    suhu = float(input("Suhu anda :"))
    if suhu >= 38:
        print ("Kamu demam")
    else:
        print ("Kamu tidak demam")
except:
    print("Salah Format Bro")