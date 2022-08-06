import os

directory = input("Please enter the directory where to save the file. ")
#file = input("Please enter the file name. ")

#name = input("What is your name. ")
#address = input("What is your address. ")
#phone_number = input("What is your phone number. ")

if os.path.isdir(directory):

  file = input("Please enter the file name. ")
  name = input("What is your name. ")
  address = input("What is your address. ")
  phone_number = input("What is your phone number. ")


  create_file = open(os.path.join(directory,file), 'w')
  create_file.write(f"{name},{address},{phone_number}\n")
  create_file.close()

  print("\nYou created the following file: ")
  created_file = open(os.path.join(directory,file), 'r')
  for line in created_file:
    print(f"\n{line}\n")
    print("\n")
    

else:
  print("You have entered an invalid directory. ")



  
