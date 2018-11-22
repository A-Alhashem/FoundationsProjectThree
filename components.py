# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = name
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []
        self.president = None


    def assign_president(self, person):
        # your code goes here!
        if person in self.members:
            self.president = person


    def recruit_member(self, person):
        # your code goes here!
        if person not in self.members:
            self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        for member in self.members:
            if member == self.president:
                print("- %s (%s years old, President) - %s" % (member.name, member.age, member.bio))
            else:
                print("- %s (%s years old) - %s" % (member.name, member.age, member.bio))
