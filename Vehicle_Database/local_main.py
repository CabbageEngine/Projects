# Simple Vehicle Profile Manager - local version

# Dictionary to store all vehicle profiles using license plates as keys
vehicle_profiles = {}

def make_vehicle(manufacturer, model, plate, **options):
    vehicle = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        'plate': plate.upper(),
    }

    for key, value in options.items():
        vehicle[key] = value
    return vehicle

def collect_vehicle_options():
    options = {}
    print("\nEnter additional vehicle details (optional). Type 'q' to stop.")
    while True:
        key = input("Field name (e.g., color, year): ").strip()
        if key.lower() in ('q', 'quit'):
            break
        value = input(f"Enter value for '{key}': ").strip()
        options[key] = value
    return options

def display_all_profiles():
    if not vehicle_profiles:
        print("\nNo vehicle profiles saved.\n")
        return
    print(f"\nSaved Vehicle Profiles ({len(vehicle_profiles)} total):")
    for plate, profile in vehicle_profiles.items():
        print(f"\nLicense Plate: {plate}")
        for key, value in profile.items():
            print(f" {key.title()}: {value}")
    print()

def modify_vehicle_profile():
    plate = input("Enter license plate number to look up: ").strip().upper()
    if plate not in vehicle_profiles:
        print("Vehicle with that plate not found.\n")
        return

    vehicle = vehicle_profiles[plate]
    print("\nVehicle found:")
    for key, value in vehicle.items():
        print(f" {key.title()}: {value}")

    print("\nEnter field you want to update (or type 'q' to quit):")
    while True:
        field = input("Field name: ").strip().lower()
        if field == 'q':
            break
        if field not in vehicle:
            print("That field does not exist. You can still add it.")
        new_value = input(f"Enter new value for '{field}': ").strip()
        vehicle[field] = new_value
        print(f"{field.title()} updated to {new_value}.\n")

def clear_profiles():
    vehicle_profiles.clear()
    print("All vehicle profiles have been cleared.\n")

# Main Menu Loop
def main():
    while True:
        print("""
Vehicle Profile Manager (Local)
-------------------------------
1. Add new vehicle profile
2. View all saved vehicle profiles
3. View / Modify a vehicle profile
4. Clear all saved vehicle profiles
5. Quit Program
""")
        choice = input("Choose an option (1 to 5): ").strip()

        if choice == '1':
            make = input("Enter manufacturer: ").strip()
            model = input("Enter model: ").strip()
            plate = input("Enter license plate: ").strip().upper()

            if plate in vehicle_profiles:
                print("A vehicle with this plate already exists.\n")
                continue

            options = collect_vehicle_options()
            profile = make_vehicle(make, model, plate, **options)
            vehicle_profiles[plate] = profile
            print("Vehicle profile saved successfully!\n")

        elif choice == '2':
            display_all_profiles()

        elif choice == '3':
            modify_vehicle_profile()

        elif choice == '4':
            confirm = input("Are you sure you want to clear all profiles? (y/n):")
            if confirm.lower() in ('y', 'yes'):
                clear_profiles()

        elif choice == '5':
            print("Thank you for using the Vehicle Profile Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-5.\n")

if __name__ == "__main__":
    main()
