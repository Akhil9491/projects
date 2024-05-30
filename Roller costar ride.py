## if and else conditional operators ##
## ROLLERCOSTER PROJECT ##


print("welcome to the rollercoster ride at ATYETI")
hight = int(input("Conform your hight"))
bill = 0
if hight >= 100:
    print("take the ride")
    age = int(input("enter your age")) 
## nasted if condition 
    
    if age <= 15:
        bill = 14
        print("pay RS of 10$ to the ride dear child")
        
## using ELIF condition in between for aged citigion's who are grater 40 age ##
    
    elif age <= 29:
        bill = 19
        print("you have a special discount price pay us RS 15$ + GST, for a ride")

    elif age <= 39:
        bill = 33
        print("pay RS of 20$ + GST")
    elif age >=40 and age <=45:
        bill = 25
        print ("HELLO CITIGEN YOU HAVE NO GST OPTION 🎉")
    elif age >= 46 and age <= 55:
        print ("YOU ARE UNDER AGED CITIGEN HAVE A FREE RIDE, ENJOY THE MOMENT🙌")
    elif age > 56:
        print ("SORRY!! NO GRANTED FOR RIDE")
          
    PHOTO = input("for a pick we charge 5$ YES or NO ")    
    if PHOTO == "YES":
       bill +=  5
       print("your amount is $",bill)
    else:
        print("$", bill)
else:
    print ("sorry for this time - need bit more hight")
    print ("THANK YOU FOR VISITING")
