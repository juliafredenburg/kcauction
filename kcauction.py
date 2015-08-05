import csv
import itertools

# read copy and pasted lines from pdf into a list

with open('DailyRecord01-03.txt', 'r') as records:
  lines = []
  for line in records:
    lines.append(line)

# remove blank lines from the list

  no_blank_lines = []
  for line in lines:
    if line != '\n':
      no_blank_lines.append(line)

# create a new sublist each time a new "K2014" is read, add the K2014 number, the price, and th 00-000 number to the sublist.

  records = []
  zero_characters = ['0', 'O', 'Q', 'o', 'P']
  possible_errors = []
  possible_errors_with_dashes = []
  possible_errors_as_permutations = itertools.product(zero_characters, repeat=5)

  j = 0
  for error in possible_errors_as_permutations:
    possible_errors.append('')
    k = 0
    for character in error:
      possible_errors[j] += character
      k += 1
      if k == 2:
        possible_errors[j] += '-'
    j += 1


  i = -1
  for line in no_blank_lines:
    if 'K2' in line:
      price_start = line.find('$')
      k_end = price_start - 1
      records.append([line[0:k_end]])
      i += 1
      records[i].append(line[price_start:len(line)])
    else:
      for error in possible_errors:
        if error in line:
          records[i].append(line)

with open('properties.csv', 'wb') as properties:
  writer = csv.writer(properties)
  for record in records:
    writer.writerow(record)