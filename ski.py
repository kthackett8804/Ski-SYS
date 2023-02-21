#login page
#user is asked for a username and password
#if both is correct then user logs in

def login():
    print("""

    #####################################


            Welcome to Clarendon High School                                                 #
                 France ski trip
                            
                 Login Menu                                                                         #

    #####################################
    """)



    user=input("enter username: ")
    password=input("enter password: ")

    user_correct= "mrwalsh5"
    pass_correct= "password5"

    while user != user_correct or password != pass_correct:
        print("try again")
        user=input("enter username: ")
        password=input("enter password: ")
        
    print("logged in ")

#main menu page
#aks user to enter an option
#then takes user to that option
def main_menu():
    print('''#######################################################################                                                                                     					Main Menu
                                                                                                                            
                         Choose from one of the following options:				
                                                                                                    
        A)New student                                			
                                                                                                    
        B)Groups                                         C)Exit     				                                                                                              
    ##################################################################
    ''')

    menu_options=input("choose from A,B, or C: ")
    menu_options=menu_options.upper()

    valid=False
    while valid==False:
        if menu_options == "A" or menu_options == "B" or menu_options == "C":
            valid=True
        else:
            menu_options=input("invalid option. choose option A,B, or C: ")
            menu_options=menu_options.upper()
    return(menu_options)                  


#user asked to enter student details
#then the information will be stored in a file
#file called newstudentdetails.txt
def newstudent():
    print('''#################################################
                                new student details
             #################################################             ''')
  
    
    #name presence check
    valid=False
    while not valid:
        first_name = input("Enter students name: ")
        if len(first_name) > 0:
            valid = True
        else:
            print('please enter the students name')

    #surname presence length check
    valid=False
    while not valid:
        surname = input("Enter students surname: ")
        if len(surname) > 0:
            valid = True
        else:
            print("please enter the students surname")
        
    #age type/range/presence check 
    valid = False
    while valid == False:
        try:
            age = int(input("Enter students age: "))
            if age >= 11 and age <= 18:
                valid = True
            else:
                print("You must enter a valid number between 11 and 18")
        except:
            print("you must enter a valid number between 11 and 18")
        
    #gender presence/range check
    valid = False
    while valid == False:
            gender =input("Enter the gender of the student f/m: ")
            gender=gender.lower()
            if gender == "f" or gender == "m":
                    valid = True
            else:
                print("You must enter f or m")
        
    #yeargroup type/range/presence check
    valid = False
    while valid == False:
        try:
            group= int(input("Enter students yeargroup: "))
            if group >= 8 and group <= 14:
                valid = True
            else:
                print("You must enter a yeargroup between 8 and 14")
            
        except:
            print("You must enter a yeargroup between 8 and 14")


    myfile=open("studentdetails.txt", "a")
    myfile.write(first_name + " ")
    myfile.write(surname + " ")
    myfile.write(str(age) + " ")
    myfile.write(gender + " ")
    myfile.write(str(group) + " ")
    myfile.close()

#user asked enter 5 ski times
#calculates average of the 5 ski times
#stores average in a file
def skitimes():
    print("""###############################################
                            ski times
            ################################################""")

    total = 0

    for i in range(0,5):
        valid=False
        while valid== False:
            try:
                skitimes= int(input("enter your ski time in seconds: "))
                if skitimes < 35 or skitimes > 650:
                    print("ski time must be between 35 and 650 seconds")
                else:
                    valid=True
                    total=total + skitimes
            except:
                print("ski time must be between 35 and 650 seconds")

    average= total / 5
    print("your average is" ,average)
    

    myfile=open("studentdetails.txt", "a")
    myfile.write(str(average) + " ")
    myfile.close()
    
    
#answer ski questions
#calculates score
#stores score in a file
def ski_quiz():

    print("""##############################################
                         ski quiz
            ###############################################
            """)

    score = 0
    print("Question 1 ")
    q1=input("""How should you behave when skiing?
        A- in a fun way
        B- in a safe way
        C- in a cool way
       : """)
    q1=q1.upper()
    a1="B"
    if q1 == a1:
        score=score+1

    print("Question 2")
    q2=input("""if you witness a accident you should ...
         A- Post it on social media
         B- stop and help
         C- run away
         : """)
    q2=q2.upper()
    a2="B"
    if q2 == a2:
        score=score+1
        
    print("Question 3")
    q3=input("""When skiing you should wear?
          A- shorts and a t-shirt
          B- a swimsuit
          C- ski gear
          : """)
    q3=q3.upper()
    a3="C"
    if q3==a3:
        score=score+1

    print("question 4")
    q4=input("""when overtaking how much space should you give?
            A- enough space to allow a person to move around you
            B- less than a metre
            C- enough space to get a bus through
            : """)
    q4=q4.upper()
    a4="A"
    if q4 == a4:
        score=score+1
             
    print("question 5")
    q5=input("""what things are important to remain in control?
            A- your hat, shoes and trousers
            B- how hungry, tired or angry you are
            C- your ability, condition of terrain, weather
            :""")
    q5=q5.upper()
    a5="C"
    if q5 == a5:
        score=score+1

    print("question 6")
    q6=input("""if its your first time skiiing what slope should you use?
             A- beginner slope
             B-advanced slope
             C-expert slope
             :""")
    q6=q6.upper()
    a6="A"
    if q6==a6:
        score=score+1

    print("question 7")
    q7=input("""what is the best weather to ski in?
            A- rain
            B- average weather
            C- hurricane
            :""")
    q7=q7.upper()
    a7="B"
    if q7 ==a7:
        score=score+1

    print("your score is", score)

    myfile=open("studentdetails.txt", "a")
    myfile.write(str(score) + "\n")
    myfile.close()

#report groups
#sorts users into different groups
def groups():
    print('''##########################################################                                              Reports
                                               
                    Choose from one of the following report options:				
                                                                                                         
            A)average ski times     B)Year Group        E)exit	
                                                                                                        
            C)ability               D)Gender     	    F) back to main menu		                                                                                              
        ##################################################################
        ''')
    report_options=input("choose from A,B,C,D,E or F: ")
    report_options=report_options.upper()
    
    
    valid=False
    while valid==False:
        if report_options == "A" or report_options== "B" or report_options == "C" or report_options == "D" or report_options == "E" or report_options == "F":
            valid=True
        else:
            report_options=input("invalid option. choose option A,B,C,D,E or F: ")
            report_options=report_options.upper()
    return(report_options)                  

def read_details():

    file=open("studentdetails.txt", "r")

    first_name= [ ]
    surname= [ ]
    age= [ ]
    gender= [ ]
    yeargroup= [ ]
    average= [ ]
    score= [ ]

    for line in file:
        items=line.split(" ")

        first_name.append(items[0])
        surname.append(items[1])
        age.append(items[2])
        gender.append(items[3])
        yeargroup.append(items[4])
        average.append(items[5])
        score.append(items[6])

    file.close()
    return(first_name,surname,age,gender,yeargroup,average,score)

#average ski time report
def reportA():
    first_name,surname,age,gender,yeargroup,average,score=read_details()
    for i in range(0, len(age)):
        print(first_name[i],surname[i],average[i])

#yeargroup report
def reportB():
    first_name,surname,age,gender,yeargroup,average,score=read_details()
   
    valid = False
    while valid == False:
        try:
            yrgroup= int(input("please enter the yeargroup you want to see? 8,9,10,11,12,13 or 14 "))
       
            if yrgroup==8 or yrgroup==9 or yrgroup==10 or yrgroup==11 or yrgroup==12  or yrgroup==13  or yrgroup==14:
                 valid = True
            else:
                print("please enter the yeargroup you want to see? 8,9,10,11,12,13 or 14 ")
        except:
            print("please enter the yeargroup you want to see? 8,9,10,11,12,13 or 14 ")
    print("ok")
    if yrgroup == 8:
        print("year 8 ski list")
        for i in range(0, len(age)):
            if int(yeargroup[i]) == 8:
                print(first_name[i],surname[i],yeargroup[i],gender[i])
                
    elif yrgroup == 9:
        print("year 9 ski list")
        for i in range(0, len(age)):
            if int(yeargroup[i]) == 9:
                print(first_name[i],surname[i],yeargroup[i], gender[i])
                
    elif yrgroup == 10:
        print("year 10 ski list")
        for i in range(0, len(age)):
            if int(yeargroup[i]) == 10:
                print(first_name[i],surname[i],yeargroup[i], gender[i])
                
    elif yrgroup == 11:
        print("year 11 ski list")
        for i in range(0, len(age)):
            if int(yeargroup[i]) == 11:
                print(first_name[i],surname[i],yeargroup[i], gender[i])
                
    elif yrgroup == 12:
        print("year 12 ski list")
        for i in range(0, len(age)):
            if int(yeargroup[i]) == 12:
                print(first_name[i],surname[i],yeargroup[i], gender[i])

    elif yrgroup == 13:
        print("year 13 ski list")
        for i in range(0, len(age)):
            if int(yeargroup[i]) == 13:
                print(first_name[i],surname[i],yeargroup[i], gender[i])
                
    elif yrgroup == 14:
        print("year 14 ski list")
        for i in range(0, len(age)):
            if int(yeargroup[i]) == 14:
                print(first_name[i],surname[i],yeargroup[i], gender[i])

            
#ask user what gender they want to show
#then will show a list of the gender
def reportD():
    first_name,surname,age,gender,yeargroup,average,score=read_details()
   
    valid = False
    while valid == False:
        group= input("please enter the gender group you want to see? f/m ")
        group = group.lower()

        if group == "f" or group == "m":
             valid = True
        else:
            print("invalid, enter gender? f/m ")

    if group == "m":
        print("boy ski list")
        for i in range(0, len(age)):
            if gender[i] == "m":
                print(first_name[i],surname[i],yeargroup[i], gender[i])

    elif group == "f":
        print("girls ski list")
        for i in range(0, len(age)):
            if gender[i] == "f":
                print(first_name[i],surname[i],yeargroup[i], gender[i])
                

#asks user what ability they want to show
#sorts users based on there ability
#shows them in a list
def reportC():
    first_name,surname,age,gender,yeargroup,average,score=read_details()
    abilityscore = []

    for i in range(0, len(age)):
        abilityscore.append(float(average[i])/(int(score[i])*10))
    
    valid= False
    while valid == False:
        try:
            ability=int(input("""
    ########################################################
    please enter the ability you want to show?
    #1- beginner 2-advanced 3-expert
   ######################################################
   """))
            if ability > 0 and ability <= 3:
                valid=True
            else:
                print("invalid. choose group 1,2 or 3")
        except:
                print("invalid. choose group 1,2 or 3")

    if ability == 1:
        print("beginner skiers list")
        for i in range(0, len(first_name)):
                       if abilityscore[i] >20:
                           print(first_name[i],surname[i],abilityscore[i])

    elif ability ==2:
        print("intermediate skiers list")
        for i in range(0, len(first_name)):
                    if abilityscore[i] >10 and abilityscore[i] <= 20:
                        print(first_name[i],surname[i],abilityscore[i])

    else:
        print("expert skiers list")
        for i in range(0, len(first_name)):
                       if abilityscore[i] <=10:
                           print(first_name[i],surname[i],abilityscore[i])
                       

                     
#main program   
login()

valid= True
while valid == True:
    menu_options=main_menu()
    if menu_options == "A":
        newstudent()
        skitimes()
        ski_quiz()
    elif menu_options == "B":
        option=groups()
        read_details()
        if  option=="A":
            reportA()
        elif option=="B":
            reportB()
        elif option=="C":
            reportC()
        elif option=="D":
            reportD()
        elif option=="E":
            exit()                   
    else:
        exit()

