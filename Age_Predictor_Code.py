
age = int(input("Enter your AGE:\n"))
# taking age

   present_year = int(input("Enter the Present Year:\n"))
# taking current year

# age nikalna, desired year main
       newage = int(input(
           "To know your age in desired YEAR,type the Year\nवांछित वर्ष में अपनी आयु जानने के लिए वह वर्ष टाइप करें:\n"))

           print("Your age in desired year will be:\n")

               print((int(newage) - int(present_year)) + int(age))

# year nikalna, desired age se
                   c = int(input(
                       "To know the year in which you will be of that age 🤔\n(Type The Desired Age to get the year)\nउस वर्ष को जानने के लिए जिसमें आप उस उम्र के होंगे\n"))

                       print("You Entered Age:", c)

                           print("In", c - age + present_year,
                                 "You Will Be Of that Age")

# 100 year wala code
                               hund = int(
                                   input("Press 1 to know when you'll be 100\n "))

                                    if (hund == 1):
                                        print("In", present_year - age + 100,
                                              "You Will Be Of 100 😂\nQuite Old🧐...RIGHT")

                                        else:
                                            print(
                                                "YOU ENTERED WRONG NUMBER :(\nRestart The Program")

# nice ending
                                           print("Thank You For Trying Our Program\nHave A Good Day\n:)\nRegards DEV😊")
