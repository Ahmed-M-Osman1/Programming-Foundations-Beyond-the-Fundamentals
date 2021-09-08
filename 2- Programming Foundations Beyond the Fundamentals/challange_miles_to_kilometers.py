miles_value = input('Enter a distance in miles: ')
kilometers_value = int(miles_value) * float(1.609344)
if int(miles_value) == 1:
    print("The one mile is equal to", kilometers_value, "kilometers")
else: 
    print("The", miles_value,"miles is equal to", kilometers_value)