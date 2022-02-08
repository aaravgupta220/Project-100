class Atm : 
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print('Your balance is Rupees 1000')

    def cashwithdrawal(self, amount):
        new_amount = 1000 - amount
        print("You withdrawed : " + str(amount) + "Your remaining balance is : " + str(new_amount))

def main():
        cardnumber = input("What is your card number : ")
        pin = input("What is your pin number : ")
        new_user = Atm(cardnumber, pin)

        print("Choose your activity : ")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter acticity choice : "))
        
        if(activity == 1):
            new_user.balanceinquiry()
        elif(activity == 2):
            amount = int(input("Enter the ammount : "))
            new_user.cashwithdrawal(amount)
        else : 
            print("Enter a valid amount")

if __name__ == "__main__":
    main()