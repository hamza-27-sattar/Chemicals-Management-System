#File Saving
import json
# Visual Results
import matplotlib.pyplot as plt

# 1st Class: Individual Chemical
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
        
# 2nd Class: Whole Inventory
class Inventory:
    def __init__(self):
        self.chemicals = []
# Loading the JSON file
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
# Add a chemical Option 1
    def add_chemical(self, chemical):
        self.chemicals.append(chemical)
# Display all chemicals Option 2
    def display_all(self):
        for chemical in self.chemicals:
            chemical.display()
# Find a chemical by ID Option 3
    def find_chemical(self, chemical_id):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                chemical.display()
                break
        else:
            print("Chemical Not Found")
# Find a chemical by name Option 4
    def find_by_name(self, name):
        for chemical in self.chemicals:
            if chemical.name.lower() == name.lower():
                chemical.display()
                break
        else:
            print("Chemical Not Found")
# Update quantity of a chemical Option 5
    def update_quantity(self, chemical_id, new_quantity):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                chemical.quantity = new_quantity
                print("Quantity Updated")
                break
        else:
            print("Chemical Not Found")
# Update category of a chemical Option 6
    def update_category(self, chemical_id, new_category):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                chemical.category = new_category
                print("Category Updated")
                break
        else:
            print("Chemical Not Found")
# Remove a chemical Option 7
    def remove_chemical(self,chemical_id):
        for chemical in self.chemicals:
            if chemical.chemical_id == chemical_id:
                self.chemicals.remove(chemical)
                print("Chemical Removed!")
                break
        else:
            print("Could not find Chemical")
# View Analytics Option 8
    def view_analytics(self):
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Professional color palette for charts
        palette = ['#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#f39c12']

        # 1. Chemicals by Category
        category_counts = {}
        for chemical in self.chemicals:
            category = chemical.category
            if category in category_counts:
                category_counts[category] += 1
            else:
                category_counts[category] = 1
        categories = list(category_counts.keys())
        category_values = list(category_counts.values())
        axes[0].bar(categories, category_values, color=palette[:len(categories)], edgecolor='black', alpha=0.85)
        axes[0].set_title("Chemicals by Category", fontsize=12, fontweight='bold')
        axes[0].set_xlabel("Category", fontsize=10)
        axes[0].set_ylabel("Number of Chemicals", fontsize=10)
        axes[0].grid(axis='y', linestyle='--', alpha=0.6)  
        # 2. Chemicals by Unit
        unit_counts = {}
        for chemical in self.chemicals:
            unit = chemical.unit
            if unit in unit_counts:
                unit_counts[unit] += 1
            else:
                unit_counts[unit] = 1
        units = list(unit_counts.keys())
        unit_values = list(unit_counts.values())
        axes[1].pie(
            unit_values, 
            labels=units, 
            autopct="%1.1f%%", 
            colors=palette[:len(units)], 
            startangle=140,
            wedgeprops={'edgecolor': 'black', 'linewidth': 0.8}
        )
        axes[1].set_title("Chemicals by Unit", fontsize=12, fontweight='bold')
        plt.tight_layout()
        plt.show()
# Saving all stored data before exiting menu Option 9
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

inventory = Inventory()
inventory.load()
# Main Menu (Looped)
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
        # Options within Main Menu
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
        elif choice == 2:
            inventory.display_all()
        elif choice == 3:
            chemical_id = input("Enter Chemical ID: ")
            inventory.find_chemical(chemical_id)
        elif choice == 4:
            name = input("Enter Chemical Name: ")
            inventory.find_by_name(name)
        elif choice == 5:
            chemical_id = input("Enter Chemical ID: ")
            new_quantity = int(input("Enter New Quantity: "))
            inventory.update_quantity(chemical_id, new_quantity)
        elif choice == 6:
            chemical_id = input("Enter Chemical ID: ")
            new_category = input("Enter New Category: ")
            inventory.update_category(chemical_id, new_category)
        elif choice == 7:
            chemical_id = input("Enter Chemical ID: ")
            inventory.remove_chemical(chemical_id)
        elif choice == 8:
            inventory.view_analytics()
        elif choice == 9:
            inventory.save()
            print("Goodbye!")
            break
        else:
            print("Wrong Option!")


