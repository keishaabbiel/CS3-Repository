# 28 - RAMOS Keisha Abbiel B.
# 9 - Arayat

#Modifications: added loop, enhanced spacing, and invalid message for non-integer answers
#Tested on OnlineGDB

#Chinese Zodiac index
zodiac = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)"
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

#loop structure
while True:
    #when user inputs an integer
    try:
        birth_year = int(input("Enter your birth year : "))
        #when user inputs an invalid integer
        if birth_year < 1900:
            print("\n\tInvalid year, it should not be earlier than 1900.")
            print("\tPlease enter your birth year again.\n")
        #when user inputs a valid integer
        else:
            index = (birth_year - 1900) % 12
            print("\n \tYour Chinese Zodiac Sign is :", zodiac[index])
            break
    #when user inputs a non-integer
    except ValueError:
        print("\n\tInvalid input, please enter a number.\n")
  
