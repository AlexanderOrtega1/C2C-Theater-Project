import theaterSeats as t


#for row in t.theater_seats:  # goes through the set of lists
  #for seat in row:           # defines each seat in each list
    #print(seat, end='\t')    # prints each seat out in
  #print('\n')
  
print()

# # #This bit does the same but with the second list
for row in t.theater_seats2: 
  for seat in row:
    print(seat, end='\t')
  print('\n')

empty_seats = []

for row in t.theater_seats2:
  index = 0
  for seat in row:
    if seat == 'o':
      empty_seat = f'{row[0]}{index}'
      empty_seats.append(empty_seat)
    else:
      pass
    index += 1

for i in empty_seats:
  print(i)