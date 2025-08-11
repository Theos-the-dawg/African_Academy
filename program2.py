import datetime
def hello():
    name = input("Enter your name: ")
    print(f"hello, {name}")


def show_date():
    date_today= datetime.date.today()
    now=datetime.datetime.now()
    #year/mm/dd/H/M/S
    future= datetime.datetime.now() + datetime.timedelta(days=2)
    print("Today's date is: 2023-10-05")
    print(f"Today's date is: {date_today}")
    print(f"Current time is: {now}")
    print(f"Future date is: {future}")


def show_gbv_data():

    people = 150
    people_affected = people *25 /100
    print(people_affected)
    print(round(people_affected))

def calc_tax():
    items =  [24,30,50]
    for each in items:
        print(each)
        sum = each * 0.15
        print(sum)
    if sum >10:
        print("Tax exceeds 10")
    if sum == 5 :
        print("Tax is within limit")
    else: 
        print("tax too low")
hello()
show_gbv_data()
show_date()

