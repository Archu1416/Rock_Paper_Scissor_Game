import random
print("WELCOME")
print() 
print("Enter 0 for Rock\nEnter 1 for Paper \nEnter 2 for Scissor\n")
while True:
    choice=int(input("Enter your choice: "))
    if choice==0:
        print("You have chose Rock")
    elif choice==1:
        print("You have chose Paper")
    elif choice==2:
        print("You have chose Scissor")
    else:
        print("Enter correct choice")
        continue
    print("Now it's turn for computer's choice")
    comp_choice=random.randint(0,2)
    if comp_choice==0:
        print("Computer's choice: Rock")
    elif comp_choice==1:
        print("Computer's choice: Paper")
    else:
        print("Computer's choice: Scissor")
    if(choice==1 and comp_choice==0) or (choice==2 and comp_choice==1) or (choice==0 and comp_choice==2):
        print("User wins!")
    elif (comp_choice==1 and choice==0) or (comp_choice==2 and choice==1) or (comp_choice==0 and choice==2):
        print("Computer wins!!")
    elif choice==comp_choice:
        print("It's a draw")
    print("If you want to play again? (Y?N)")
    x=input().upper()
    if x=='N':
        print("Thanks for playing!")
        break
     
