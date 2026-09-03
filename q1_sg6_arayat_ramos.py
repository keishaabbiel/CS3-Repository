'''
1. Define the Lab: Create a Lab class that takes a room_number during initialization.
2. Define the Technician: Create a Technician class with a name. Add an attribute called assigned_lab and set it to None at first.
3. The "Hand-off" Method: Inside Technician, create a method called assign_lab(self, lab_obj). This method should take a Lab object as a parameter and store it in self.assigned_lab.
Test the Relationship:
4. Create a Lab object (e.g., chem_lab = Lab("302")).
5. Create a Technician object (e.g., mr_cruz = Technician("Mr. Cruz")).
6. Assign the lab: mr_cruz.assign_lab(chem_lab).
7. The Final Print: Print the room number using "Double Dot" access: print(mr_cruz.assigned_lab.room_number).
'''

#define the lab
class Lab:
    def __init__(self, room_number):
        self.room_number = room_number

#define the technician
class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None

    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj


# test the relationship
chem_lab = Lab("Room 205")
mr_cruz = Technician("Mr. Cruz")

# assign lab to technician
mr_cruz.assign_lab(chem_lab)

# access the lab's room number through technician
print(mr_cruz.assigned_lab.room_number)
