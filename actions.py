# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Abdulaziz"
my_age = 31
my_bio = "Learning to Program"
myself = Person(my_name, my_bio, my_age)

def introduction():
	print("Hello, %s. Welcome to our portal." % my_name)

def options():
	# your code goes here!
	print("-----")
	print("Would you like to: ")
	print("1) Create a new club.")
	print("2) Browse and join clubs")
	print("3) View existing club")
	print("4) Display members of a club")
	print("-1) Close application")
	user_option = input(">")
	return user_option


	"""
	Instructor created a new function under this called print_population!!
	"""

def print_population():
	print("------------------------")
	index = 1
	for person in population:
		print("(%s) %s" % (index, person.name))
		index += 1


def create_club():
	# your code goes here!
	# get club name
	club_name = input("Pick a name for your awesome new club:\n ")

	# get the club description
	club_description = input("What is your club about?\n")

	club = Club(club_name, club_description)
	club.recruit_member(myself)
	club.assign_president(myself)

	# get the members to recuit to the club
	print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop): ")
	print_population()
	person_to_be_recruited = ""
	while person_to_be_recruited != -1:
		person_to_be_recruited = int(input("> "))
		if person_to_be_recruited == "":
			print("Please enter a valid number")
		else:
			club.recruit_member(population[person_to_be_recruited-1])


	# print the new club
	print("Here's your new club...")
	print(club.name)
	print(club.description)
	club.print_member_list()
	clubs.append(club)


	

def view_clubs():
	# your code goes here!
	for club in clubs:
		print("NAME: %s\nDESCRIPTION: %s\nMEMBERS: %s\n" % (club.name, club.description, len(club.members)))
	

def view_club_members():
	# your code goes here!
	view_clubs()
	club_found = True
	while club_found:
		club_name = input("Enter the name of the club who's members you'd like to see: ")
		for club in clubs:
			if club.name.lower() == club_name.lower():
				club.print_member_list()
				club_found = False
	

def join_clubs():
	# your code goes here!
	view_clubs()
	club_name = input("Enter the name of the club you would like to join: \n")
	for name in clubs:
		if name.name == club_name:
			name.recuit_member(myself)
			print("%s has just joined %s!" % (myself.name, name.name))

	

def application():
	introduction()
	# your code goes here!
	option = ""
	while option != "-1":
		option = options()
		if option == "1":
			create_club()
		elif option == "2":
			join_clubs()
		elif option == "3":
			view_clubs()
		elif option == "4":
			view_club_members()

