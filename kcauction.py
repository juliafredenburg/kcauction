import csv

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

# create a new sublist each time a new "K2014" is read

  records = []
  i = -1
  for line in no_blank_lines:
    if 'K2014' in line:
      records.append([line])
      i += 1
    else:
      records[i].append(line)

# NEXT:
# check how long each sublist is
# make each sublist the same length
# line up like items in sublists
# combine data that is spread accross multiple list items



with open('properties.csv', 'wb') as properties:
  writer = csv.writer(properties)
  for record in records:
    writer.writerow(record)