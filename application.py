"""Countries and Capitals"""
LIBRARY = {}
LIBRARYLIST = []
VALUE = []
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
def init():
    """Menu for init"""
    print "  "
    print ">>>>Welcome to Countries and Capitals<<<< "
    print "Write - Countrie - to insert a country and its capital:  "
    print "Write - exit -  to exit"
    print "   "
    question = raw_input("Choose an option:  ")
    questionlower = question.lower()
    if questionlower == "Countries" or questionlower == "countries" \
        or questionlower == "Countries " or questionlower == "countries ":
        addcountries()
        clean()
    elif questionlower == "Exit" or questionlower == "exit" \
        or questionlower == "Exit " or questionlower == "exit ":
        clean()
    else:
        clean()
        print "  "
        print "<<<Enter a valid option: >>>"
        init()

def listcountries():
    """List of countries"""
    print "  "
    print ">>>List of Countries<<<"
    count = LIBRARY.keys()
    for count in LIBRARY:
        print "---", (count.title())

def listcapitals():
    """List of capitals"""
    print "  "
    print ">>>List of Capitals<<<"
    cap = LIBRARY.values()
    for cap in LIBRARY.values():
        print "---", (cap.title())

def listall():
    """list of all"""
    print "  "
    print "\n>>> List of Countries and Capitals<<<"
    for i in LIBRARY:
        print"{Countries:^20s}: {Capital}" .format(Countries=i, Capital=LIBRARY[i])

def listordered():
    """list ordered"""
    print "  "
    print ">>> List of Countries and Capitals Ordered<<<"
    longi = len(LIBRARY.values())
    cont = 0
    ordercap = sorted(LIBRARY.values())
    ordercou = sorted(LIBRARY.keys())
    while  cont < longi:
        print "{Countries:^20s}: {Capital}" \
            .format(Countries=str(ordercou[cont]), Capital=str(ordercap[cont]))
        cont += 1

def menu():
    """principal menu"""
    print "Opciones que desea hacer:  "
    print "Write - Countries - to view a list of countries."
    print "Write - Capitals - to view a list of Capitals."
    print "Write - All - if you want to see the list of countries with their capitals."
    print "Write - AllOrdered - si desea ver la lista ordenada de paises con sus capitales."
    print "Write - AllMail - if you want the list to email lgarcia@cognits.co."
    print "Write - Exit - to exit the program."
    try:
        print "  "
        options = raw_input("Choose an option:  ")
        if options == "Countries" or options == "countries"\
            or options == "Countries " or options == "countries ":
            clean()
            listcountries()
            menu()
        if options == "Capitals" or options == "capitals"\
            or options == "Capitals " or options == "capitals ":
            clean()
            listcapitals()
            menu()
        elif options == "All" or options == "all"\
            or options == "All " or options == "all ":
            clean()
            listall()
            menu()
        elif options == "AllOrdered" or options == "allordered"\
            or options == "AllOrdered " or options == "allordered ":
            clean()
            listordered()
            menu()
        elif options == "AllMail" or options == "allmail"\
            or options == "AllMail " or options == "allmail ":
            clean()
            email()
            menu()
        elif options == "Exit" or options == "exit"\
            or options == "Exit " or options == "exit ":
            clean()
        else:
            clean()
            print "  "
            print "<<<Enter valid option>>>"
            print "  "
            menu()
    except ValueError:
        print "<<<Enter valid option for the Menu: >>>"
        menu()

def clean():
    """function for clean"""
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")
clean()

def email():
    """function for email"""
    question3 = raw_input("To:  ")
    question4 = raw_input("Subject:  ")
    clean()
    question = raw_input("Username:  ")
    question2 = raw_input("Password:  ")
    clean()
    username = question
    password = question2
    toaddrs = question3
    body = "Countries\t-------\tCapitals\n"
    for msg in LIBRARY:
        body = body + str(msg) +"\t-------\t" +str(LIBRARY[msg]) + "\n"
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = toaddrs
    msg['Subject'] = question4
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(username, toaddrs, text)
        server.quit()
        print "   "
        print "From:   ", question
        print "To:     ", question3
        print "Subject:", msg['Subject']
        print "   "
        print"<<<Your email has been sent ..."
        print"   "
    except ValueError:
        print"    "
        print"<<<There was an error in sending ..."
        print"   "
def addcountries():
    """This function allows you to add data to lists and dictionaries"""
    try:
        key = raw_input("Add Countries: ")
        keylow = key.lower()
        LIBRARYLIST.append(keylow)
        lists = raw_input("Add Capital: ")
        LIBRARY[key] = lists
        again()
    except ValueError:
        print "<<<Enter the data correctly>>>"
        addcountries()
        clean()

def again():
    """This function asks if you want to add another country"""
    question = raw_input("Do you want to insert another Countries and Capital (y/n) ")
    questionlower = question.lower()
    if questionlower == "y" or questionlower == "yes"\
        or questionlower == "y " or questionlower == "yes ":
        addcountries()
    elif questionlower == "n" or questionlower == "no"\
        or questionlower == "n " or questionlower == "no ":
        clean()
        menu()
    else:
        clean()
        print "A valid option and enter (y/n)"
        again()
init()
