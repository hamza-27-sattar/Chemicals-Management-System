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

chemical1 = Chemical("Hydrochloric Acid","CH001","Acid",500,"mL","2027-01")
chemical2 = Chemical("Ethanol","CH002","Solvent",1000,"mL","2027-02")
chemical3 = Chemical("Citric Acid","CH003","Acid",200,"mL","2027-03")


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

inventory = Inventory()
inventory.add_chemical(chemical1)
inventory.add_chemical(chemical2)
inventory.add_chemical(chemical3)

