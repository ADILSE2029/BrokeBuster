import os


class BrokeBuster:
    def __init__(self):
        self.filename = "brokebuster.txt"

    def add_expense(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("")
            print("No Data Storage File was found,Created Data Storage File.")
            return
        with open(self.filename, "r") as f:
            fetched_data = f.readlines()

        given_category = input("Write Category:").strip()
        decorator(60)

        found = False
        for i, data in enumerate(fetched_data):
            broked_data = data.strip().split('|')
            category_name = broked_data[0].strip()
            category_spendings = int(broked_data[1])
            if category_name == given_category:
                found = True
                given_expense = int(input("Write Expense:"))
                category_spendings += given_expense
                fetched_data[i] = f"{category_name}|{category_spendings}\n"
                print(
                    f"{category_spendings}$ Added  to category {category_name}\n")
        if not found:
            print("No Category Found\nuse main menu to add category")
            decorator(60)
        with open(self.filename, "w") as f:
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
                    data_broked = data.strip().split('|')
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
