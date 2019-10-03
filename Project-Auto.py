import os
from termcolor import colored
from lazyme.string import color_print
import subprocess
import pyfiglet
import time
os.environ['TERM'] = 'xterm'


#Banner
def banner():
    ascii_banner = pyfiglet.figlet_format("Project Automation")
    os.system("cls" if os.name == "nt" else "clear")
    color_print(ascii_banner,color='yellow',bold=True)
    print('===========================',colored('Ome Mishra(De.Hack3r)','green'),'=====')



# Ptoject Descriptions

def description():
    color_print('Please Provide The Project Description',color='black',highlight='white',bold=True)

    print(colored('-------------------------------------------------------------','green'))

    description.name = input(colored('Project Name:- ','green'))
    description.date = input(colored('Starting Date:- ','green'))
    description.ip_add = input(colored("IP/URL:- ",'red'))

    color_print("========Login Cred========",color='magenta',bold=True)

    description.username = input(colored("Username:- ",'green'))
    description.password = input(colored("Password:- ",'green'))

    color_print("=====Build On technology=====",color='magenta',bold=True)

    description.buildon = input(colored("Build On (PHP/ASP etc):- ",'green'))





#Setting Up The Directory


def setdirectory():
    color_print("Enter The Desired Location",color="red",bold=True)
    setdirectory.location= input(colored(":- ",'green'))
    with open("Directory.txt", "w") as f:
        f.write(setdirectory.location)
    color_print("Wait We are Setting Up......",color='green',highlight='black',bold=True)
    time.sleep(3)
    startup()


# start automation call

def automation_call():
    color_print('=========Welcome=========',color='purple',bold=True)
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    print("\n")
    print(colored('We Will Create','red')+ colored('Some Folders And File','blue'))

    proceed = input(colored('Do You Want To Continue(Y/N) :-','yellow'))

    if proceed == "Y" or proceed=="y":
        description()
        automation()
        tool_automation()
    else:
        exit(0)



# Automation
def automation():

    #===========Setting Up Directory==========
    with open("Directory.txt") as f:
        data = f.read()
        os.chdir(data)

    # # ==========Making Directory==============
    os.mkdir(description.name)
    os.chdir(description.name)
    os.mkdir("Screenshots")
    os.mkdir("Admin")
    os.mkdir("Tool-Output")
    os.mkdir("verification")



 #===========Setting Up Creds==============

    with open("Creds.txt","w") as f:
        f.write("Application Name:- "+description.name)
        f.write("\n")
        f.write("Application Date:- " + description.date)
        f.write("\n")
        f.write("Application URL:- " + description.ip_add)
        f.write("\n")
        f.write("Email/Username:- :- " + description.username)
        f.write("\n")
        f.write("Passwords:- " + description.password)
        f.write("\n")
        f.write("Build On Tech:- " + description.buildon)

#Tools Automation

def tool_automation():
    os.chdir("Tool-Output")
    os.mkdir("Nikto")
    os.mkdir("Content-Discovery")

    # #================== Nikto =========================
		# V2 part
    #
    # # ================= Contents Discovery ==============
   



# startup
def startup():

    banner()
    color_print('Have You Saved Your Directory',bold=True,color='red')
    valid=input(colored('Y/N :- ','blue'))

    if valid == "Y" or valid=="y":
        print(colored('Ok Continue.....','blue'))
        automation_call()
    else:
        print("Please Set The Directory")
        setdirectory()

if __name__ == '__main__':
    startup()
