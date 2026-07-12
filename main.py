from generator import generate_password
from history import save_history, view_history
import checker

def strength_bar(score):
    percent = score * 10
    filled = "█" * score
    empty = "░" * (10 - score)

    return f"{filled}{empty}  {percent}%"

def main():
    while True:
        print("\n==============================")
        print(" PASSWORD SECURITY TOOLKIT")
        print("==============================")
        print("1. Check Password")
        print("2. Generate Password")
        print("3. View History")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            password = input("Enter password: ")

            result = checker.check_password(password)

            score, strength, suggestions, entropy = result

            print("\n" + "=" * 40)
            print("PASSWORD ANALYSIS")
            print("=" * 40)

            print(f"Score       : {score}/10")
            print(f"Strength    : {strength}")
            print(f"Entropy     : {entropy} bits")

            print("\nStrength Meter")
            print(strength_bar(score))
            if suggestions:
                print("\nSuggestions:")
                for suggestion in suggestions:
                    print("-", suggestion)
            else:
                print("\nExcellent password!")

            save_history(password, score, strength)

        elif choice == "2":
            try:
                length = int(input("Password length: "))

                if length < 8:
                    print("Length must be at least 8.")
                    continue

                password = generate_password(length)

                print("\nGenerated Password:")
                print(password)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            view_history()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()