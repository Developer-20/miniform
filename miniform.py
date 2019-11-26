profile = {
    "dev": ["developer","d20"],
    "faith": ["f8","faith8"],
    "emmanuel":["emmy","ehm33"]
}
#the code below asks for the user's name
my_name = input("Enter your name: ")

#the if statement checks if the user's name input is in the dictionary above
if my_name in profile:

	#the code above checked if the user name is in the dictionary and if its found to be true, this code below asks the user to input his username
    username = input("Enter your username: ")

    #this code below then checks if the username is correct from the dictionary
    if username == profile[my_name][0]:

    	#the code below then generates the password and the complete details of the datan in the dictionary
    	password = profile[my_name][1]
    	print(f"Here are your details \nUsername: {username} \nPassword: {password}")
else :
	print("Your username isnt on our database")


input()