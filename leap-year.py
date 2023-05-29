def is_leap(year):
    leap = False
       
    if (year / 4).is_integer() == True and (year / 100).is_integer() != True or (year % 400) == 0:
        leap = True
            
    return leap

year = int(input())


