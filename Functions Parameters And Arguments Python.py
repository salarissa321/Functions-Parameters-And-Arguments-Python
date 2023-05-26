



#------------------------------------------------------------------
#-------- Functions Parameters And Arguments----------
#------------------------------------------------------------------



# # def With One Parameter

a , b , c = "Salar" , "Raman" , "Gamel"

print(f"Hello {a}") # Hello Salar
print(f"Hello {b}") # Hello Raman
print(f"Hello {c}") # Hello Gamel


# def                        =>                      Function Keyword[Define]
# say_hello                  =>                       Function Name
# name                       =>                       Parameters
# print(f"Hallo {name}")     =>                       Task
# say_hello("Salar")         =>                      Salar is The Argument


def say_hello(name) :
    print(f"Hallo {name}")

say_hello("Salar") # Hallo Salar
say_hello(a) # Hallo Salar
say_hello(b) # Hallo Raman
say_hello(c) # Hallo Gamel


print("." * 90) # ..........................................................................................

# Def With Two Parameters

def addition(n1 , n2) :
    print(n1 + n2)

addition(100,300) # 400
addition(-90,300) # 210

print("#" * 50) # ##################################################


def addition(n1 , n2) :
    # print(n1 + n2)
    if type(n1) != int or type(n2) != int :
        print("Only Interges Allowed")
    
    else :
        print(n1 + n2) # 
 

addition(100,300) # 400
addition("100","Salar") # Only Interges Allowed
addition(100,500) # 600

print("#" * 50) # ##################################################


def full_name(first, middle , last) :
    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")
full_name("Salar" , "Issa" , "Gamel") # Hello Salar I Gamel
    



