# subtotal = float(input("Enter order subtotal : £"))
#
# if subtotal >=50:
#     delivery_fee=0
# elif 25<= subtotal <50:
#     delivery_fee=2.00
# else:
#     delivery_fee=3.50
#
#
# final_total = subtotal+delivery_fee
#
# print(f"Delivery fee: £{delivery_fee:.2f}")
# print(f"Final total: £{final_total:.2f}")


print("Shop Bill calculate")
name=input("Enter Your name : ")
item=input("Enter Your Item : ")
price_per_iteam=float(input("Enter your item price : £"))
quantity=int(input("How many you want : "))
discount_percentage=float(input("Enter your percentage : [10 ,20 ,30] "))
number_of_people=int(input("How meany people want to share : "))
subtotal=price_per_iteam*quantity
discount=subtotal*discount_percentage/100
final_total=subtotal-discount
if number_of_people >= 1:
    each_person_pay = final_total / number_of_people
    print(f"Each person pays: £{each_person_pay:.2f}")
else:
    print("Please enter at least 1 person.")

print(f"Hello {name} !\nYour name has {len(name)} characters.\nItem :{item}\nQuantity : {quantity:.2f}\nSubtotal: {subtotal:.2f}\nDiscount : {discount:.2f}\nFinal Total: {final_total:.2f}")


