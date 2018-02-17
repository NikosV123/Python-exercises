# -*- coding: utf-8 -*-
number = raw_input("Παρακαλώ εισάγεται τον αριθμό που θα θέλατε να σχηματιστεί σε λατινική μορφή.\n")
number = str(number)
roman = ""
roman = str(roman)
romanM = ""
romanM = str(romanM)
number3 = ""
number6 = ""
roman3 = ""
roman6 = ""
for j in range (1,4):
    if (len(number) >= j):
        number3 = number[len(number)-j] + number3
for h in range (4,7):
    if (len(number) >= h):
        number6 = number[len(number)-h] + number6
r2 = ""
j = 0
if (0 == 1):
    x = 0
    y = 0
    pass
elif((int(number)<=0) | (int(number) != float(number))):
    print "Παρακαλώ εισάγεται έναν φυσικό αριθμό μεγαλύτερο του μηδέν!"
    x = 0
    y = 0
    pass
else:
    x = len(number3)
    y = len(number6)
romanM = ""
b = 0
romanM = romanM + "_" * int(int(number)/1000000)
roman = roman + "M" * int(int(number)/1000000)
for i in range (0,x):
    # Επί 10 στα λατινικά
    n = int(number3[i])
    roman3 = roman3.replace( "M" , "X")
    roman3 = roman3.replace( "C" , "M")
    roman3 = roman3.replace( "L" , "D")
    roman3 = roman3.replace( "X" , "C")
    roman3 = roman3.replace( "V" , "L")
    roman3 = roman3.replace( "I" , "X")
    if (n%5 == 4):
        roman3 = roman3 + "I"
        if (n == 4):
            roman3 = roman3 + "V"
        else:
            roman3 = roman3 + "X"
    else:
        if (n>= 5):
            roman3 = roman3 + "V"
        roman3 = roman3 + "I" * (n%5)
for i in range (0,y):
    n = int(number6[i])
    roman6 = roman6.replace( "M" , "X")
    roman6 = roman6.replace( "C" , "M")
    roman6 = roman6.replace( "L" , "D")
    roman6 = roman6.replace( "X" , "C")
    roman6 = roman6.replace( "V" , "L")
    roman6 = roman6.replace( "I" , "X")
    if (n%5 == 4):
        roman6 = roman6 + "I"
        if (n == 4):
            roman6 = roman6 + "V"
        else:
            roman6 = roman6 + "X"
    else:
        if (n>= 5):
            roman6 = roman6 + "V"
        roman6 = roman6 + "I" * (n%5)
romanM = romanM + "_" * len(roman6)
roman = roman + roman6
roman = roman + roman3
print romanM
print roman
#Η λογική που χρησιμοποίησα είναι να πάιρνει το πρώτο ψηφείο , μετα να τον πολλαπλασιάζει με το 10 (στα λατινικά) και τέλος να προσθέτει το επόμενο ψηφείο μέχρι να τελειώσουν οι αριθμοί
