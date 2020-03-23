# Create the necesairy csv files

import csv


def export_csv():
    with open('Personenautos_2018_en_2019.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["kenteken", "ev", "year"])
            for row in csv_reader:
                if row[11] == '' and row[12] == '' and row[20] == row[21]:
                    writer.writerow([row[0], True, str(row[21])[:4]])
                elif row[0] != "Kenteken":
                    writer.writerow([row[0], False, str(row[21])[:4]])


def main():
    export_csv()

main()
