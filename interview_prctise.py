#Find the 2nd highest number from the list
numbers = [1,2,3,4,65,24,90,4,45,15,15]

highest_number = numbers[0]
second_highest_number = numbers[0]

for number in numbers:
    if number > highest_number:
        second_highest_number = highest_number
        highest_number = number
    elif number > second_highest_number and second_highest_number != number:
        second_highest_number = number
print(second_highest_number)
print(highest_number)

#=============================================
#Taking a Input Sring
INPUT_STRING = "Mitesh Mitesh is giving giving interview"

#Create a List of Split Words
WORDS = INPUT_STRING.split()

#CREATE a LIST OF UNIQUE WORDS
UNIQUE_WORDS = []

#To Execute a for loop in List of WORDS
for WORD in WORDS:
    if WORD not in UNIQUE_WORDS:
        UNIQUE_WORDS.append(WORD)

# To CREATE OUTPUT STRING FROM UNIQUE LIST
OUTPUT_STRING = ' '.join(UNIQUE_WORDS)

#PRINT INPUT_STRING,& OUTPUT_STRING
print(f"Original input String, {INPUT_STRING}")
print(f"Unique Output String, {OUTPUT_STRING}")
