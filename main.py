
import module1 as m1

    ## main area
def main():

    functions= m1.BrokeBuster()

    functions.decorator()
    print("\t BROKE BUSTER \t")
    

    while True:
        try:

            functions.decorator()
            user_choice = input(
                "[A] Add Expense\n[M] Manage Category\n[R] Reset\n[E] Exit\n\nChoice:").lower()
            

            if user_choice == "a":
                functions.add_expense()
            elif user_choice == "m":

                functions.decorator()
                user_choice = input(
                    "[A] Add Category\n[V] View Current Categories\n[R] Remove Category\n\nChoice:").lower()
                if user_choice == "a":
                    functions.add_category()
                elif user_choice == "v":
                    functions.view_category()
                elif user_choice == "r":
                    functions.remove_category()
                else:
                    functions.decorator()
                    print("Invalid Input")


            elif user_choice == "r":
                
                functions.reset()
            elif user_choice == "e":
                functions.decorator()
                print("Thanks for using")
                break
            else:
                functions.decorator()
                print("Invalid Input")


        except ValueError:
            functions.decorator()
            print("Invalid Input")
            


if __name__ == "__main__":
    main()
