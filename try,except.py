def get_password() :
    try :
        user_password = int(input("enter your password :"))
        if user_password == 270508 :
            print("you have been given access bro")
        else :
            print("we are really sorry, access denied")
    except ValueError :
        print("error, enter a valid number")
    except Exception as g :
        print("an error has occurred")

get_password()


# creating a converter that can convert degree to farenheit
import math
def converting_degree_to_farenheit(degree) :
    return (degree * 9/5)+32
degree = float(input("enter the value of the degree :"))
if degree >= 0 :
    farenheit = converting_degree_to_farenheit(degree)
    print(f"the value of farenheit {degree} is : {farenheit:2f}")
elif degree < 0 :
    farenheit = converting_degree_to_farenheit(degree)
    print(f"the value of farenheit {degree} is : {farenheit:2f}")
else :
    print("invalid input")