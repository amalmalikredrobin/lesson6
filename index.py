# age = int(input('Vvedite svoy vozrast'))

# if age >= 18 and age <= 50:
#     print('Welcome')
# else: print('Bye')

cost=int(input("vvedite stoimost azakaza: "))
money=int(input("vvedite summu kotoruyu vy dali: "))

if cost % 100 == 0 and money % 100 ==0:
     change = money - cost
     five_hundreds = change // 500
     change = money - cost

     two_hundreds= change // 200
     change = change % 200

     hundreds = change // 100
     print(five_hundreds, two_hundreds, hundreds)


print(500//5)