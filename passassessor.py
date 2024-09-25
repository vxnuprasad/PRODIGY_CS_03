import re
import getpass

# Banner for the program
banner = """

╭━━━╮╱╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱╱╱╱┃╭━╮┃
┃╰━╯┣━━┳━━┳━━┫┃╱┃┣━━┳━━┳━━┳━━┳━━┳━━┳━╮
┃╭━━┫╭╮┃━━┫━━┫╰━╯┃━━┫━━┫┃━┫━━┫━━┫╭╮┃╭╯
┃┃╱╱┃╭╮┣━━┣━━┃╭━╮┣━━┣━━┃┃━╋━━┣━━┃╰╯┃┃
╰╯╱╱╰╯╰┻━━┻━━┻╯╱╰┻━━┻━━┻━━┻━━┻━━┻━━┻╯
"""
print(banner)
print("--- Password Strength Assessment Tool By Techno-rabit ---")

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count how many criteria are met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_char_criteria])

    # Determine strength level based on criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = {
        "length": length_criteria,
        "upper": upper_criteria,
        "lower": lower_criteria,
        "number": number_criteria,
        "special": special_char_criteria,
    }

    return strength, feedback


def main():
    password = getpass.getpass("Enter a password to assess its strength: ")

    view_password = input("\nDo you want to view the entered password? (yes/no): ").strip().lower()
    if view_password in ['yes', 'y']:
        print(f"\nYour entered password is: {password}")

    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}\n") 
    print("Criteria Met:\n")
    print(f"  Length (≥ 8): {'✔' if feedback['length'] else '✘'}\n")
    print(f"  Uppercase Letter: {'✔' if feedback['upper'] else '✘'}\n")
    print(f"  Lowercase Letter: {'✔' if feedback['lower'] else '✘'}\n")
    print(f"  Number: {'✔' if feedback['number'] else '✘'}\n")
    print(f"  Special Character: {'✔' if feedback['special'] else '✘'}\n")


if __name__ == "__main__":
    main()
