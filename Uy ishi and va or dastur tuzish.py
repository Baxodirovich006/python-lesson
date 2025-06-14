# Uy ishi and or bilan dastur tuzish

ilovalar=input("Salom ilovarni kurishga xush kelibsiz ilovalarni kurib ciqing marxamat[instagram,telegram,youtube,chroome,capcut]>>")

if ilovalar=="instagram":
    print(f"{ilovalar}")
elif ilovalar=="telegram":
    print(f"{ilovalar}")
elif ilovalar=="youtube":
    print(f"{ilovalar}")
elif ilovalar=="chroome":
    print(f"{ilovalar}")
elif ilovalar=="capcut":
    print(f"{ilovalar}")
else:
    print("kechirasiz bu yerdagi ilovlar ichida siz aytgan ilova mavjud emas")

sirk=int(input("iltimos yoshingizni kiriting >>"))

if sirk<18 or sirk==18:
    print("sizga kirish narxi 22.000 som")
elif sirk<=40:
    print("sizga kirish narxi 44.000 som")
elif sirk>40 and sirk<50:
    print("sizga kirish narxi 55.000 som")
elif sirk<=60:
    print("sizga kirish narxi 60.000 som")
elif sirk>60:
    print("siz uchun kirish bepul")
else:
    print("xatolik iltimos amalingizni tekshirib koring")


































































