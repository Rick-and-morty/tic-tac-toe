import csv
with open("data.csv") as open_txt:
    contents = open_txt.readlines()

# print(contents[2].split(",")[2])


clean_data = [line.replace('\n', '').split(',') for line in contents]
# print(clean_data)

with open("data.csv") as open_txt:
    # contents = csv.reader(open_txt, delimiter="|")
    contents = csv.DictReader(open_txt, delimiter='|')
    print(list(contents)[1]["Water Temp"])
