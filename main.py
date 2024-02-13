import theaterSeats as t


for row in t.theater_seats:  # goes through the set of lists
  for seat in row:           # defines each seat in each list
    print(seat, end='\t')    # prints each seat out in
  print('\n')
  
print()

# # #This bit does the same but with the second list
for row in t.theater_seats2: 
  for seat in row:
    print(seat, end='\t')
  print('\n')

