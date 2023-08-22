from time import *
import random as r

def mistake(par, user):
    error=0
    for i in range(len(par)):
        try:
            if par[i]!= user[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay= time_e - time_s
    time_R = round(time_delay,2)
    speed= len(userinput)/ time_R
    return round(speed)

test =["Enroll in any course hand picked",
       " By your organization.",
       " These courses cover topics and skills your organization", 
       " Focused on improving."]
test1= r.choice(test)
print("****Typing Speed*****")
print(test1)
print()
print()
time_1 = time()
testinput= input("Enter: ")
time_2= time()

print("Speed: ", speed_time(time_1,time_2, testinput), "w/sec")
print("Error: ", mistake(test1, testinput))
