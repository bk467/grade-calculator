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

def score_needed():
    current = ask_number("\nYour current grade (%): ", 0, 100)
    exam_weight = ask_number("Weight of the exam (%): ", 1, 100)
    target = ask_number("Final grade you want (%): ", 0, 100)

    w = exam_weight / 100
    needed = (target - current * (1 - w)) / w #Formula to calculate grade, looked this up because I couldn't come up with it on my own

    if needed > 100:
        print("You would need", round(needed, 2), "%, which is not possible LOL you're cooked")
    elif needed <= 0:
        print("You already have", target, "% even with a 0 on the exam, you're chilling")
    else:
        print("You need", round(needed, 2), "% on the exam, you got this bro")

def gpa():
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0,
    } #using a hash map to attribute grade points to a letter grade instead of using a long if-else block

    print("\nEnter your courses. Leave the name blank when you're done.")
    total_credits = 0
    total_points = 0

    while True:
        name = input("Course name: ").strip()
        if name == "":
            break
        credits = ask_number("  Credit hours for " + name + ": ", 0.5, 10)

        while True:
            letter = input("  Letter grade for " + name + " (e.g. A, B+): ").strip().upper()
            if letter in grade_points:
                break
            print("  Please enter a valid letter grade like A, B+, or C-.")

        total_credits = total_credits + credits
        total_points = total_points + credits * grade_points[letter]

    if total_credits == 0:
        print("No courses entered.")
        return

    result = total_points / total_credits
    print("\nTotal credits:", total_credits)
    print("GPA:", round(result, 2))


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
            score_needed()
        elif choice == "3":
            gpa()
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