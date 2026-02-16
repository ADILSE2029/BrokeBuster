class brokebuster:
    def add_expense(self):

        with open("brokebuster.txt", "r") as f:
            checker = f.read()
            if not checker:
                decorator(60)
                print("No Category Found,Add Category using main menu")
            else:
                given_expense = int(input("Write Expense:"))
                given_category = input("Write Category:")
                f.seek(0)
                fetched_data = f.readlines()
                for i, data in enumerate(fetched_data):
                    broked_data = data.strip().split('|')
                    category_name = broked_data[0]
                    category_spendings = int(broked_data[1])
                    if category_name == given_category:
                        category_spendings += given_expense
                        fetched_data[i] = f"{category_name}|{category_spendings}\n"
                        print(
                            f"Expense Added. New Expense for category {category_name} : {category_spendings}\n")

                with open("brokebuster.txt", "w") as f:
                    f.writelines(fetched_data)

    def add_category(self):
        decorator(60)
        given_new_category = input("Write Name of Category:")
        with open("brokebuster.txt", "a") as f:
            f.write(given_new_category+"|"+"0\n")
            print("Category Added")

    def view_category(self):
        with open("brokebuster.txt", "r") as f:
            checker = f.read()
            if not checker:
                decorator(60)
                print("No Category Found,Hence no Data,Use main menu to add category")
            else:
                f.seek(0)
                fetched_data = f.readlines()
                category_name = "Name"
                category_price = "Spendings"
                print(f"{category_name:<30}{category_price}")
                for data in fetched_data:
                    data_broked = fetched_data[0].strip().split('|')
                    category_name = data_broked[0]
                    category_saved_amount = data_broked[1]
                    decorator(60)
                    print(f"{category_name:<30}{category_saved_amount}")

    def reset(self):
        with open("brokebuster.txt", "w") as f:
            f.write("")
            print("Reset Successfull")


def decorator(value):
    print("="*value)
