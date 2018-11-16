# read and write csv file
import csv, os

os.makedirs('csv_copy', exist_ok=True)

# loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue      # skip non csv files

    print('Read from '+csvFilename+' ...')
    # Read the csv file in
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        csvRows.append(row)
    csvFileObj.close()

    # Write out the csv file.
    csvFileObj = open(os.path.join('csv_copy', csvFilename),
                      'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

#
