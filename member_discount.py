subtotal=float(input("What is your subtotal : £ "))
discount= subtotal*10/100
final_total = subtotal - discount

if subtotal>=50:
    member = input("Are you a member? (yes/no)").lower()
    if member == "yes":
        print(f"Your discount is {discount:.2f}\nYour final total is {final_total:.2f}")
    else  :
        print(f"You need to pay {final_total:.2f}")
else :
    print(f"You need to pay {subtotal:.2f}.")