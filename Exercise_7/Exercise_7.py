# -*- coding: utf-8 -*-
import time
import datetime
year = int(datetime.datetime.now().strftime("%Y"))
month = int(datetime.datetime.now().strftime("%m"))
day = int(datetime.datetime.now().strftime("%d"))
weekday = int(datetime.date.today().strftime("%w"))
number_of_dates = 0
# monday = 1
first_weekday_of_month = datetime.datetime(year, month, 1, 20, 00)
first_weekday_of_month = int(first_weekday_of_month.strftime("%w"))
#βρίσκω το first_weekday_of_month για να βρώ στην συνέχεια το second_weekday_of_month με day 8 (2 μέρες που έχουν σχεδόν την ίδια λογική)
if ((day < 9) & (day > 0)):
    extra_day = 1
else:
    extra_day = 0
    #βλέπω την περίπτωση αν στον σημερηνή ημερομηνία με μήνα x που ήμαστε ισχύει: a/x/year όπου 1/x/year είναι δευτέρα αρα έιναι και η 8/x/yearα δευτέρα όπου a<8 ( εξέρεση της μεθοδολογίας μου)
for i in range (0,120):
    # January = 1
    month_count = month + i
    if (month_count > 12):
        month_count = (month + i) % 12
    year_count = year + int((month + i) / 12)
    if (month_count == 2):
        #Το πρώτο weekday του μήνα αλλάζει ανάλογα με το υπόλυπο της διαίρεσης του πόσες μέρες έχει ο κάθε μήνας
        if ((year_count % 4) == 0):
            first_weekday_of_month = first_weekday_of_month + 1
    elif (((month_count % 2) == 1) & (month_count < 8)):
        first_weekday_of_month = first_weekday_of_month + 3
    elif ((month_count % 2) == 0) & (month_count >7):
        first_weekday_of_month = first_weekday_of_month + 3
    else:
        first_weekday_of_month = first_weekday_of_month + 2
    first_weekday_of_month = first_weekday_of_month % 7
    if (first_weekday_of_month == 1):
        number_of_dates = number_of_dates + 1
if ((month_count == 0) & (day < 9) & (day > 0) & (number_of_dates != 0)):
    number_of_dates = number_of_dates - 1
    #Το ίδιο με παραπάνω για αυτήν την εξέρεση.
print number_of_dates
#Το να βρω τις Δευτέρες την 8η μέρα του κάθε μήνα είναι το ίδιο με το ίδιο σχεδόν με το να βρείς τις Δευτέρες την 1η μέρα του κάθε μήνα
