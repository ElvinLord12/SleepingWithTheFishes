import csv

def parse_catches(file, species):
    with open(file) as file_csv:
        reader = csv.reader(file_csv, delimiter=',')
        count = 0
        for row in reader:
            if count == 0:
                count += 1
            else:
                if species == row[0]:
                    country = row[3]
                    animal = row[0]
                    area = row[1]
                    print(animal)
                    print (country)
                    print (area)

                else:
                    pass


def parse_country(file, country):
    with open(file) as file_csv:
        reader = csv.reader(file_csv, delimiter=',')
        count = 0
        for row in reader:
            if count == 0:
                count+= 1
            else:
                if country == row[0]:
                    return row[1]
                else:
                    pass


def parse_species(file, species):
    with open(file) as file_csv:
        reader = csv.reader(file_csv, delimiter=',')
        count = 0
        for row in reader:
            if count == 0:
                count += 1
            else:
                if species == row[0]:
                    print (row[1])
                    return row[2]
                else:
                    pass


def write_out_file(file_name, file):
    with open(file_name, mode='w') as out_file:
        writer = csv.writer(out_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(['Species', 'Country'])
        count = 0
        with open(file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                if count == 0:
                    count += 1
                else:
                    writer.writerow([parse_species("data_sets/species.csv",row[0]),parse_country("data_sets/countries.csv", row[3])])

write_out_file("out.csv", "data_sets/ICESCatchDataset2006-2015.csv")



file = "data_sets/countries.csv"
country = "IT"
grabbed_country = parse_country(file,country)
print(country)
print(grabbed_country)

print("=====")

file = 'data_sets/species.csv'
species = (parse_species(file,'AAB'))
print(species)

print("=====")

file = "data_sets/ICESCatchDataset2006-2015.csv"
catch = parse_catches(file,"ABK")