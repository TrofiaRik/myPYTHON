def computepay(hours, rate):
    if hours < 40:
        grosspay = hours * rate
        return grosspay
    elif hours > 40:
    # basic_pay = 40*frate
    # extra_hrs = fhrs - 40
    # extra_rate = frate*1.5
    # extra_pay = extra_hrs*extra_rate
    # grosspay = basic_pay+extra_pay
    #Other method:
        basic_pay = rate * hours
        extra_pay = (hours - 40)*(rate*0.5)
        grosspay = basic_pay+extra_pay
        return grosspay

hrs = input("Please, enter the hours woked this week: ")
rate = input("Please, enter the rate per hour: ")
try:
    fhrs = float(hrs)
    frate = float(rate)
except:
    print("Programma interrotto!")
    quit()

print("Your gross pay for this week is: ",computepay(fhrs,frate))
