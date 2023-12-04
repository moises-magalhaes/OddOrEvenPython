again="yes"
while again=="yes":
    num=int(input("Enter a number: "))
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
    again=input("Do you want to use the program again? ")
print("thank you!")
