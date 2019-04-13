import csv

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



file = 'data_sets/species.csv'
species = (parse_species(file,'AAB'))
print(species)