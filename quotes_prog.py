

with open('quotes.txt','r',encoding='UTF-8') as file:
    data=file.read()
    print(data)

author=input("Хто написав ці рядки?")

with open('quotes.txt','a',encoding='UTF-8') as file:
    file.write(f'\n{author}\n')

with open('quotes.txt','r',encoding='UTF-8') as file:
    data=file.read()
    print(data)

a= input("Хочете ще додати цитати і авторів?(так,ні)")

while a=="так":
    b=input ("Введіть цитату:")

    with open('quotes.txt','a',encoding='UTF-8') as file:
        file.write(f'\n{b}\n')

    with open('quotes.txt','r',encoding='UTF-8') as file:
        data=file.read()
        print(data)
    a= input("Хочете ще додати цитати і авторів?(так,ні)")

else:
    with open('quotes.txt','r',encoding='UTF-8') as file:
        data=file.read()
        print(data)
    
