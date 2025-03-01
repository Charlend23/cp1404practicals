COLOUR_AND_CODE = {"amaranth": "#e52b50", "aliceblue": "#f0f8ff", "amber": "#ffbf00", "beige": "#f5f5dc",
                   "black": "#000000", "blueviolet": "#8a2be2", "canary": "#ffff99", "champagne": "#f7e7ce",
                   "white": "#ffffff", "wisteria": "#c9a0dc"}

def main():
    user_colour = get_input("Enter colour to get code: ")
    while user_colour != "":
        try:
            print(COLOUR_AND_CODE[user_colour])
        except KeyError:
            print("Invalid Colour")
        user_colour = get_input("Enter colour to get code: ")

def get_input(prompt):
        user_input = input(prompt).lower()
        return user_input

main()