'''
Author: Shep O'Keeffe
Date: 9/30/24
Description: An algorithm to determine the postage cost for entered mail. Its type is determined by its dimensions. The cost to mail it
is determined by its type and the number of postal zones it will travel through.
Bugs: 
Sources: computer science classes
'''
def get_mail_type(length, height, thickness):
    '''
    finds the type of mail being sent based on the measurements of the package
    args:
        length (float): the length of the package
        height (float): the height of the package
        thickness (float): the thickness of the package
    returns:
        str: the type of mail the package is
    ''' 
    if height < 3.5:
        return "unmailable"
    else:
        if length < 3.5:
            return "unmailable"
        else:
            if thickness < 0.007:
                return "unmailable"
            elif thickness >= 0.007 and thickness <= 0.016:
                if length <= 4.25:
                    return "postcard"
                else:
                    return "large postcard"
            elif thickness > 0.016 and thickness < 0.25:
                return "envelope"
            elif thickness >= 0.25 and thickness <= 0.5:
                return "large envelope"
            elif thickness > 0.5:
                if length + height*2 + thickness*2 <= 84.0:
                    return "package"
                elif length + height*2 + thickness*2 > 84.0 and length + height*2 + thickness*2 <= 130.0:
                    return "large package"
                else:
                    return "unmailable"

def get_zip_zone(zipcode):
    '''
    finds the zone in which a zipcode resides
    args:
        zipcode (int): the entered zipcode
    returns:
        int: the zone of the zipcode
    '''
    if zipcode <= 6999:
        return 1
    elif zipcode >= 7000 and zipcode <= 19999:
        return 2
    elif zipcode >= 20000 and zipcode <= 35999:
        return 3
    elif zipcode >= 36000 and zipcode <= 62999:
        return 4
    elif zipcode >= 63000 and zipcode <= 84999:
        return 5
    elif zipcode >= 85000 and zipcode <= 99999:
        return 6

def get_final_cost(get_mail_type, length, height, thickness, get_zip_zone, zipcode_1, zipcode_2):
    '''
    finds the final postage cost of the mail based on the mail type and the amount of zipcode zones the mail will travel through
    args:
        get_mail_type (str): the output of the "get_mail_type" function (the mail type)
        length (float): the length of the mail
        height (float): the height of the mail
        thickness (float): the thickness of the mail
        get_zip_zone (int): the output of the "get_zip_zone" function (the zipcode zone)
        zipcode_1 (int): the zipcode from which the mail is being sent
        zipcode_2 (int): the zipcode to which the mail is being sent
    returns:
        str: "unmailable" (if the mail is unmailable)
        int: the postage cost of the mail (otherwise)
    '''
    #the price of a mailable piece of mail is calculated by adding the base cost of the mail type (e.g. 20 cents) to the cost per zone 
    #(e.g. 3 cents) times the amount of zones traveled (the positive difference of the starting and ending zone).
    
    if get_mail_type(length, height, thickness) == "unmailable":
        print("unmailable")
    elif get_mail_type(length, height, thickness) == "postcard":
        return .20 + .03 * abs(get_zip_zone(zipcode_1) - get_zip_zone(zipcode_2))
    elif get_mail_type(length, height, thickness) == "large postcard":
        return .37 + .03 * abs(get_zip_zone(zipcode_1) - get_zip_zone(zipcode_2))
    elif get_mail_type(length, height, thickness) == "envelope":
        return .37 + .04 * abs(get_zip_zone(zipcode_1) - get_zip_zone(zipcode_2))
    elif get_mail_type(length, height, thickness) == "large envelope":
        return .60 + .05 * abs(get_zip_zone(zipcode_1) - get_zip_zone(zipcode_2))
    elif get_mail_type(length, height, thickness) == "package":
        return 2.95 + .25 * abs(get_zip_zone(zipcode_1) - get_zip_zone(zipcode_2))
    elif get_mail_type(length, height, thickness) == "large package":
        return 3.95 + .35 * abs(get_zip_zone(zipcode_1) - get_zip_zone(zipcode_2))

def main():
    '''
    takes the data of a piece of mail, converts it to the correct data types, and runs it though the other functions (five times).
    only accepts an input consisting of five pieces of numerical data.
    '''
    main_iterations = 0 #stop this
    while True:
        if main_iterations < 5:
            while True:
                try:
                    mail_details = input("package measurements and zipcodes: ").split(",")#splits the input into pieces when it
                    
                    length = float(mail_details[0])
                    height = float(mail_details[1])
                    thickness = float(mail_details[2])
                    zipcode_1 = int(mail_details[3])
                    zipcode_2 = int(mail_details[4])

                    print(get_final_cost(get_mail_type, length, height, thickness, get_zip_zone, zipcode_1, zipcode_2))
                    main_iterations += 1
                    break
                except ValueError:
                    print("data must be numerical")
                except IndexError:
                    print("data must be 5 values")
        else:
            break

main()