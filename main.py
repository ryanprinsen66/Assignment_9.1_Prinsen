#Assignment 9.1 Prinsen
#Importing os directories
import os

#Prompt user for name of directory
directory = input("Please enter the directory where to save the file. ")

#Validate the directory entered does exist
if os.path.isdir(directory):

  #Prompt user for file name and file contents
  file = input("Please enter the file name. ")
  name = 'Name: '+input("What is your name. ")
  address = ' Address: '+input("What is your address. ")
  phone_number = ' Phone: '+input("What is your phone number. ")

  #Create the file name based on user input
  create_file = open(os.path.join(directory,file), 'w')
  #Add the contents to the file
  create_file.write(f"{name},{address},{phone_number}\n")
  #Close the file
  create_file.close()

  #Display the file info and contents for verification
  print(f"\nFile Name: {file}. \nFile Contents: ")
  created_file = open(os.path.join(directory,file), 'r')
  for line in created_file:
    print(f"{line}")
    
#Response if directory does not exist
else:
  print("You have entered an invalid directory. ")



  
