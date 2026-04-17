
import module1 as m1

    ## main area
def main():

    brokebuster= m1.BrokeBuster()

    brokebuster.decorator()
    print("\t BROKE BUSTER \t")
    

    while True:
        try:

            brokebuster.decorator()
            user_choice = input(
                "[A] Add Expense\n[M] Manage Category\n[R] Reset\n[E] Exit\n\nChoice:").lower()
            

            if user_choice == "a":
                brokebuster.add_expense()
            elif user_choice == "m":

                brokebuster.decorator()
                user_choice = input(
                    "[A] Add Category\n[V] View Current Categories\n[R] Remove Category\n\nChoice:").lower()
                if user_choice == "a":
                    brokebuster.add_category()
                elif user_choice == "v":
                    brokebuster.view_category()
                elif user_choice == "r":
                    brokebuster.remove_category()
                else:
                    brokebuster.decorator()
                    print("Invalid Input")


            elif user_choice == "r":
                
                brokebuster.reset()
            elif user_choice == "e":
                brokebuster.decorator()
                print("Thanks for using")
                break
            else:
                brokebuster.decorator()
                print("Invalid Input")


        except ValueError:
            brokebuster.decorator()
            print("Invalid Input")
            


if __name__ == "__main__":
    main()
