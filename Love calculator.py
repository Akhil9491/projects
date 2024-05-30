##LOVE CALCULATOR ##
## USING STRING DATA TYPE##

print ("WELCOME BACK TO THE LOVE CALCULATOR")
NAME1 = input("ENTER FIRST NAME")
NAME2 = input("ENTER SECOND NAME")
##combining the names using + operator to pass as single string value ##
## and caps to lowe convert using low() method ##
COUPPLE_NAME = NAME1 + NAME2
LOWER_NAMING = COUPPLE_NAME.lower()

t = LOWER_NAMING.count("t")
r = LOWER_NAMING.count("r")
u = LOWER_NAMING.count("u")
e = LOWER_NAMING.count("t")

FIRST_DIGIT = t + r + u + e

l = LOWER_NAMING.count("l")
o = LOWER_NAMING.count("o")
v= LOWER_NAMING.count("v")
e = LOWER_NAMING.count("e")

SECOND_DIGIT = l + o + v + e

SCORE = int(str(FIRST_DIGIT) + str(SECOND_DIGIT))
if (SCORE < 10) or (SCORE == 10):
  print ("YOUR LOVE SCORE IS", SCORE)
elif (SCORE <15) or (SCORE < 20):
  print("your love score is", SCORE)
else:
  print("GREAT COUPPLE", SCORE)
print ("❤THANK YOU FOR CHOSING ME❤")