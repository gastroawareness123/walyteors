from DoctorServiceBackend.settings import *
from DoctorServiceBackend.wsgi import *
from DoctorServiceBackend.asgi import *

from users.models import *

import csv

file_path = './QR CODE COMPILED LIST.csv'
with open(file_path, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    # fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        print(row)
        [ sr_no, region, sales_officer_name, doctor_name, doctor_category ] = row
        
        sales_region, is_region_created = SalesOfficerRegion.objects.get_or_create(name=region)
        sales_officer, is_sales_officer_created = SalesOfficer.objects.get_or_create(name = sales_officer_name, region=sales_region)
        category, is_category_created = DoctorCategory.objects.get_or_create(name = doctor_category)
        doctor = Doctor.objects.create(name = doctor_name, sales_officer = sales_officer, category = category)

  