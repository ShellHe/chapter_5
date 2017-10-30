def daynumtoname(num):
    if num == 0:
        return "Sunday"
    if num == 1:
        return "Monday"
    if num == 2:
        return "Tuesday"
    if num == 3:
        return "Wednesday"
    if num == 4:
        return "Thursday"
    if num ==  5:
        return "Friday"
    if num == 6:
        return "Saturday"
    else:
        return "Please enter an integer between 0 and 6."
print(daynumtoname(int(input("Please enter an integer between 0 and 6."))))    