import re

# Initialize variables
month = ''
count_day = 0
flag_day = False
actions = ['Slept', 'Ate', 'Meditated', 'Exercised', 'Read']
counts = {'Slept': 0, 'Ate': 0, 'Meditated': 0, 'Exercised': 0, 'Read': 0}
youtube_hours = 0

# with open('/Users/jamiesu/Desktop/main/Coding/tally_my_journal/temp.txt') as file:
with open('/Users/jamiesu/Desktop/main/Journals & Reflections/Journals/tally.txt') as file:
	for line in file:

		# First, retrieve the month name (which I always write before everything else)
		if not month:
			find_month = re.search(r'^End (.+)', line)
			if find_month:
				month = find_month.group(1)

		else:
			# Use regex to find the start of a different day
			if re.search(r'^\d+?\w\w:', line):
				flag_day = True

			# (I always write the actions on the line after the day number)
			elif flag_day == True:
				for act in actions:
					# Parse the actions for the day
					if re.search(act, line, re.IGNORECASE):
						counts[act] += 1

				# Parse the Youtube-hours value for the day
				hours_for_the_day = re.search(r'Youtube: ~?(.+?) hours?', line, re.IGNORECASE)
				if hours_for_the_day:	# technically this if-clause shouldn't be necessary
					youtube_hours += float(hours_for_the_day.group(1))

				count_day += 1
				flag_day = False

# Format and print the output
print(f"\nMonth: \t\t\t{month}")
print(f"Total Days Counted: \t{count_day} days\n")

for key, value in counts.items(): 
	if (key == 'Exercised') or (key == 'Meditated'): tabs = '\t\t'
	else: tabs = '\t\t\t'

	if value == 1: days = 'day'
	else: days = 'days'

	print(f"{key}: {tabs}{value} {days}")

print(f"Total Youtube Hours: \t{youtube_hours} hours\n")
