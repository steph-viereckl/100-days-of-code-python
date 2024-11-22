#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Open starting letter and store in variable
with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    invite_letter = starting_letter.read()

# Get list of names and create letter for each
with open("Input/Names/invited_names.txt", mode="r") as name_file:

    for name in name_file.readlines():

        updated_name = name.strip()

        # Create new letter
        with open(f"Output/ReadyToSend/letter_for_{updated_name}.txt", mode="w") as new_letter:

            new_letter.write(invite_letter.replace("[name]", updated_name))

