import random

min = 1

max = 6
#Min and max arent even necessary but its a good first step 
roll_again = "yes" 
#First you have to define the variable





while roll_again == "yes":
    print("Rolling the dice... ")
    print("whats it gonna be? :)")
    print random.randint(min,max)
    roll_again = raw_input("Roll again?")
    #Then start the loop and print what you want to see Terminal 
    #Make sure to finish with  raw_input command to end the loop (Very important) and print your string. 

while roll_again == "no":
    print("Have a nice day!")
    break
#I added a another loop statement ending with a goodbye message, had to implement a break otherwise would continue infinitely.
