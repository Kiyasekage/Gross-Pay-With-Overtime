print("Welcome to counting your gross pay with overtime")
name = input("Input your username : ")
hour = int(input("Enter hours : "))
rate = float(input("Enter rate : "))
total_pay = 0
if hour>40:
    hour-=40
    gross_pay = hour*rate*1.5+40*10
    print(f"Your gross pay is {gross_pay},{name}00")
elif hour<=40:
    gross_pay = hour*rate
    print(f"Your gross pay is {gross_pay},{name}")
