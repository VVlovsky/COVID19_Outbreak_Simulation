import csv
import requests
import os


def download():
    rc = []
    rr = []
    rd = []
    path = os.getcwd()

    death_url = (
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    confirmed_url = (
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    recovered_url = (
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    req = requests.get(death_url)
    url_content = req.content
    csv_file = open(path + '/../data/death.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

    req = requests.get(confirmed_url)
    url_content = req.content
    csv_file = open(path + '/../data/confirmed.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

    req = requests.get(recovered_url)
    url_content = req.content
    csv_file = open(path + '/../data/recovered.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

    cv = CSVParse('../data/confirmed.csv')

    try:
        i = 4
        while True:
            rc.append(cv.read([i]))
            i += 1
    except:
        pass

    cv = CSVParse('../data/recovered.csv')
    try:
        i = 4
        while True:
            rr.append(cv.read([i]))
            i += 1
    except:
        pass

    cv = CSVParse('../data/death.csv')
    try:
        i = 4
        while True:
            rd.append(cv.read([i]))
            i += 1
    except:
        pass


class CSVParse:
    def __init__(self, csv_file, delimiter=','):
        self.csv_file = csv_file
        self.delimiter = delimiter

    def read(self, columns):
        to_return_arr = []
        with open(self.csv_file, newline='') as csvf:
            reader = csv.reader(csvf, delimiter=self.delimiter, quotechar='"')

            for row in reader:
                # if row[1] == 'Country Code' or row[1] == "country_name":
                #     continue
                for c in columns:
                    if row[c] != '':
                        to_return_arr.append(row[c])
                    else:
                        to_return_arr.append(0)
            to_return_arr.pop(0)
            # print(to_return_arr)
        return sum([int(x) for x in to_return_arr])

download()
