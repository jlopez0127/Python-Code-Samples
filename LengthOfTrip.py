numbersToDays = {} 
Sunday: 0
Monday: 1
Tuesday: 2
Wednesday: 3
Thursday: 4
Friday: 5
Saturday: 6

startingDay = int(input("Enter the day you will be leaving on your trip, 0 being sunday, 1 being Monday,up to 6 being : "))
tripLength = int(input("Enter how many days you are going to be on your trip: "))
lastDay= (startingDay + tripLength)%7

print (lastDay)

#Julian Lopez
# 10/10/2023
#This program is to help users find out what day they are going to arrive by asking th euser when they will leave and whow long they plan to be gone for.