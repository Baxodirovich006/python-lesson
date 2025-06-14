# x=[1,2,3,4,5,6,7,8,9]

# for y in x:
#     if y==4:
#         continue
#     else:
#         print(y)
        
    
# ishora=True

# while ishora:
#     gmail=input("gmailni kiriting (to'xtatish uchun exit) ::> ")
#     kod=input("kodingizni kiriting(to'xtatish uchun exit)::>")
#     if gmail=="exit" or kod=='exit':
#         print("dastur tugadi")
#         ishora=False
#     elif gmail=="zafar" or kod==3434:
#         print("siz royxatdan o'tdingiz")
#     elif gmail=="ramiz" or kod==2323:
#         print("siz royxatdan o'tdingiz")
#     elif gmail=="bexruz" or kod==5454:
#         print("siz royxatdan o'tdingiz")
#     elif gmail=="anvar" or kod==1111:
#         print("siz royxatdan o'tdingiz")
#     else:
#         print("siz ro'yxatdan o'ta olmadingiz")

uy_hayvoni = ["it","mushuk"]
yovvoyi_hayvon = ["jirafa","ilon"]

while True:
    hayvon = input("biror hayvon nomini kiriting (to'xtatish uchun 'stop' deb yozing): ")
    
    if hayvon == 'stop':
        print("Dastur to‘xtatildi.")
        break
    elif hayvon in uy_hayvoni:
        print(f"{hayvon} - bu xonaki hayvon.")
    elif hayvon in yovvoyi_hayvon:
        print(f"{hayvon} - bu yovvoyi hayvon.")
    else:
        print(f"{hayvon} haqida ma'lumot yo‘q.")



















































































