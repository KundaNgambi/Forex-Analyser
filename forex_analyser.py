
import csv



filename = 'ff_calendar_thisweek.csv'

def ff_cleaner():

    with open(filename,newline = "") as infile, \
        open('ff_usd_calender.csv','w',newline="") as outfile:

        reader = csv.DictReader(infile)
        fieldnames = ['Date','Time','Title','Country','Impact']
        writer = csv.DictWriter(outfile,fieldnames =fieldnames)
        writer.writeheader()

        for row in reader:
            if row['Country'] == 'USD' and row['Impact'] == 'High':
                writer.writerow({
                    'Date': row['Date'],
                    'Time': row['Time'],
                    'Title': row['Title'],
                    'Country': row['Country'],
                    'Impact': row['Impact']
                })

    print('ff_usd_calender.csv created!')
ff_cleaner()

file = 'ff_usd_calender.csv'

def ff_cleaner_analysis():

    with open(file,'r',newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

ff_cleaner_analysis()

