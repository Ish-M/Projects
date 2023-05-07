# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:25:27 2022

@author: Ishaan
"""
from datetime import timedelta
from datetime import datetime
def findA(century):
    if century%4 == 0:
        return 2
    elif century%4 == 1:
        return 0
    elif century%4 == 3:
        return 3
    elif century%4 == 2:
        return 5
def findB(year):
    return year // 12
def findC(year):
    return year % 12
monthinput = input("What month is it(as a number)? ")
dayinput = input("What is the day of the month? ")

yearwhole = input("What year is it? ")
century = int(yearwhole [0:2])
year = int(yearwhole[2:5])
date1 = datetime(day=int(dayinput), month = int(monthinput), year = 1)
date2 = datetime(day = 4, month = 1, year = 1)
date3 = datetime (day = 3, month = 1, year = 1)
VarA = findA(century)
VarB= findB(year)
VarC = findC(year)
VarD = VarC // 4
yearh=int(yearwhole)
if (yearh%400 == 0):
          VarE = (date1-date2).days
elif (yearh%100 == 0):
          VarE = (date1-date3).days
elif (yearh%4 == 0):
          VarE = (date1-date2).days
else:
          VarE = (date1-date3).days



totalvar=VarA+VarB+VarC+VarD+VarE
daytable = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
finalans = (totalvar%7)
answer = daytable[finalans]
print ("It will be a "+ answer + " on "+ monthinput+ "/" + dayinput + "/" + yearwhole)