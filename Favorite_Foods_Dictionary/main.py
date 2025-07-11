from pathlib import Path

# Favorite Foods Dictionary
'''
Build a dictionary where each key is a person's name and the value is a list
of their favorite foods.
- Create a dictionary with at least 3 people and their favorite food
- Write a function show_favorites(people_foods) that neatly prints out
each person's name and their favorite foods
'''

def show_favorites(people_foods):
    print("\n-- Favorite Foods Summary --")
    for full_name, foods in people_foods.items():
        print(f"{full_name}: {', '.join(foods)}")

# all_users is renamed from people_foods dictionary
def get_new_userinfo(all_users):
    favorite_foods = []

    first_name = input("What is your first name: ").title()
    last_name = input("What is your last name: ").title()
    full_name = f"{first_name} {last_name}"
    
    print(f"\nHi {full_name}! Please enter your three favorite foods.")

    while len(favorite_foods) < 3:
        food_choice = input(f"Favorite food #{len(favorite_foods)+1}: ")
        food_choice = food_choice.title()
        if food_choice:
            favorite_foods.append(food_choice)
        else:
            print("Please enter your favorite food: ")

    print(f"\nThanks {full_name}! Your favorite foods are: "\
    f"{', '.join(favorite_foods)}.\n")

    # Store user info in directory.
    # full_name is the key, favorite foods is the value stored as a list
    all_users[full_name] = favorite_foods

# Main Program

print('''Welcome to MyFoods Central Kitchen

Enter your profile and provide your favorite foods and
we'll produce your foods with healthy, fresh ingredients
where you can pick-up from our location.\n''')

people_foods = {}

# Collect info for 3 users
for _ in range(3):
    get_new_userinfo(people_foods)

# Display results
show_favorites(people_foods)


