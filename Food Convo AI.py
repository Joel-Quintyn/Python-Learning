"""
SYNOPSIS: A Program Of How I Thought AI Worked, Written Using My Python Knowledge At That Time.
"""


class food:

    def __init__(self, meal_type):
        self.meal_type = meal_type
        self.item = ['Chicken']
        self.food_count = 0

    def add_item(self):
        fitem = str(input("\nWhat's For {}?\nResponse: ".format(self.meal_type.capitalize())))
        self.item.append(fitem)

    def list_items(self):
        print(f'Your {self.meal_type} Items Are:')
        for self.i in self.item:
            print('*' + self.i)


mealtype = str(input("What Are You Having Now? Breakfast, Lunch or Dinner\nResponse: ")).lower().split()

for i, word in enumerate(mealtype):
    if word == 'breakfast':
        print("\nYou'll Be Having Breakfast!!!")
        breakfast = food(word)
        breakfast.add_item()
        breakfast.list_items()
        break
    elif word == 'lunch':
        print("\nYou'll Be Having Lunch!!!")
        lunch = food(word)
        lunch.add_item()
        lunch.list_items()
        break
    elif word == 'dinner':
        print("\nYou'll Be Having Dinner!!!")
        dinner = food(word)
        dinner.add_item()
        dinner.list_items()
        break
    elif word not in mealtype:
        print("Sorry Not A Command")
        break
