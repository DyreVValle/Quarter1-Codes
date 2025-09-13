full_name = input("Enter your full name (First Name, Middle Name, Last Name): ")
parts = [part.strip() for part in full_name.split(",")]
if len(parts) == 3:
	first = parts[0].capitalize()
	middle = parts[1].capitalize()
	last = parts[2].capitalize()
	middle_initial = middle[0] + "."
	formatted_name = f"{last}, {first} {middle_initial}"
	print("Formatted name:", formatted_name)
else:
	print("Please enter your name in the correct format: First Name, Middle Name, Last Name")
