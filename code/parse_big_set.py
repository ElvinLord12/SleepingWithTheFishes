import csv

def parse_big_shit(file):
    with open("cleaned_bacteria.csv", mode='w') as out:
        writer = csv.writer(out,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        writer.writerow(['TARA 004', 'TARA 141', 'TARA 142','TARA 142 S','TARA 145',
                         'TARA 145 S','TARA 146', 'TARA 146 S',
                         'TARA 148','TARA 148 S','TARA 149','TARA 149 S',
                         'TARA 150','TARA 151','TARA 152','TARA 152 S','TARA 066',
                         'TARA 067','TARA 068','TARA 068 S','TARA 70','TARA 70 S',
                         'TARA 072','TARA 072 S','TARA 076','TARA 076 S','TARA 078',
                         'TARA 078 S','TARA 082',])
        count = 0
        with open(file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                if count == 0:
                    count += 1
                elif count == 1:
                    bacteria = row[0]

                else:
                    pass


parse_big_shit("bacteria.csv")