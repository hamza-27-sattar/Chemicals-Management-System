import json
import matplotlib.pyplot as plt

class Chemical:
    def __init__(self,name,chemical_id,category,quantity,unit, expiry_date):
        self.name = name
        self.chemical_id = chemical_id
        self.category = category
        self.quantity = quantity
        self.unit = unit
        self.expiry_date = expiry_date
    def display(self):
        print(f'''
    +--------------------------------+
    | Chem. Name: {self.name}
    | ID:         {self.chemical_id}
    | Category:   {self.category}
    | Quantity:   {self.quantity} {self.unit}
    | Exp. Date:  {self.expiry_date}
    +--------------------------------+
        ''')        

chemical1 = Chemical("Hydrochloric Acid","001","Acid",500,"mL","01-2027")
chemical2 = Chemical("Ethanol","002","Solvent",1000,"mL","02-2027")
chemical3 = Chemical("Citric Acid","003","Acid",200,"mL","03-2027")


class Inventory:
    def __init__(self):
        self.chemicals = []

    def add_chemical(self, chemical):
        self.chemicals.append(chemical)

    def display_all(self):
        for chemical in self.chemicals:
            chemical.display()

    def find_chemical(self, chemical_id):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                chemical.display()
                break
        else:
            print("Chemical Not Found")
    def update_quantity(self, chemical_id, new_quantity):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                chemical.quantity = new_quantity
                print("Quantity Updated")
                break
        else:
            print("Chemical Not Found")
    def remove_chemical(self,chemical_id):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                self.chemicals.remove(chemical)
                print("Chemical Removed!")
                break
        else:
            print("Could not find Chemical")
    def find_by_name(self, name):
        for chemical in self.chemicals:
            if chemical.name.lower() == name.lower():
                chemical.display()
                break
        else:
            print("Chemical Not Found")
    def update_category(self, chemical_id, new_category):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                chemical.category = new_category
                print("Category Updated")
                break
        else:
            print("Chemical Not Found")

    def save(self):
        data = []
        for chemical in self.chemicals:
            data.append({
                "Name": chemical.name,
                "Chemical ID": chemical.chemical_id,
                "Category": chemical.category,
                "Quantity": chemical.quantity,
                "Unit": chemical.unit,
                "Expiry Date": chemical.expiry_date
            })
        with open("chemicals.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory Saved!")

    def load(self):
        try:
            with open("chemicals.json", "r") as file:
                data = json.load(file)

            for item in data:
                chemical = Chemical(
                item["Name"],
                item["Chemical ID"],
                item["Category"],
                item["Quantity"],
                item["Unit"],
                item["Expiry Date"]
            )

                self.chemicals.append(chemical)

            print("Inventory Loaded!")

        except FileNotFoundError:
            print("No saved inventory found.")
    def view_analytics(self):
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        # -------------------------------
        # 1. Chemicals by Category
        # -------------------------------
        category_counts = {}

        for chemical in self.chemicals:
            category = chemical.category

            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1

        categories = list(category_counts.keys())
        category_values = list(category_counts.values())

        axes[0, 0].bar(categories, category_values)
        axes[0, 0].set_title("Chemicals by Category")
        axes[0, 0].set_xlabel("Category")
        axes[0, 0].set_ylabel("Number of Chemicals")

        # -------------------------------
        # 2. Chemicals by Unit
        # -------------------------------
        unit_counts = {}

        for chemical in self.chemicals:
            unit = chemical.unit

            if unit in unit_counts:
                unit_counts[unit] += 1
            else:
                unit_counts[unit] = 1

        units = list(unit_counts.keys())
        unit_values = list(unit_counts.values())

        axes[0, 1].pie(unit_values, labels=units, autopct="%1.1f%%")
        axes[0, 1].set_title("Chemicals by Unit")


        # -------------------------------
        # 3. Expiry Overview
        # -------------------------------
        expiry_dates = []
        expiry_names = []

        for chemical in self.chemicals:
            expiry_names.append(chemical.name)
            expiry_dates.append(chemical.expiry_date)

        axes[1, 0].bar(expiry_names, range(len(expiry_dates)))
        axes[1, 0].set_title("Expiry Date Overview")
        axes[1, 0].set_xlabel("Chemical")
        axes[1, 0].set_ylabel("Expiry Entry")
        axes[1, 0].tick_params(axis="x", rotation=45)


        # -------------------------------
        # 4. Total Chemicals
        # -------------------------------
        total_chemicals = len(self.chemicals)

        axes[1, 1].bar(["Total Chemicals"], [total_chemicals])
        axes[1, 1].set_title("Total Chemicals in Inventory")
        axes[1, 1].set_ylabel("Number of Chemicals")


        plt.tight_layout()
        plt.show()
    

inventory = Inventory()
inventory.load()

#def menu():
while True:
        print('''
        +===================================+
        |   Chemical Management System      |
        |                                   |
        | 1. Add Chemical                   |
        | 2. Display all Chemicals          |
        | 3. Find Chemical (ID)             |
        | 4. Find Chemical (Name)           |
        | 5. Update Quantity                |
        | 6. Update Category                |
        | 7. Remove Chemical                |
        | 8. View Analytics                 |
        | 9. Save and Exit                  |       
        |                                   |
        +===================================+
        ''')

        
        choice = int(input("Enter choice: "))
        if choice == 1:
            name = input("Chemical name: ")
            chemical_id = input("Chemical ID: ")   
            category = input("Category: ")
            quantity = int(input("Quantity: "))
            unit = input("Unit: ")
            expiry_date = input("Expiry date: ")
            chemical = Chemical(name, chemical_id, category, quantity, unit, expiry_date)
            inventory.add_chemical(chemical)
            print("Chemical Added!")
        if choice == 2:
            inventory.display_all()
        if choice == 3:
            chemical_id = input("Enter Chemical ID: ")
            inventory.find_chemical(chemical_id)
        if choice == 4:
            name = input("Enter Chemical Name: ")
            inventory.find_by_name(name)
        if choice == 5:
            chemical_id = input("Enter Chemical ID: ")
            new_quantity = int(input("Enter New Quantity: "))
            inventory.update_quantity(chemical_id, new_quantity)
        if choice == 6:
            chemical_id = input("Enter Chemical ID: ")
            new_category = input("Enter New Category: ")
            inventory.update_category(chemical_id, new_category)
        if choice == 7:
            chemical_id = input("Enter Chemical ID: ")
            inventory.remove_chemical(chemical_id)
        if choice == 8:
            inventory.view_analytics()
        if choice == 9:
            inventory.save()
            print("Goodbye!")
            break



