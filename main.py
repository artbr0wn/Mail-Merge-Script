#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



# # open starting letter and return it as a string
# with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as letter:
#     starting_letter = letter.read()
# #test starting_letter
# print(starting_letter)
#
#
# #open names and return as list
# with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as data:
#     names = data.readlines()
# #test list
# # print(names)
#
# #need a list of names without the "\n"
# #grabbed the total # of names
# name_count = len(names)
#
# #empty list for invited names
# invited_names_list = []
#
# #for loop to iterate through each name
# for x in names:
#     #random var to strip each name in loop of the "\n" value
#     test = x.strip()
#     invited_names_list.append(test)
# #testing to see if it works
# # print(invited_names_list)
#
#
# #return new list of names w/o the "\n" to add into the mail merge [name] category
# #another for loop to iterate through each name and add in new name
# for x in range(0,name_count):
#     #replacing [name] with invited name
#     ending_letter = starting_letter.replace("[name]", f"{invited_names_list[x]}")
#     #adding a var for each invited name, for the open funct
#     invited_name = invited_names_list[x]
#     #testing to see if it works
#     # print(ending_letter)
#     #now I need to add a new letter to the folder ready to send
#     with open(f"../Mail Merge Project Start/Output/ReadyToSend/{invited_names_list[x]}.txt", mode='w') as invited_name:
#         invited_name.write(ending_letter)



#instructors code

PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)


##

#so in essence instructor used a for loop within the with statement of the letter file, so whilst letter was opened
# it was able to be edited to iterate through each name in the list, drop the specific "\n" char then mail merge to line
# all within 9 lines lol... fuck the instructor bruh