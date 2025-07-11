import json
from pathlib import Path
from functions import *

# Create subdirectory for storing car profile data
DATA_FILE = Path("vehicle_data/vehicle_profiles.json")

# Check to verify folder exists, verify file integrity, then save vehicle
    # profile data to file
def save_vehicle_to_file(vehicle, filename=DATA_FILE):
    filename.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if filename.exists():
        try:
            with open(filename, "r", encoding='utf-8') as file:
                existing = json.load(file)
        except json.decoder.JSONDecodeError:
            print("Warning: Existing file was empty or invalid, starting fresh.")
        
    existing.append(vehicle)
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(existing, file, indent=4)

# Load vehicle profile data from file. Verify file existence and integrity
def load_vehicle_profiles(filename=DATA_FILE):
    if filename.exists():
        try:
            with open(filename, "r", encoding='utf-8') as file:
                return json.load(file)
        except json.decoder.json.JSONDecodeError:
            return []
    return []

# Create a dictionary with attributes of vehicle 
def make_vehicle(manufacturer, model, plate, **options):
    vehicle_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        'plate': plate.title(),
        }
    for option, value in options.items():
        vehicle_dict[option] = value
    return vehicle_dict

# Add any additional options to vehicle attributes
def collect_vehicle_options():
    options = {}
    print("\nEnter vehicle details (optional). Type 'q' to stop.")
    
    while True:
        while True:
            typeMenu()
 
            try:
                vehicle_type = input("\nEnter vehicle type: ")
                if vehicle_type == '1':
                    vehicle_type = "Vehicle Type: "
                    value = "car"
                    print(f"You've selected a {value} as your vehicle type.\n")
                    options[vehicle_type] = value
                    break
                elif vehicle_type == '2':
                    vehicle_type = "Vehicle Type: "
                    value = "pick-up truck"
                    print(f"You've selected a {value} as your vehicle type.\n")
                    options[vehicle_type] = value
                    break
                elif vehicle_type == '3':
                    vehicle_type = "Vehicle Type: "
                    value = "sports-utility vehicle"
                    print(f"You've selected a {value} as your vehicle type.\n")
                    options[vehicle_type] = value
                    break
                elif vehicle_type == '4':
                    vehicle_type = "Vehicle Type: "
                    value = "van"
                    print(f"You've selected a {value} as your vehicle type.\n")
                    options[vehicle_type] = value
                    break
                elif vehicle_type == '5':
                    vehicle_type = "Vehicle Type: "
                    value = "box truck"
                    print(f"You've selected a {value} as your vehicle type.\n")
                    options[vehicle_type] = value
                    break
                elif vehicle_type == '6':
                    vehicle_type = "Vehicle Type: "
                    value = "flatbed truck"
                    print(f"You've selected a {value} as your vehicle type.\n")
                    options[vehicle_type] = value
                    break
                elif vehicle_type == '7':
                    vehicle_type = "Vehicle Type: "
                    value = "heavy truck"
                    print(f"You've selected a {value} as your vehicle type.\n")
                    options[vehicle_type] = value
                    break
                elif vehicle_type == '8':
                    break
                else:
                    print("That is not a valid number. Try again.")
                    continue
            except ValueError:
                print(f"That is not a valid number. Try again.")
     
        while True:       
            vehicle_color = "Vehicle Color: "
            value = input(f"{vehicle_color}: ").strip()
            if value.lower() in ('q', 'quit'):
                break
            else:
                if value.isdigit():
                    print("Sorry, that is not a valid entry")
                    continue
                else:
                    print(f"Your vehicle color is {value}")
                    options[vehicle_color] = value
                    break
        
        return options

# Show all stored vehicle profiles
def display_all_profiles():
    vehicles = load_vehicle_profiles()
    if not vehicles:
        print("No vehicle profiles saved.\n")
        return
    
    print(f"\nSaved Car Profiles ({len(vehicles)} total):")
    for i, vehicle in enumerate(vehicles, start=1):
        print(f"\nVehicle {i}:")
        for key, value in vehicle.items():
            print(f"  {key.title()}: {value}")
    print("\n")

# Retrieve from license plate data to view / modify single vehicle profile
def modify_vehicle_profile():
    vehicles = load_vehicle_profiles()
    if not vehicles:
        print("No vehicle profiles available.\n")
        return

    lookup_plate = input("Enter license plate number to lookup vehicle profile: ")

    for vehicle in vehicles:
        if vehicle.get('plate') == lookup_plate:
            print("\nVehicle found: ")
            for key, value in vehicle.items():
                print(f"{key.title()}: {value}")

            print("\nWhich field would you like to update? " +
                  "(or type 'q' to quit)")
            while True:
                field = input("Field name: ").strip().lower()
                if field == 'q':
                    break
                if field not in vehicle:
                    print("That field does not exist. Try again.")
                    continue
                new_value = input(f"Enter new value for {field}: ").strip()
                vehicle[field] = new_value
                print(f"{field.title()} updated to {new_value}.\n")

            with open(DATA_FILE, "w", encoding='utf-8') as file:
                json.dump(vehicles, file, indent=4)
            print("Vehicle profile updated.\n")
            return

    print("Vehicle with that plate number not found.\n")

# Delete all vehicle profiles on record
def clear_profiles(filename=DATA_FILE):
    if filename.exists():
        filename.unlink()
        print("All vehicle profiles have been deleted.\n")
    else:
        print("No vehicle profile file exists to delete.\n")

# Main Menu Loop
def main():
    while True:
        print("""
Vehicle Profile Manager
-----------------------
1. Add a new vehicle profile
2. View all saved vehicle profiles
3. View / Modify single vehicle profile
4. Clear all saved vehicle profiles
5. Quit
""")
        # Menu choices
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            make = input("Enter manufacturer: ").strip()
            model = input("Enter model: ").strip()
            plate = input("Enter license plate: ").strip().upper()

            extra_options = collect_vehicle_options()
            vehicle_profile = make_vehicle(make, model, plate, **extra_options)

            save_vehicle_to_file(vehicle_profile)
            print("Vehicle profile saved successfullly!\n")

        elif choice == '2':
            display_all_profiles()

        elif choice == '3':
            modify_vehicle_profile()

        elif choice == '4':
            confirm = input("Are you sure? This will erase all saved " +
                            "vehicle profiles (y/n): ")
            if confirm.lower() in ('y', 'yes'):
                clear_profiles()

        elif choice == '5':
            print("Thank You for Using the Vehicle Profile Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-5.\n")


if __name__ == "__main__":
    main()