
import module1 as m1


def main():
    classed = m1.BrokeBuster()
    while True:
        m1.decorator(60)
        try:
            user_choice = input(
                "[A] Add Expense\n[M] Manage Category\n[R] Reset\n[E] Exit\n\nChoice:").lower()
            if user_choice == "a":
                m1.decorator(60)
                classed.add_expense()
            elif user_choice == "m":
                m1.decorator(60)

                user_choice = input(
                    "[A] Add Category\n[V] View Current Categories\n\nChoice:").lower()
                if user_choice == "a":
                    classed.add_category()
                elif user_choice == "v":
                    classed.view_category()
                else:
                    print("Invalid Input")

            elif user_choice == "r":
                m1.decorator(60)
                classed.reset()
            elif user_choice == "e":
                m1.decorator(60)
                print("Thanks for using")
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
            print("Hello")


if __name__ == "__main__":
    main()
