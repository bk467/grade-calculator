def ask_number(prompt, low, high):
    while True:
        text = input(prompt)
        try:
            number = float(text)
        except ValueError:
            print("Please enter a number.")
            continue

        if number < low or number > high:
            print("Please enter a number between", low, "and", high)
        else:
            return number


def course_grade():
    print("\nEnter your categories. Leave the name blank when you're done")
    total_weight = 0
    total_points = 0

    while True:
        name = input("Category name: ").strip()
        if name == "":
            break
        weight = ask_number("  Weight of " + name + " (%): ", 0, 100)
        score = ask_number("  Your score in " + name + " (out of 100): ", 0, 100)
        total_weight = total_weight + weight
        total_points = total_points + weight * score

    if total_weight == 0:
        print("No categories entered.")
        return

    if total_weight > 100:
        print("Your weights add up to more than 100%. Please check them.")
        return

    grade = total_points / total_weight
    print("\nWeight graded so far:", round(total_weight, 2), "%")
    print("Current grade:", round(grade, 2), "%")


def show_menu():
    print("\n## GRADE CALCULATOR ##")
    print("1. Current course grade")
    print("2. Score needed on an exam")
    print("3. GPA")
    print("4. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            course_grade()
        elif choice == "2":
            print("Score needed calculator coming soon.")
        elif choice == "3":
            print("GPA calculator coming soon.")
        elif choice == "4":
            print("See ya!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nSee ya!")