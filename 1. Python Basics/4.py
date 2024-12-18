#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

globe="Global Variables"
def myfun():
    loc="Local Variables"
    print(loc)
print(globe)
myfun()
#print(loc) --> Cannot access