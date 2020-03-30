# Create the necessary csv files

import csv


def export_csv():
    with open('Personenautos_2018_en_2019.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # create column names for dataset
            writer.writerow(["kenteken", "ev", "year"])
            kentekens = []
            for row in csv_reader:
                # row 11 and 12 empty to check if is ev and row 20 = 21 for only non imported cars
                if row[11] == '' and row[12] == '' and row[20] == row[21]:
                    # write to our dataset the license row0 True (is an ev) and the year
                    writer.writerow([row[0], True, str(row[21])[:4]])
                    kentekens.append(row[0])
                # row0 not equal to kenteken because that is column name and same as above for 20 and 21s
                # row0 not in kentekens to skip the evs
                elif row[0] != "Kenteken" and row[20] == row[21] and row[0] not in kentekens:
                    # write to dataset row0 --> license false for no ev and the year
                    writer.writerow([row[0], False, str(row[21])[:4]])


def main():
    export_csv()

main()
