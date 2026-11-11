print("Well come to Shop Bill Calculator\n")
name = input("What is your name : ")
item = input("Please Enter your Item : ")
price_per_item=float(input("Enter the item price : "))
print(f"Price per item: £{price_per_item:.2f}")
quantity= int(input("How may You want : "))
discount_percent=float(input("select your discount : [10 or 20 or 25] : "))
people=int(input("How many people plan to share: "))
subtotal=quantity*price_per_item
discount=subtotal*discount_percent/100
final_total=subtotal-discount
print("\n")
print("Hello "+name+"!")
print(f"Your name has {len(name)} characters.\nItem :{item}\nQuantity : {quantity}\nSubtotal : £{subtotal:.2f}\nDiscount : £{discount:.2f}\nFinal Total : £{final_total:.2f}\nEach person pays : £{final_total/people:.2f}\n\nThank you for shopping with us!")
