import os


class BrokeBuster:
    ## file name check
    def __init__(self):
        self.filename = "brokebuster.txt"

    ### adding mechanism
    def add_expense(self):
        self.decorator()

            #### scene 1 - no file exist to add expense to 
        if not os.path.exists(self.filename):
            self.decorator()
            print("No file was found,Created new storage file.")
            with open(self.filename, "w") as f:
                f.write("")
            return
        

            #### scene 2 - file exist
        with open(self.filename, "r") as f:
            fetched_data = f.readlines()


        
        given_category = input("Select Category:").strip().upper()
        if given_category.isalpha()== True:
            pass
        else:
            self.decorator()
            print("Invalid name, must be letters only")
            return
        
        found=False
        for index_value,actual_data in enumerate(fetched_data):
            broked_data = actual_data.strip().split('|')
            category_name = broked_data[0].strip()
            category_spendings = int(broked_data[1])
            if category_name == given_category:
                given_expense = int(input("Add Expense:"))
                category_spendings += given_expense
                fetched_data[index_value] = f"{category_name}|{category_spendings}\n"
                self.decorator()
                print(
                    f"{given_expense}$ Added  to category {category_name}\n")
                found=True
                

        if found == False:
            self.decorator()
            print("No Category Found\nUse manage category option to add category")
            return
            

        with open(self.filename, "w") as f:
            f.writelines(fetched_data)

    ### adding category mechanism 
    def add_category(self):
        self.decorator()

           ## scene 1 - storage file does not exist
        if not os.path.exists(self.filename):
            self.decorator()
            print("No file was found,Created new storage file.")
            with open(self.filename, "w") as f:
                f.write("")
            return
        
        
           ## scene 2 - file exist 
        with open(self.filename, "r") as f:
            fetched_data = f.readlines()

        
        given_new_category = input("Write Name of Category:").strip().upper()
        if not given_new_category.isalpha():
            self.decorator()
            print("Invalid name, must be letters only")
            return
        else:
            pass
            
        
            
        for index_value, actual_data in enumerate(fetched_data):
            broked_data =  actual_data.strip().split('|')
            category_name = broked_data[0].strip()
            if category_name == given_new_category:
                self.decorator()
                print("Category already exist, try using different name")
                return
            else:
                pass
        print("Category added")      ## cannot be used inside loop bcz it keep printing on very iteration.
            
        with open(self.filename,"a") as f:
                    f.write(given_new_category+"|"+"0\n")

       
       ## view category mechanism
    def view_category(self):
        self.decorator()
         
          ##scene 1 - file does not exist
        if not os.path.exists(self.filename):
            self.decorator()
            print("No file was found,Created new storage file.")
            with open(self.filename, "w") as f:
                f.write("")
            return
          ## scene 2 - file exist
        with open(self.filename, "r") as f:
            fetched_data = f.readlines()

            if not fetched_data:
                self.decorator()
                print("No Category Found\nUse manage category option to add")
                return

            category_name = "Name"
            category_price = "Spendings"
            print(f"{category_name:<30}{category_price}")
            for data in fetched_data:
                data_broked = data.strip().split('|')
                category_name = data_broked[0]
                category_saved_amount = data_broked[1]
                print(f"{category_name:<30}{category_saved_amount}")
        

        ## removing category mechanism
    def remove_category(self):
        self.decorator()

        ##scene 1 - file does not exist
        if not os.path.exists(self.filename):
            self.decorator()
            print("No file was found,Created new storage file.")
            with open(self.filename, "w") as f:
                f.write("")
            return
        
          ## scene 2 - file exist
        
        given_category = input("Write category:").strip().upper()
        if not given_category.isalpha():
            self.decorator()
            print("Invalid name, must be letters only")
            return
        else:
            pass
            
        

        with open(self.filename, "r") as f:
            fetched_data = f.readlines()
        if not fetched_data:
            self.decorator()
            print("No Category Found to remove")
            return
        
        found=False
        list_data=[]
        for data in fetched_data:
            if data.startswith(given_category):
                found=True
            else:
                list_data.append(data)

        if found==True:
            self.decorator()
            print(f"Category removed: {given_category}")


        with open(self.filename, "w") as f:
            f.writelines(list_data)
    
        ## decoration purposes 
    def decorator(self):
        print("="*40)


        ##reset mechanism
    def reset(self):
        self.decorator()
        with open(self.filename, "w") as f:
            f.write("")
        print("Reset Successfull")


