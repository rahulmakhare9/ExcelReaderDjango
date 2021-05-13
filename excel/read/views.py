from django.shortcuts import render
from django.http import HttpResponse
import xlrd

def index(request):
    response = ""
    wb = xlrd.open_workbook('C://Users//Acer//PycharmProjects//ExcelRead//excel//read//file.xls')
    # need to replace path as per directory structure
    # wb = xlrd.open_workbook('C://Users//Acer//PycharmProjects//ExcelRead//excel//read//file.xls')
    l = len(wb.sheet_names())
    print(l)
    for i in range(l):
        sheet = wb.sheet_by_index(i)
        print(sheet)
        response = response + "<br>" + str(sheet)
        response = response + "<table style='border:1px solid black'>"
        for s in sheet:
            print("k:"+str(s)[1:-1])
            text = "<tr>"
            for data in str(s)[1:-1].split(","):
                print(data)
                print(data.split(":")[1])
                text = text + "<td style='border:1px solid black'>" + data.split(":")[1] + "</td>"
            response = response + "" + text + "</tr>"
        response = response + "</table>"
    return HttpResponse(response)
