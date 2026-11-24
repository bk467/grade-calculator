def show_menu():
    print("\n=== Grade Calculator ===")
    print("1. Current course grade")
    print("2. Score needed on an exam")
    print("3. GPA")
    print("4. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            print("Course grade calculator coming soon.")
        elif choice == "2":
            print("Required score calculator coming soon.")
        elif choice == "3":
            print("GPA calculator coming soon.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    # Catch Ctrl+C / Ctrl+D so quitting early exits cleanly
    # instead of dumping a traceback on the user.
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")