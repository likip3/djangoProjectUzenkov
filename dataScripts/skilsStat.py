import csv
import math
from collections import Counter

from openpyxl import Workbook

name_list = ["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"]

currencyTransfer = {"AZN": 35.68, "BYR": 23.91, "EUR": 59.90, "GEL": 21.74, "KGS": 0.76,
                    "KZT": 0.13, "RUR": 1, "UAH": 1.64, "USD": 60.66, "UZS": 0.0055}


class Vacancy:
    def __init__(self, vacancies):
        self.name = vacancies[name_list[0]]
        self.averageSalary = math.floor((float(vacancies[name_list[1]]) + float(vacancies[name_list[2]])) / 2) * \
                             currencyTransfer[vacancies[name_list[3]]]
        self.areaName = vacancies[name_list[4]]
        self.publicationYear = int(vacancies[name_list[5]][:4])
        self.skills = vacancies['key_skills'].split('\n')


class DataSet:
    def __init__(self, filename, vacancyName):
        self.filename = filename
        self.vacancyName = vacancyName

    def csv_reader_raw(self):
        with open(self.filename, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            header = next(reader)
            headerLength = len(header)
            for row in reader:
                if '' not in row and len(row) == headerLength:
                    yield dict(zip(header, row))

    @staticmethod
    def appList(dictIN, k, c):
        if k in dictIN:
            dictIN[k].extend(c)
        else:
            dictIN[k] = c

    def getDynamics(self):
        skillsByYear = {}

        for vacancyDictionary in self.csv_reader_raw():
            vacancy = Vacancy(vacancyDictionary)
            if any(x.lower() in ['с#', 'c sharp', 'шарп', 'c#'] for x in vacancy.name.split(' ')):
                self.appList(skillsByYear, vacancy.publicationYear, vacancy.skills)

        return skillsByYear


class InputStart:
    def __init__(self):
        # self.filename = input('Введите название файла: ')
        # self.vacancyName = input('Введите название профессии: ')
        self.filename = 'vacancies_with_skills.csv'
        self.vacancyName = 'C# Програмист'
        dataset = DataSet(self.filename, self.vacancyName)
        skillsByYear = dataset.getDynamics()

        self.report = Report(self.vacancyName, skillsByYear)
        self.report.generateExelFromSheets()


class Report:
    def __init__(self, vacancyName, skillsByYear):
        self.workbook = Workbook()
        self.vacancyName = vacancyName
        self.skillsByYear = skillsByYear

    def getSheet(self, year):
        work_sheet = self.workbook.create_sheet(str(year))
        countt = Counter(self.skillsByYear[year])
        skillsCount = 10
        if len(countt) < 10:
            skillsCount = len(countt.most_common())
        for i in range(10):
            work_sheet.append([countt.most_common(skillsCount)[i][0], countt.most_common(skillsCount)[i][1]])
        return work_sheet

    def generateExelFromSheets(self):

        for i in range(2015, 2023):
            yearSheet = self.getSheet(i)
        self.workbook.remove(self.workbook['Sheet'])
        self.workbook.save('skillsReport.xlsx')


InputStart()
