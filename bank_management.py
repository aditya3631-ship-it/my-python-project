import json
try:
   with open("bank.json") as file:
      accounts = json.load(file)
except FileNotFoundError:
   accounts = []

def add_account():
  new_account_no = input("enter acccount number : ")
  found = False
  for item in accounts:
     if item['account_no'] == new_account_no:
        found = True
        break
  if found:
     print("account already existed ")
  else:   
      name = input("enter your name : ")
      phone_no = (input("enter your mobile number : "))
      try:
         balance = int(input("enter your balance : "))
      except ValueError:
         print("invalid input")
         return
      if balance < 0:
         print("invalid balance")
         return

      account = {
     "name" : name,
     "account_no" : new_account_no,
     "phone_no" : phone_no,
     "balance" : balance
     } 
      accounts.append(account)
      print("account detail added successfully")

def view_account():
   if not accounts:
      print("accounts detail empty")
   else:
      for i, item in enumerate(accounts,start=1):
         print(f"accounts : {i}")
         print(f"name : {item['name']}")
         print(f"account-no : {item['account_no']}")
         print(f"phone-no : {item['phone_no']}")
         print(f"balance : {item['balance']}")
         print("-"*25)
      
def search_account():
   search_account_no = input("enter your account number : ")
   found = False
   for item in accounts:
      if item['account_no'] == search_account_no:
          
          print(f"name : {item['name']}")
          print(f"account-no : {item['account_no']}")
          print(f"phone-no : {item['phone_no']}")
          print(f"balance : {item['balance']}")
          print("-"*25)
          found = True
          break
   if not found:
      print("account not found")

def deposit_money():
   account_no = input("enter account number : ")
   found = False
   for item in accounts:
     if (account_no == item['account_no']):
      found = True
      print(f"name : {item['name']}")
      print(f"account_no : {item['account_no']}")
      print(f"balance : {item['balance']}")
      try:
        amount = int( input("enter amount you want to deposit : "))
      except ValueError:
         print("invalid input")
         return
      if amount > 0:
        item['balance'] += amount
        print(f"New balance: {item['balance']}")
      else:
         print("invalid amount")
      break
   if not found:
        print("invalid account number")

def withdraw_money():
   account_no = input("enter your account no : ")
   found =False
   for item in accounts:
      if account_no == item['account_no']:
         found = True
         print(f"name : {item['name']}")
         print(f"account_no : {item['account_no']}")
         print(f"balance : {item['balance']}")
         try:
           amount = int(input("enter amount you want to withdraw : "))
         except ValueError:
            print("invalid input")
            return
         if amount<=0:
            print("invalid amount")
         elif item['balance'] >= amount:
            item['balance'] -= amount
            print(f"New balance : {item['balance']}")
         else:
            print("insufficient amount")
         break
   if not found:
      print("invalid account number")

def transfer_money():
   sender_no = input("enter sender account number : ")
   receiver_no = input("enter receiver account number : ")
   if (sender_no == receiver_no):
      print("cannot transfer to the same account")
      return

   sender = None
   receiver = None

   for item in accounts:
      if item['account_no'] == sender_no:
         sender = item
      if item['account_no'] == receiver_no:
         receiver = item

   if sender is None:
      print("sender account not found")
      return
   if receiver is None:
      print("receiver account not found")
      return

   try:
     amount = int(input("enter amount to transfer : "))
   except ValueError:
      print("invalid input")
      return
   if amount <= 0:
      print("invalid amount")
      return
   if sender['balance'] < amount:
      print("insufficient balance")
      return

   sender['balance'] -= amount
   receiver['balance'] += amount

   print("money transferred successfully")
   print(f"sender new balance : {sender['balance']}")
   print(f"receiver new balance : {receiver['balance']}")

def update_account():
   account_no = input("enter account number: ")
   found = False
   for item in accounts:
      if item['account_no'] == account_no:
          print(f"name : {item['name']}")
          print(f"account-no : {item['account_no']}")
          print(f"phone-no : {item['phone_no']}")
          print(f"balance : {item['balance']}")
          print("-"*25)
          found = True
          break
   if not found:
         print("invalid account")
         return
   print("1. update name ")
   print("2. update mobile no")
   update = input("choose what do you want to update : ")
   if (update == "1"):
      new_name = input("enter new name : ")
      item['name'] = new_name
      print("name update successfully")

   elif (update == "2"):
      new_number = input("enter new number : ")
      item['phone_no'] = new_number
      print("phone number update successfully")

   else:
      print("invalid choice")

def delete_account():
   account_no = input("enter account number : ")
   found = False
   for item in accounts:
      if item['account_no'] == account_no:
         accounts.remove(item)
         print("account delete successfully")
         found = True
         break
   if not found:
      print("invalid account")

while True:
    print("\n===== Bank Management System =====")

    print("1. Create Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transfer Money")
    print("7. Update Account")
    print("8. Delete Account")
    print("9. Save Data and Exit")
    

    choice = input("enter your choice : ")
    if(choice == "1"):
        add_account()
    elif(choice == "2"):
       view_account()
    elif(choice == "3"):
       search_account()
    elif(choice == "4"):
       deposit_money()
    elif (choice == "5"):
       withdraw_money()
    elif (choice == "6"):
       transfer_money()
    elif (choice == "7"):
       update_account()
    elif (choice == "8"):
       delete_account()
    elif (choice == "9"):
       with open ("bank.json","w") as file:
          json.dump(accounts,file,indent=4)
       break
    else:
       print("invalid choice")