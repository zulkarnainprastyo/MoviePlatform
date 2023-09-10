class UserInterface:
    def __init__(self):
        self.user_id = None

    def display_menu(self):
        print("Main Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Exit")

    def get_user_input(self):
        return input("Enter your choice: ")

    def get_user_id(self):
        while True:
            try:
                user_id = int(input("Enter User ID: "))
                return user_id
            except ValueError:
                print("Invalid User ID. Please enter a valid integer.")

    def option_1(self):
        if self.user_id is not None:
            print(f"Option 1 selected for User ID {self.user_id}")
        else:
            print("Option 1 selected.")

    def option_2(self):
        if self.user_id is not None:
            print(f"Option 2 selected for User ID {self.user_id}")
        else:
            print("Option 2 selected.")

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_input()
            if choice == "1":
                self.option_1()
            elif choice == "2":
                self.option_2()
            elif choice == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def main(self):
        self.user_id = self.get_user_id()
        self.run()

if __name__ == "__main__":
    ui = UserInterface()
    ui.main()
