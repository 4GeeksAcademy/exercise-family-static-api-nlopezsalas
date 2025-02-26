
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {"id": self._generateId(), "first_name": "John", "last_name": self.last_name, "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": self._generateId(), "first_name": "Jane", "last_name": self.last_name, "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": self._generateId(), "first_name": "Jimmy", "last_name": self.last_name, "age": 5, "lucky_numbers": [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    # def add_member(self, member):
    #     self._members.append(member)
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name  # Ensure the last name is Jackson
        self._members.append(member)

    def delete_member(self, id):
        self._members = [member for member in self._members if member['id'] != id]
        
        # fill this method and update the return
        # member_pos = None
        # for pos in range(0, len(self._members)):
        #     if self._members[pos]["id"] == id:
        #         member_pos = pos
        # if member_pos != None: 
        #     self._members.pop(member_pos)
        #     return 'ok'
        # else: return 'no existe el id'

    def get_member(self, id):
        member = list(filter(lambda member: member["id"] == id ,self._members))
        if member != []:
            return member[0]
        else: return None

        # for pos in range(0, len(self._members)):
        #     if self._members[pos]["id"] == id:
        #         return self._members[pos]
            
        # return None
    
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
       return self._members
