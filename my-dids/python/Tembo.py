def main_menu():
  print("""
sim 1
1:safaricom
2:M-pesa
             
""")

def m_pesa():
    print("""
1:send money
2:withdraw cash
3:Buy Airtime
4:loan and savings
5:lipa na M-pesa
6:my account                                                  
""")

def safaricom():
      print("welcome to safaricom servise!")
     

choice1 = input("Enter your code:")
if choice1 == "1":
      safaricom()
elif choice1 == "2":
       m_pesa()
else:
    print("invalid choice")    
    main_menu()  

def send_money():
     print("send money")
choice2 = input("Enter your code:")
if choice2 == "1":
   send_money()
choice3 =input("Enter Phone No:(Digits 0-9,*,#,+)10-13 characters: ")
def phone_No():
     print("Enter Phone number ")  
choice4 = input("Amount")
def Amount():
     print("enter amount:")     