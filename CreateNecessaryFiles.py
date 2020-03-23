# Create the necesairy csv files

import csv


def export_ev(year):
    with open('Personenautos_2018_en_2019.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('EVs' + str(year) + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["kenteken"])
            for row in csv_reader:
                if year == 2018:
                    if row[11] == '' and row[12] == '' and row[20] == row[21] and row[21] < str(year + 1) + "0101":
                        writer.writerow([row[0], row[20], row[21]])
                else:
                    if row[11] == '' and row[12] == '' and row[20] == row[21] and row[21] >= str(year) + "0101":
                        writer.writerow([row[0], row[20], row[21]])


def export_non_ev(year):
    with open('Personenautos_2018_en_2019.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('nonEVs' + str(year) + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["kenteken"])
            for row in csv_reader:
                if year == 2018:
                    if (row[11] != '' or row[12] != '') and row[20] == row[21] and row[21] < str(year + 1) + "0101":
                        writer.writerow([row[0], row[21], row[20]])
                else:
                    if (row[11] != '' or row[12] != '') and row[20] == row[21] and row[21] > str(year) + "0101":
                        writer.writerow([row[0], row[21], row[20]])


def main():
    export_ev(2018)
    export_ev(2019)
    export_non_ev(2019)
    export_non_ev(2018)


main()
