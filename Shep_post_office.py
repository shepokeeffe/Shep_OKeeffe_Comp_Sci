mail_deets = input("enter the data: ").split(",")

length = float(mail_deets[0])
height = float(mail_deets[1])
thickness = float(mail_deets[2])
zipcode_1 = int(mail_deets[3])
zipcode_2 = int(mail_deets[4])

def main():
    get_zipcode_1(zipcode_1)

#def find_mail_type():
#    if int(length) >= 3.5 
#       mail_type = "unmailable"
#    elif 

#find_mail_type()

def get_zipcode_1(zipcode_1):
    zip_area_1 = zip_area_1
    if int(zipcode_1) <= 6999:
        zip_area_1 = 1
    elif int(zipcode_1) >= 7000 and int(zipcode_1) <= 19999:
        zip_area_1 = 2
    elif int(zipcode_1) >= 20000 and int(zipcode_1) <= 35999:
        zip_area_1 = 3
    elif int(zipcode_1) >= 36000 and int(zipcode_1) <= 62999:
        zip_area_1 = 4
    elif int(zipcode_1) >= 63000 and int(zipcode_1) <= 84999:
        zip_area_1 = 5
    elif int(zipcode_1) >= 85000 and int(zipcode_1) <= 99999:
        zip_area_1 = 6