#KEVIN AHMADIPUTRA
#TP058396

#MAIN MENU [def main_menu():]
def main_menu():
    print ("\n\n\t***REAL CHAMPION SPORT ACADEMY SYSTEM (RCSAS)***\n\nUser Type :\n1. Admin\n2. Student\n3. Exit")
    user_type = int(input("Enter User Type : "))
    while (user_type > 3 or user_type < 1):
        user_type = int(input("\nWrong User Type !!!\nEnter User Type : "))
    if(user_type == 1):
        admin_login()
    elif(user_type == 2):
        ps_menu()
    else:
        exit()

#Login to Admin System [def admin_login():]  [ADD ADMIN USERNAME & PASSWORD FROM TXT FILE]
def admin_login():
    print("\n\n\t***Welcome to Admin System***\n\nAdmin System Option :\n1. Login\n2. Back to Main Menu\n3. Exit")
    adminsystem_opt = int(input("Enter your Option : "))
    while (adminsystem_opt > 3 or adminsystem_opt < 1):
        adminsystem_opt = int(input("\nWrong Option !!!\nEnter Your Option : "))
    if(adminsystem_opt == 1):
        adminfile = open("Admin_user_pass.txt","r")
        adminlist = []
        for line in adminfile:
            line = line.strip()
            line = line.split("\t")
            adminlist.append(line)
        adminfile.close()
        admin_cnt = len(adminlist)
        ad_x = 0
        ad_flag = 0
        admin_user = input("\nAdmin's Username : ")
        admin_pass = input("Admin's Password : ")
        for i in range(admin_cnt):
            if(admin_user in adminlist[0+ad_x] and admin_pass in adminlist[0+ad_x]):
                ad_flag = 1
            ad_x = ad_x + 1
        if(ad_flag == 1):
            admin_menu()
        else:
            adminwrong_opt = int(input("\nAccount Error !!!\nWrong Username nor Password !!!\nEnter '0' to Try Again or 'ANY NUMBER' to Main Menu : "))
            if (adminwrong_opt == 0):
                admin_login()
            else:
                main_menu()
    elif(adminsystem_opt == 2):
        main_menu()
    else:
        exit()
    
#Functionalities of Admin [def admin_menu():]
def admin_menu():
    print("\n\nAdmin's Functionalities :\n1. Add Records\n2. Display Records\n3. Search Specific Records\n4. Sort and Display Records\n5. Modify Record\n6. Main Menu\n7. Exit")
    adminfunc_opt = int(input("Enter Functionalities Option : "))
    while(adminfunc_opt < 1 or adminfunc_opt > 7):
        adminfunc_opt = int(input("\nWrong Option !!!\nEnter Functionalities Option : "))
    if(adminfunc_opt == 1):
        admin_f1()
    elif(adminfunc_opt == 2):
        admin_f2()
    elif(adminfunc_opt == 3):
        admin_f3()
    elif(adminfunc_opt == 4):
        admin_f4()
    elif(adminfunc_opt == 5):
        admin_f5()
    elif(adminfunc_opt == 6):
        main_menu()
    else:
        exit()


#Admin F1 = Add Record [def admin_f1():]
def admin_f1():
    code1 = "CC" #For Coach ID
    code2 = "LC" #For Sport Center Code.    Sport Center Code [Branch A = 1, Branch B = 2, and Branch C = 3]
    code3 = "SP" #For Sport Code. 
    code4 = "RM" #For Money.
    code6 = "DL" #For Sport Schedule
    ssname1 = "Branch A"
    ssname2 = "Branch B"
    ssname3 = "Branch C"
    print("\n\n\t***Admin's Functionalities - Add Record***\n\nRecords Option :\n1. Coach\n2. Sport\n3. Sport Schedule\n4. Admin Functionalities Menu")
    adminf1_opt = int(input("Enter Your Option : "))
    while (adminf1_opt > 4 or adminf1_opt < 1):
        adminf1_opt = int(input("\nWrong Option !!!\nEnter Your Option : "))
    if(adminf1_opt == 1):
        print("\n\nSport Center :\n1. Sport Center Branch A\n2. Sport Center Branch B\n3. Sport Center Branch C")
        ss_opt = int(input("Enter Choosen Sport Center : "))
        while (ss_opt > 3 or ss_opt < 1):
            ss_opt = int(input("\nWrong Option !!!\nEnter Choosen Sport Center : "))
        if(ss_opt == 1):
            import os
            filesize = os.path.getsize("Sport_Center_BranchA_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sport Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            coach_number = int(input("\n\n\t***Sport Center Branch A***\n\nEnter the Number of Coach : "))
            for cnt in range (coach_number):
                ssfileall_coach = open("All_Sport_Center_Coach.txt","a")
                ss1file1 = open("Sport_Center_BranchA_Coach.txt","a")
                cofile = open("All_Sport_Center_Coach.txt","r")
                co_idcheck = []
                for line in cofile:
                    line = line.strip()
                    line = line.split("\t")
                    co_idcheck.append(line[0])
                cofile.close()
                print("Used Coach ID : ")
                print(co_idcheck)
                co_id = input("\nCoach Number "+str(cnt+1)+"\n\nRange of ID is 100 - 999 !!!\nWithout CC (Just Number)\nEnter Coach ID\t\t\t\t: ")
                while (int(co_id) > 999 or int(co_id) < 100 or code1+co_id in co_idcheck):
                    co_id = input("\nWrong Input or Coach ID Exist !!!\nRange of ID is 100 - 999 !!!\nWithout CC (Just Number)\nEnter Coach ID\t\t\t\t: ")
                co_nm = input("Enter Coach Name\t\t\t: ")
                co_dj = input("Enter Coach Joined Date (dd/MM/yy)\t: ")
                co_td = input("Enter Coach Terminated Date (dd/MM/yy)\t: ")
                co_ph = input("Enter Coach Phone Number\t\t: ")
                co_ad = input("Enter Coach Address\t\t\t: ")
                print("\nCode for Sport Center :\nSport Center Branch A = 1\nSport Center Branch B = 2\nSport Center Branch C = 3")
                co_scc = str(1)
                print("\nEnter Coach Sport Center Code\t\t: "+co_scc)
                co_scn = ssname1
                print("Enter Coach Sport Center Name\t\t: "+co_scn+"\n")

                cofile1 = open("Sport_Center_BranchA_Sports.txt","r")
                colist1 = []
                
                for line in cofile1:
                    line = line.strip()
                    line = line.split("\t")
                    colist1.append(line[0])
                    colist1.append(line[1])
                    colist1.append(line[2])
                print("\nAvailable Sport ID, Sport Name, Hourly Rate : ")
                print(colist1)
                cofile1.close()
                cocnt = len(colist1)
                co_x = 0
                co_sc = input("\nWITHOUT 'SP' (Just Number)!!!\nEnter Coach Sport Code\t\t\t: ")
                while (code3+co_sc not in colist1):
                    co_sc_try = int(input ("\nWrong Input or Record not Exist !!!\nAdd 'Sport Code' Record in Sport Record First :)\nEnter '0' to Try Again or 'ANY NUMBER' to Admin Func Menu : "))
                    if(co_sc_try == 0):
                        co_sc = input ("\nEnter Coach Sport Code\t\t\t: ")
                    else:
                        admin_menu()
                for i in range (cocnt):
                    if(code3+co_sc == colist1[0+co_x]):
                        co_sn = colist1[1+co_x]
                        co_hr = colist1[2+co_x]
                    co_x = co_x + 1
                print("Enter Coach Sport Name\t\t\t: "+co_sn+"\nEnter Coach Hourly Rate\t\t\t: "+co_hr)
                co_rt = int(input("Enter Coach Rating\t\t\t: "))
                while(co_rt != 0):
                    co_rt = int(input("\nFirst Rating (Before Student Give Rating) is 0\nEnter Coach Rating\t\t\t: "))
                ssfileall_coach.write(code1+co_id+"\t"+co_nm+"\t"+co_dj+"\t"+co_td+"\t"+co_hr+"\t"+co_ph+"\t"+co_ad+"\t"+code2+co_scc+"\t"+co_scn+"\t"+code3+str(co_sc)+"\t"+co_sn+"\t"+str(co_rt)+"\n")
                ss1file1.write(code1+str(co_id)+"\t"+co_nm+"\t"+co_dj+"\t"+co_td+"\t"+co_hr+"\t"+co_ph+"\t"+co_ad+"\t"+code2+co_scc+"\t"+co_scn+"\t"+code3+str(co_sc)+"\t"+co_sn+"\t"+str(co_rt)+"\n")
                ssfileall_coach.close()
                ss1file1.close()
            admin_f1()

        elif(ss_opt == 2):
            import os
            filesize = os.path.getsize("Sport_Center_BranchB_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sport Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            coach_number = int(input("\n\n\t***Sport Center Branch B***\n\nEnter the Number of Coach : "))
            for cnt in range (coach_number):
                ssfileall_coach = open("All_Sport_Center_Coach.txt","a")
                ss2file1 = open("Sport_Center_BranchB_Coach.txt","a")
                cofile = open("All_Sport_Center_Coach.txt","r")
                co_idcheck = []
                for line in cofile:
                    line = line.strip()
                    line = line.split("\t")
                    co_idcheck.append(line[0])
                cofile.close()
                print("Used Coach ID : ")
                print(co_idcheck)
                co_id = input("\nCoach Number "+str(cnt+1)+"\n\nRange of ID is 100 - 999 !!!\nWithout CC (Just Number)\nEnter Coach ID\t\t\t\t: ")
                while (int(co_id) > 999 or int(co_id) < 100 or code1+co_id in co_idcheck):
                    co_id = input("\nWrong Input or Coach ID Exist !!!\nRange of ID is 100 - 999 !!!\nWithout CC (Just Number)\nEnter Coach ID\t\t\t\t: ")
                co_nm = input("Enter Coach Name\t\t\t: ")
                co_dj = input("Enter Coach Joined Date (dd/MM/yy)\t: ")
                co_td = input("Enter Coach Terminated Date (dd/MM/yy)\t: ")
                co_ph = input("Enter Coach Phone Number\t\t: ")
                co_ad = input("Enter Coach Address\t\t\t: ")
                print("\nCode for Sport Center :\nSport Center Branch A = 1\nSport Center Branch B = 2\nSport Center Branch C = 3")
                co_scc = str(2)
                print("\nEnter Coach Sport Center Code\t\t: "+co_scc)
                co_scn = ssname2
                print("Enter Coach Sport Center Name\t\t: "+co_scn+"\n")
                
                cofile1 = open("Sport_Center_BranchB_Sports.txt","r")
                colist1 = []
                for line in cofile1:
                    line = line.strip()
                    line = line.split("\t")
                    colist1.append(line[0])
                    colist1.append(line[1])
                    colist1.append(line[2])
                print("\nAvailable Sport ID, Sport Name, Hourly Rate : ")
                print(colist1)
                cofile1.close()
                cocnt = len(colist1)
                co_x = 0
                co_sc = input("\nWITHOUT 'SP' (Just Number)!!!\nEnter Coach Sport Code\t\t\t: ")
                while (code3+co_sc not in colist1):
                    co_sc_try = int(input ("\nWrong Input or Record not Exist !!!\nAdd 'Sport Code' Record in Sport Record First :)\nEnter '0' to Try Again or 'ANY NUMBER' to Admin Func Menu : "))
                    if(co_sc_try == 0):
                        co_sc = input ("\nEnter Coach Sport Code\t\t\t: ")
                    else:
                        admin_menu()
                for i in range (cocnt):
                    if(code3+co_sc == colist1[0+co_x]):
                        co_sn = colist1[1+co_x]
                        co_hr = colist1[2+co_x]
                    co_x = co_x + 1
                print("Enter Coach Sport Name\t\t\t: "+co_sn+"\nEnter Coach Hourly Rate\t\t\t: "+co_hr)
                co_rt = int(input("Enter Coach Rating\t\t\t: "))
                while(co_rt != 0):
                    co_rt = int(input("\nFirst Rating (Before Student Give Rating) is 0\nEnter Coach Rating\t\t\t: "))
                ssfileall_coach.write(code1+co_id+"\t"+co_nm+"\t"+co_dj+"\t"+co_td+"\t"+co_hr+"\t"+co_ph+"\t"+co_ad+"\t"+code2+co_scc+"\t"+co_scn+"\t"+code3+str(co_sc)+"\t"+co_sn+"\t"+str(co_rt)+"\n")
                ss2file1.write(code1+str(co_id)+"\t"+co_nm+"\t"+co_dj+"\t"+co_td+"\t"+co_hr+"\t"+co_ph+"\t"+co_ad+"\t"+code2+co_scc+"\t"+co_scn+"\t"+code3+str(co_sc)+"\t"+co_sn+"\t"+str(co_rt)+"\n")
                ssfileall_coach.close()
                ss2file1.close()
            admin_f1()

        else:
            import os
            filesize = os.path.getsize("Sport_Center_BranchC_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sport Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            coach_number = int(input("\n\n\t***Sport Center Branch C***\n\nEnter the Number of Coach : "))
            for cnt in range (coach_number):
                ssfileall_coach = open("All_Sport_Center_Coach.txt","a")
                ss3file1 = open("Sport_Center_BranchC_Coach.txt","a")
                cofile = open("All_Sport_Center_Coach.txt","r")
                co_idcheck = []
                for line in cofile:
                    line = line.strip()
                    line = line.split("\t")
                    co_idcheck.append(line[0])
                cofile.close()
                print("Used Coach ID : ")
                print(co_idcheck)
                co_id = input("\nCoach Number "+str(cnt+1)+"\n\nRange of ID is 100 - 999 !!!\nWithout CC (Just Number)\nEnter Coach ID\t\t\t\t: ")
                while (int(co_id) > 999 or int(co_id) < 100 or code1+co_id in co_idcheck):
                    co_id = input("\nWrong Input or Coach ID Exist !!!\nRange of ID is 100 - 999 !!!\nWithout CC (Just Number)\nEnter Coach ID\t\t\t\t: ")
                co_nm = input("Enter Coach Name\t\t\t: ")
                co_dj = input("Enter Coach Joined Date (dd/MM/yy)\t: ")
                co_td = input("Enter Coach Terminated Date (dd/MM/yy)\t: ")
                co_ph = input("Enter Coach Phone Number\t\t: ")
                co_ad = input("Enter Coach Address\t\t\t: ")
                print("\nCode for Sport Center :\nSport Center Branch A = 1\nSport Center Branch B = 2\nSport Center Branch C = 3")
                co_scc = str(3)
                print("\nEnter Coach Sport Center Code\t\t: "+co_scc)
                co_scn = ssname3
                print("Enter Coach Sport Center Name\t\t: "+co_scn+"\n")
                
                cofile1 = open("Sport_Center_BranchC_Sports.txt","r")
                colist1 = []
                for line in cofile1:
                    line = line.strip()
                    line = line.split("\t")
                    colist1.append(line[0])
                    colist1.append(line[1])
                    colist1.append(line[2])
                print("\nAvailable Sport ID, Sport Name, Hourly Rate : ")
                print(colist1)
                cofile1.close()
                cocnt = len(colist1)
                co_x = 0
                co_sc = input("\nWITHOUT 'SP' (Just Number)!!!\nEnter Coach Sport Code\t\t\t: ")
                while (code3+co_sc not in colist1):
                    co_sc_try = int(input ("\nWrong Input or Record not Exist !!!\nAdd 'Sport Code' Record in Sport Record First :)\nEnter '0' to Try Again or 'ANY NUMBER' to Admin Func Menu : "))
                    if(co_sc_try == 0):
                        co_sc = input ("\nEnter Coach Sport Code\t\t\t: ")
                    else:
                        admin_menu()
                for i in range (cocnt):
                    if(code3+co_sc == colist1[0+co_x]):
                        co_sn = colist1[1+co_x]
                        co_hr = colist1[2+co_x]
                    co_x = co_x + 1
                print("Enter Coach Sport Name\t\t\t: "+co_sn+"\nEnter Coach Hourly Rate\t\t\t: "+co_hr)
                co_rt = int(input("Enter Coach Rating\t\t\t: "))
                while(co_rt != 0):
                    co_rt = int(input("\nFirst Rating (Before Student Give Rating) is 0\nEnter Coach Rating\t\t\t: "))
                ssfileall_coach.write(code1+co_id+"\t"+co_nm+"\t"+co_dj+"\t"+co_td+"\t"+co_hr+"\t"+co_ph+"\t"+co_ad+"\t"+code2+co_scc+"\t"+co_scn+"\t"+code3+str(co_sc)+"\t"+co_sn+"\t"+str(co_rt)+"\n")
                ss3file1.write(code1+str(co_id)+"\t"+co_nm+"\t"+co_dj+"\t"+co_td+"\t"+co_hr+"\t"+co_ph+"\t"+co_ad+"\t"+code2+co_scc+"\t"+co_scn+"\t"+code3+str(co_sc)+"\t"+co_sn+"\t"+str(co_rt)+"\n")
                ssfileall_coach.close()
                ss3file1.close()
            admin_f1()

    elif(adminf1_opt == 2):
        print("\n\nSport Center :\n1. Sport Center Branch A\n2. Sport Center Branch B\n3. Sport Center Branch C")
        ss_opt = int(input("Enter Choosen Sport Center : "))
        while (ss_opt > 3 or ss_opt < 1):
            ss_opt = int(input("\nWrong Option !!!\nEnter Choosen Sport Center : "))
        if(ss_opt == 1):
            sport_number = int(input("\n\n\t***Sport Center Branch A***\n\nEnter the Number of Sport : "))
            for cnt in range (sport_number):
                ssfileall_sport = open("All_Sport_Center_Sports.txt","a")
                ss1file2 = open("Sport_Center_BranchA_Sports.txt","a")
                sp_scn = ssname1
                sp_scc = str(1)
                print("\nSport Number "+str(cnt+1)+"\nEnter Sport Center Code\t\t: "+sp_scc+"\nEnter Sport Location\t\t: "+sp_scn)
                spfile = open("All_Sport_Center_Sports.txt","r")
                spfile1 = open("Sport_Center_BranchA_Sports.txt","r")
                splist = []
                splist1 = []
                for line in spfile:
                    line = line.strip()
                    line = line.split("\t")
                    splist.append(line[0])
                    splist.append(line[1])
                    splist.append(line[2])
                for line in spfile1:
                    line = line.strip()
                    line = line.split("\t")
                    splist1.append(line[0])
                    splist1.append(line[1])
                    splist1.append(line[2])
                spfile.close()
                spfile1.close()
                #print(splist)
                #print(splist1)
                sp_cnt = len(splist)
                sp_x = 0
                sp_cd = input("\nWITHOUT 'SP' (Just Number) !!!\nRange 100 - 999 !!!\nEnter Sport Code\t\t: ")
                while (int(sp_cd)>999 or int(sp_cd)<100):
                    sp_cd = input("\nNot in Range !!!\nEnter Sport Code\t\t: ")
                if(code3+sp_cd in splist and code3+sp_cd not in splist1):
                    for i in range (sp_cnt):
                        if(code3+sp_cd == splist[0+sp_x]):
                            sp_nm = splist[1+sp_x]
                            sp_hr = splist[2+sp_x]
                        sp_x = sp_x + 1
                    print("\nEnter Aport Name\t\t: ",sp_nm)
                    print("Enter Sport Hourly Rate\t\t: ",sp_hr)
                    ss1file2.write(code3+sp_cd+"\t"+sp_nm+"\t"+sp_hr+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                elif(code3+sp_cd not in splist and code2+sp_cd in splist1):
                    print("Available Sport to add : ")
                    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
                    print(sp_namelist)
                    sp_nm = input("\nEnter Sport Name\t\t: ")
                    while(sp_nm not in sp_namelist or sp_nm in splist ):
                        sp_nm = input("\nWrong Option or Sport Name Exist!!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Sport Name\t\t: ")
                    sp_hr = int(input("\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    while (sp_hr > 500 or sp_hr < 100):
                        sp_hr = int(input("\nNot in Range !!!\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    ssfileall_sport.write(code3+sp_cd+"\t"+sp_nm+"t"+code4+str(sp_hr)+"\t"+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                elif(code3+sp_cd not in splist and code2+sp_cd not in splist1):
                    print("Available Sport to add : ")
                    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
                    print(sp_namelist)
                    sp_nm = input("\nEnter Sport Name\t\t: ")
                    while(sp_nm not in sp_namelist or sp_nm in splist):
                        sp_nm = input("\nWrong Option or Sport Name Exist!!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Sport Name\t\t: ")
                    sp_hr = int(input("\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    while (sp_hr > 500 or sp_hr < 100):
                        sp_hr = int(input("\nNot in Range !!!\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    ss1file2.write(code3+sp_cd+"\t"+sp_nm+"\t"+code4+str(sp_hr)+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                    ssfileall_sport.write(code3+sp_cd+"\t"+sp_nm+"\t"+code4+str(sp_hr)+"\t"+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                else:
                    print("Records Exist !!!\nThe Record will not Saved:) ")
                    
                ssfileall_sport.close()
                ss1file2.close()
            admin_f1()
            
                    
        elif(ss_opt == 2):
            sport_number = int(input("\n\n\t***Sport Center Branch B***\n\nEnter the Number of Sport : "))
            for cnt in range (sport_number):
                ssfileall_sport = open("All_Sport_Center_Sports.txt","a")
                ss2file2 = open("Sport_Center_BranchB_Sports.txt","a")
                sp_scn = ssname2
                sp_scc = str(2)
                print("\nSport Number "+str(cnt+1)+"\nEnter Sport Center Code\t\t: "+sp_scc+"\nEnter Sport Location\t\t: "+sp_scn)
                spfile = open("All_Sport_Center_Sports.txt","r")
                spfile1 = open("Sport_Center_BranchB_Sports.txt","r")
                splist = []
                splist1 = []
                for line in spfile:
                    line = line.strip()
                    line = line.split("\t")
                    splist.append(line[0])
                    splist.append(line[1])
                    splist.append(line[2])
                for line in spfile1:
                    line = line.strip()
                    line = line.split("\t")
                    splist1.append(line[0])
                    splist1.append(line[1])
                    splist1.append(line[2])
                spfile.close()
                spfile1.close()
                #print(splist)
                #print(splist1)
                sp_cnt = len(splist)
                sp_x = 0
                sp_cd = input("\nWITHOUT 'SP' (Just Number) !!!\nRange 100 - 999 !!!\nEnter Sport Code\t\t: ")
                while (int(sp_cd)>999 or int(sp_cd)<100):
                    sp_cd = input("\nNot in Range !!!\nEnter Sport Code\t\t: ")
                if(code3+sp_cd in splist and code3+sp_cd not in splist1):
                    for i in range (sp_cnt):
                        if(code3+sp_cd == splist[0+sp_x]):
                            sp_nm = splist[1+sp_x]
                            sp_hr = splist[2+sp_x]
                        sp_x = sp_x + 1
                    print("\nEnter Aport Name\t\t: ",sp_nm)
                    print("Enter Sport Hourly Rate\t\t: ",sp_hr)
                    ss2file2.write(code3+sp_cd+"\t"+sp_nm+"\t"+sp_hr+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                elif(code3+sp_cd not in splist and code2+sp_cd in splist1):
                    print("Available Sport to add : ")
                    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
                    print(sp_namelist)
                    sp_nm = input("\nEnter Sport Name\t\t: ")
                    while(sp_nm not in sp_namelist or sp_nm in splist):
                        sp_nm = input("\nWrong Option or Sport Name Exist!!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Sport Name\t\t: ")
                    sp_hr = int(input("\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    while (sp_hr > 500 or sp_hr < 100):
                        sp_hr = int(input("\nNot in Range !!!\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    ssfileall_sport.write(code3+sp_cd+"\t"+sp_nm+"t"+code4+str(sp_hr)+"\t"+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                elif(code3+sp_cd not in splist and code2+sp_cd not in splist1):
                    print("Available Sport to add : ")
                    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
                    print(sp_namelist)
                    sp_nm = input("\nEnter Sport Name\t\t: ")
                    while(sp_nm not in sp_namelist or sp_nm in splist):
                        sp_nm = input("\nWrong Option or Sport Name Exist!!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Sport Name\t\t: ")
                    sp_hr = int(input("\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    while (sp_hr > 500 or sp_hr < 100):
                        sp_hr = int(input("\nNot in Range !!!\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    ss2file2.write(code3+sp_cd+"\t"+sp_nm+"\t"+code4+str(sp_hr)+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                    ssfileall_sport.write(code3+sp_cd+"\t"+sp_nm+"\t"+code4+str(sp_hr)+"\t"+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                else:
                    print("Records Exist !!!\nThe Record will not Saved:) ")
                    
                ssfileall_sport.close()
                ss2file2.close()
            admin_f1()

        else:
            sport_number = int(input("\n\n\t***Sport Center Branch C***\n\nEnter the Number of Sport : "))
            for cnt in range (sport_number):
                ssfileall_sport = open("All_Sport_Center_Sports.txt","a")
                ss3file2 = open("Sport_Center_BranchC_Sports.txt","a")
                sp_scn = ssname3
                sp_scc = str(3)
                print("\nSport Number "+str(cnt+1)+"\nEnter Sport Center Code\t\t: "+sp_scc+"\nEnter Sport Location\t\t: "+sp_scn)
                spfile = open("All_Sport_Center_Sports.txt","r")
                spfile1 = open("Sport_Center_BranchC_Sports.txt","r")
                splist = []
                splist1 = []
                for line in spfile:
                    line = line.strip()
                    line = line.split("\t")
                    splist.append(line[0])
                    splist.append(line[1])
                    splist.append(line[2])
                for line in spfile1:
                    line = line.strip()
                    line = line.split("\t")
                    splist1.append(line[0])
                    splist1.append(line[1])
                    splist1.append(line[2])
                spfile.close()
                spfile1.close()
                #print(splist)
                #print(splist1)
                sp_cnt = len(splist)
                sp_x = 0
                sp_cd = input("\nWITHOUT 'SP' (Just Number) !!!\nRange 100 - 999 !!!\nEnter Sport Code\t\t: ")
                while (int(sp_cd)>999 or int(sp_cd)<100):
                    sp_cd = input("\nNot in Range !!!\nEnter Sport Code\t\t: ")
                if(code3+sp_cd in splist and code3+sp_cd not in splist1):
                    for i in range (sp_cnt):
                        if(code3+sp_cd == splist[0+sp_x]):
                            sp_nm = splist[1+sp_x]
                            sp_hr = splist[2+sp_x]
                        sp_x = sp_x + 1
                    print("\nEnter Aport Name\t\t: ",sp_nm)
                    print("Enter Sport Hourly Rate\t\t: ",sp_hr)
                    ss3file2.write(code3+sp_cd+"\t"+sp_nm+"\t"+sp_hr+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                elif(code3+sp_cd not in splist and code2+sp_cd in splist1):
                    print("Available Sport to add : ")
                    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
                    print(sp_namelist)
                    sp_nm = input("\nEnter Sport Name\t\t: ")
                    while(sp_nm not in sp_namelist or sp_nm in splist):
                        sp_nm = input("\nWrong Option or Sport Name Exist!!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Sport Name\t\t: ")
                    sp_hr = int(input("\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    while (sp_hr > 500 or sp_hr < 100):
                        sp_hr = int(input("\nNot in Range !!!\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    ssfileall_sport.write(code3+sp_cd+"\t"+sp_nm+"t"+code4+str(sp_hr)+"\t"+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                elif(code3+sp_cd not in splist and code2+sp_cd not in splist1):
                    print("Available Sport to add : ")
                    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
                    print(sp_namelist)
                    sp_nm = input("\nEnter Sport Name\t\t: ")
                    while(sp_nm not in sp_namelist or sp_nm in splist):
                        sp_nm = input("\nWrong Option or Sport Name Exist!!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Sport Name\t\t: ")
                    sp_hr = int(input("\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    while (sp_hr > 500 or sp_hr < 100):
                        sp_hr = int(input("\nNot in Range !!!\nHourly Rate Range 100 to 500\nEnter Sport Hourly Rate\t\t: "))
                    ss3file2.write(code3+sp_cd+"\t"+sp_nm+"\t"+code4+str(sp_hr)+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                    ssfileall_sport.write(code3+sp_cd+"\t"+sp_nm+"\t"+code4+str(sp_hr)+"\t"+"\t"+code2+sp_scc+"\t"+sp_scn+"\n")
                else:
                    print("Records Exist !!!\nThe Record will not Saved:) ")
                    
                ssfileall_sport.close()
                ss3file2.close()
            admin_f1()
            
    elif(adminf1_opt == 3):
        print("\n\nSport Center :\n1. Sport Center Branch A\n2. Sport Center Branch B\n3. Sport Center Branch C")
        ss_opt = int(input("Enter Choosen Sport Center : "))
        while (ss_opt > 3 or ss_opt < 1):
            ss_opt = int(input("\nWrong Option !!!\nEnter Choosen Sport Center : "))
        if(ss_opt == 1):
            import os
            filesize = os.path.getsize("Sport_Center_BranchA_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            schedule_number = int(input("\n\n\t***Sport Center Branch A***\n\nEnter the Number of Schedule : "))
            for cnt in range (schedule_number):
                ssfileall_schedule = open("All_Sport_Center_Schedule.txt","a")
                ss1file3 = open("Sport_Center_BranchA_Schedule.txt","a")
                sc_scc = str(1)
                sc_scn = ssname1
                print("\nSchedule Number "+str(cnt+1)+"\nEnter Sport Center Code\t\t\t:",sc_scc)
                print("Enter Sport Center Location\t\t:",sc_scn)
                scfile = open ("Sport_Center_BranchA_Coach.txt","r")
                sclist = []
                for line in scfile :
                    line = line.strip()
                    line = line.split("\t")
                    sclist.append(line[0])
                    sclist.append(line[1])
                    sclist.append(line[10])
                print("\nAvailable Coach ID, Coach Name, Sport Name : ")
                print(sclist)
                scfile.close()
                sc_cnt = len(sclist)
                sc_x = 0
                sc_coid = input("\nWITHOUT 'CC' (Just Number) !!!\nEnter Coach ID\t\t\t\t: ")
                while (code1+sc_coid not in sclist):
                    sc_coid = input("\nCoach ID not Exist !!!\nWITHOUT 'CC' (Just Number) !!!\nEnter Coach ID\t\t\t\t: ")
                for i in range (sc_cnt):
                    if(code1+sc_coid == sclist[0+sc_x]):
                        sc_cn = sclist[1+sc_x]
                        sc_sn = sclist[2+sc_x]
                    sc_x = sc_x + 1
                print("Enter Coach Name\t\t\t:",sc_cn)
                print("Enter Sport Name\t\t\t:",sc_sn)
                sc_tm = input("Enter Time (dd/MM/yy/hh:mm - hh:mm)\t: ")
                scfile2 = open("All_Sport_Center_Schedule.txt","r")
                sclist2 = []
                for line in scfile2:
                    line = line.strip()
                    line = line.split("\t")
                    sclist2.append(line[0])
                print("Used Schedule ID : ")
                print(sclist2)
                scfile2.close()
                scnum = input("\nWITHOUT 'DL' (JUST NUMBER) !!!\nRange is 100 - 999\nEnter Schedule ID : ")
                while(int(scnum)>999 or int(scnum)<100 or code6+scnum in sclist2):
                    scnum = input("\nWrong Input or Schedule ID Exist !!!\nWITHOUT 'DL' (JUST NUMBER) !!!\nRange is 100 - 999\nEnter Schedule ID : ")
                ssfileall_schedule.write(code6+scnum+"\t"+code1+sc_coid+"\t"+sc_cn+"\t"+sc_sn+"\t"+code2+sc_scc+"\t"+sc_scn+"\t"+sc_tm+"\n")
                ss1file3.write(code6+scnum+"\t"+code1+sc_coid+"\t"+sc_cn+"\t"+sc_sn+"\t"+code2+sc_scc+"\t"+sc_scn+"\t"+sc_tm+"\n")
                ssfileall_schedule.close()
                ss1file3.close()
            admin_f1()

        elif (ss_opt == 2):
            import os
            filesize = os.path.getsize("Sport_Center_BranchB_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            schedule_number = int(input("\n\n\t***Sport Center Branch B***\n\nEnter the Number of Schedule : "))
            for cnt in range (schedule_number):
                ssfileall_schedule = open("All_Sport_Center_Schedule.txt","a")
                ss2file3 = open("Sport_Center_BranchB_Schedule.txt","a")
                sc_scc = str(2)
                sc_scn = ssname2
                print("\nSchedule Number "+str(cnt+1)+"\nEnter Sport Center Code\t\t\t:",sc_scc)
                print("Enter Sport Center Location\t\t:",sc_scn)
                scfile = open ("Sport_Center_BranchB_Coach.txt","r")
                sclist = []
                for line in scfile :
                    line = line.strip()
                    line = line.split("\t")
                    sclist.append(line[0])
                    sclist.append(line[1])
                    sclist.append(line[10])
                print("\nAvailable Coach ID, Coach Name, Sport Name : ")
                print(sclist)
                scfile.close()
                sc_cnt = len(sclist)
                sc_x = 0
                sc_coid = input("\nWITHOUT 'CC' (Just Number) !!!\nEnter Coach ID\t\t\t\t: ")
                while (code1+sc_coid not in sclist):
                    sc_coid = input("\nCoach ID not Exist !!!\nWITHOUT 'CC' (Just Number) !!!\nEnter Coach ID\t\t\t\t: ")
                for i in range (sc_cnt):
                    if(code1+sc_coid == sclist[0+sc_x]):
                        sc_cn = sclist[1+sc_x]
                        sc_sn = sclist[2+sc_x]
                    sc_x = sc_x + 1
                print("Enter Coach Name\t\t\t:",sc_cn)
                print("Enter Sport Name\t\t\t:",sc_sn)
                sc_tm = input("Enter Time (dd/MM/yy/hh:mm - hh:mm)\t: ")
                scfile2 = open("All_Sport_Center_Schedule.txt","r")
                sclist2 = []
                for line in scfile2:
                    line = line.strip()
                    line = line.split("\t")
                    sclist2.append(line[0])
                print("Used Schedule ID : ")
                print(sclist2)
                scfile2.close()
                scnum = input("\nWITHOUT 'DL' (JUST NUMBER) !!!\nRange is 100 - 999\nEnter Schedule ID : ")
                while(int(scnum)>999 or int(scnum)<100 or code6+scnum in sclist2):
                    scnum = input("\nWrong Input or Schedule ID Exist !!!\nWITHOUT 'DL' (JUST NUMBER) !!!\nRange is 100 - 999\nEnter Schedule ID : ")
                ssfileall_schedule.write(code6+scnum+"\t"+code1+sc_coid+"\t"+sc_cn+"\t"+sc_sn+"\t"+code2+sc_scc+"\t"+sc_scn+"\t"+sc_tm+"\n")
                ss2file3.write(code6+scnum+"\t"+code1+sc_coid+"\t"+sc_cn+"\t"+sc_sn+"\t"+code2+sc_scc+"\t"+sc_scn+"\t"+sc_tm+"\n")
                ssfileall_schedule.close()
                ss2file3.close()
            admin_f1()

        else:
            import os
            filesize = os.path.getsize("Sport_Center_BranchC_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    print("admin menu")#ADMIN FUNC MENU
                else:
                    print("Main mNeu")#MAIN MENU
            schedule_number = int(input("\n\n\t***Sport Center Branch C***\n\nEnter the Number of Schedule : "))
            for cnt in range (schedule_number):
                ssfileall_schedule = open("All_Sport_Center_Schedule.txt","a")
                ss3file3 = open("Sport_Center_BranchC_Schedule.txt","a")
                sc_scc = str(3)
                sc_scn = ssname3
                print("\nSchedule Number "+str(cnt+1)+"\nEnter Sport Center Code\t\t\t:",sc_scc)
                print("Enter Sport Center Location\t\t:",sc_scn)
                scfile = open ("Sport_Center_BranchC_Coach.txt","r")
                sclist = []
                for line in scfile :
                    line = line.strip()
                    line = line.split("\t")
                    sclist.append(line[0])
                    sclist.append(line[1])
                    sclist.append(line[10])
                print("\nAvailable Coach ID,Coach Name, Sport Name : ")
                print(sclist)
                sc_cnt = len(sclist)
                sc_x = 0
                sc_coid = input("\nWITHOUT 'CC' (Just Number) !!!\nEnter Coach ID\t\t\t\t: ")
                while (code1+sc_coid not in sclist):
                    sc_coid = input("\nCoach ID not Exist !!!\nWITHOUT 'CC' (Just Number) !!!\nEnter Coach ID\t\t\t\t: ")
                for i in range (sc_cnt):
                    if(code1+sc_coid == sclist[0+sc_x]):
                        sc_cn = sclist[1+sc_x]
                        sc_sn = sclist[2+sc_x]
                    sc_x = sc_x + 1
                print("Enter Coach Name\t\t\t:",sc_cn)
                print("Enter Sport Name\t\t\t:",sc_sn)
                sc_tm = input("Enter Time (dd/MM/yy/hh:mm - hh:mm)\t: ")
                scfile2 = open("All_Sport_Center_Schedule.txt","r")
                sclist2 = []
                for line in scfile2:
                    line = line.strip()
                    line = line.split("\t")
                    sclist2.append(line[0])
                print("Used Schedule ID : ")
                print(sclist2)
                scfile2.close()
                scnum = input("\nWITHOUT 'DL' (JUST NUMBER) !!!\nRange is 100 - 999\nEnter Schedule ID : ")
                while(int(scnum)>999 or int(scnum)<100 or code6+scnum in sclist2):
                    scnum = input("\nWrong Input or Schedule ID Exist !!!\nWITHOUT 'DL' (JUST NUMBER) !!!\nRange is 100 - 999\nEnter Schedule ID : ")
                ssfileall_schedule.write(code6+scnum+"\t"+code1+sc_coid+"\t"+sc_cn+"\t"+sc_sn+"\t"+code2+sc_scc+"\t"+sc_scn+"\t"+sc_tm+"\n")
                ss3file3.write(code6+scnum+"\t"+code1+sc_coid+"\t"+sc_cn+"\t"+sc_sn+"\t"+code2+sc_scc+"\t"+sc_scn+"\t"+sc_tm+"\n")
                ssfileall_schedule.close()
                ss3file3.close()
            admin_f1()
    else:
        admin_menu()
           


#ADMIN FUNC 2 - DISPLAY RECORD [def admin_f2():]
def admin_f2():    
    print("\n\n\t***Admin's Functionalities - 'Display Record'***\n\nRecord Option :\n1. Coach\n2. Sport\n3. Registered Students\n4. Admin Functionalities Menu")
    adminf2_opt =int(input("Enter Your Option : "))
    while (adminf2_opt > 4 or adminf2_opt < 1):
        adminf2_opt =int(input("Wrong Option !!!\nRe-enter Your Option : "))
    if(adminf2_opt == 1):
        print("\n\nSport Center :\n1. Sport Center 1\n2. Sport Center 2\n3. Sport Center 3\n4. All Sport Center")
        ss_no = int(input("Enter Choosen Sport Center : "))
        while(ss_no > 4 or ss_no < 1):
            ss_no = int(input("\nWrong Choice !!!\nEnter Choosen Sport Center : "))
        if(ss_no == 1):
            import os
            filesize = os.path.getsize("Sport_Center_BranchA_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            dcofile = open("Sport_Center_BranchA_Coach.txt","r")
            dcolist = []
            for line in dcofile:
                line = line.strip()
                line = line.split("\t")
                dcolist.append(line)
            dcofile.close()
            #print(dcolist)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1
            dcox = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dcox == 0):
                admin_f2()
            else:
                main_menu()

        elif(ss_no == 2):
            import os
            filesize = os.path.getsize("Sport_Center_BranchB_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            dcofile = open("Sport_Center_BranchB_Coach.txt","r")
            dcolist = []
            for line in dcofile:
                line = line.strip()
                line = line.split("\t")
                dcolist.append(line)
            dcofile.close()
            #print(dcolist)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1
            dcox = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dcox == 0):
                admin_f2()
            else:
                main_menu()

        elif(ss_no == 3):
            import os
            filesize = os.path.getsize("Sport_Center_BranchC_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            dcofile = open("Sport_Center_BranchC_Coach.txt","r")
            dcolist = []
            for line in dcofile:
                line = line.strip()
                line = line.split("\t")
                dcolist.append(line)
            dcofile.close()
            #print(dcolist)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1
            dcox = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dcox == 0):
                admin_f2()
            else:
                main_menu()

        else:
            import os
            filesize = os.path.getsize("All_Sport_Center_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            dcofile = open("All_Sport_Center_Coach.txt","r")
            dcolist = []
            for line in dcofile:
                line = line.strip()
                line = line.split("\t")
                dcolist.append(line)
            dcofile.close()
            #print(dcolist)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1
            dcox = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dcox == 0):
                admin_f2()
            else:
                main_menu()
            
    elif(adminf2_opt == 2):
        print("\n\nSport Center :\n1. Sport Center 1\n2. Sport Center 2\n3. Sport Center 3")
        ss_no = int(input("Enter Choosen Sport Center : "))
        while(ss_no > 3 or ss_no < 1):
            ss_no = int(input("\nWrong Choice !!!\nEnter Choosen Sport Center : "))
        if(ss_no == 1):
            import os
            filesize = os.path.getsize("Sport_Center_BranchA_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sports Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            dspfile = open("Sport_Center_BranchA_Sports.txt","r")
            dsplist = []
            for line in dspfile:
                line = line.strip()
                line = line.split("\t")
                dsplist.append(line)
            dspfile.close()
            #print(dsplist)
            dsp_cnt = len(dsplist)
            dsp_x = 0
            for i in range(dsp_cnt):
                print("\nSport Number "+str(dsp_x+1)+"\nSport Code\t\t\t: ",dsplist[0+dsp_x][0])
                print("Sport Name\t\t\t: ",dsplist[0+dsp_x][1])
                print("Sport Hourly Rate\t\t: ",dsplist[0+dsp_x][2])
                print("Sport's Sport Center Code\t: ",dsplist[0+dsp_x][3])
                print("Sport's Sport Center Name\t: ",dsplist[0+dsp_x][4])
                dsp_x = dsp_x + 1
            dspx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dspx == 0):
                admin_f2()
            else:
                main_menu()

        elif(ss_no == 2):
            import os
            filesize = os.path.getsize("Sport_Center_BranchB_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sports Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            dspfile = open("Sport_Center_BranchB_Sports.txt","r")
            dsplist = []
            for line in dspfile:
                line = line.strip()
                line = line.split("\t")
                dsplist.append(line)
            dspfile.close()
            dsp_cnt = len(dsplist)
            dsp_x = 0
            for i in range(dsp_cnt):
                print("\nSport Number "+str(dsp_x+1)+"\nSport Code\t\t\t: ",dsplist[0+dsp_x][0])
                print("Sport Name\t\t\t: ",dsplist[0+dsp_x][1])
                print("Sport Hourly Rate\t\t: ",dsplist[0+dsp_x][2])
                print("Sport's Sport Center Code\t: ",dsplist[0+dsp_x][3])
                print("Sport's Sport Center Name\t: ",dsplist[0+dsp_x][4])
                dsp_x = dsp_x + 1
            dspx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dspx == 0):
                admin_f2()
            else:
                main_menu()

        else:
            import os
            filesize = os.path.getsize("Sport_Center_BranchC_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sports Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            dspfile = open("Sport_Center_BranchC_Sports.txt","r")
            dsplist = []
            for line in dspfile:
                line = line.strip()
                line = line.split("\t")
                dsplist.append(line)
            dspfile.close()
            dsp_cnt = len(dsplist)
            dsp_x = 0
            for i in range(dsp_cnt):
                print("\nSport Number "+str(dsp_x+1)+"\nSport Code\t\t\t: ",dsplist[0+dsp_x][0])
                print("Sport Name\t\t\t: ",dsplist[0+dsp_x][1])
                print("Sport Hourly Rate\t\t: ",dsplist[0+dsp_x][2])
                print("Sport's Sport Center Code\t: ",dsplist[0+dsp_x][3])
                print("Sport's Sport Center Name\t: ",dsplist[0+dsp_x][4])
                dsp_x = dsp_x + 1
            dspx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dspx == 0):
                admin_f2()
            else:
                main_menu()

    elif(adminf2_opt == 3):
        import os
        filesize = os.path.getsize("Student_info.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nNo Student Record Exist in this Sport Center !!!\nStudent Need to Register First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                admin_menu()
            else:
                main_menu()
        dstfile = open("Student_info.txt","r")
        dstlist = []
        for line in dstfile :
            line = line.strip()
            line = line.split("\t")
            dstlist.append(line)
        dstfile.close()
        #print(dstlist)
        dst_cnt = len(dstlist)
        dst_x = 0
        for i in range (dst_cnt):
            print("\nStudent Number "+str(dst_x+1)+"\nStudent ID\t\t: ",dstlist[0+dst_x][0])
            print("Student Username\t: ",dstlist[0+dst_x][1])
            print("Student Name\t\t: ",dstlist[0+dst_x][2])
            print("Student Address\t\t: ",dstlist[0+dst_x][3])
            print("Student Phone Number\t: ",dstlist[0+dst_x][4])
            print("Student Sport Name\t: ",dstlist[0+dst_x][5])
            dst_x = dst_x + 1
        dstx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(dstx == 0):
            admin_f2()
        else:
            main_menu()

    else:
        admin_menu()


#ADMIN FUNC 3 - SEARCH SPECIFIC RECORD OF [def admin_f3():]
def admin_f3():
    print("\n\n\t***Admin's Functionalities - Search Specific Record***\n\nSearch Option :\n1. Coach by Coach ID\n2. Coach by overall Performance(Rating)\n3. Sport by Sport ID\n4. Student by Student ID\n5. Admin Functionalities Menu")
    code1 = "CC" #FOR COACH
    code3 = "SP" #FOR SPORT
    code5 = "RT" #FOR STUDDENT
    adminf3_opt = int(input("Enter Your Option : "))
    while(adminf3_opt > 5 or adminf3_opt < 1):
        adminf3_opt = int(input("\nWrong Option !!!\nEnter Your Option : "))
    if(adminf3_opt == 1):
        import os
        filesize = os.path.getsize("All_Sport_Center_Coach.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                admin_menu()
            else:
                main_menu()
                
        se_idlist = []
        se_id = open("All_Sport_Center_Coach.txt","r")
        for line in se_id:
            line = line.strip()
            line = line.split("\t")
            se_idlist.append(line[0])
        print("\nAvailable Coach ID : ")
        print(se_idlist)
        se_id.close()
        se_idlist1 = []
        se_id1 = input("\nWITHOUT 'CC' (JUST NUMBER) !!!\nEnter Coach ID : ")
        while(code1+se_id1 not in se_idlist):
            se_id1 = input("\nCoach ID not Exist !!!\nWITHOUT 'CC' (JUST NUMBER) !!!\nEnter Coach ID : ")
        seidfile = open("All_Sport_Center_Coach.txt","r")
        for line in seidfile:
            if(line.startswith(code1+se_id1)):
               line = line.strip()
               line = line.split("\t")
               se_idlist1.append(line)
        #print(se_idlist1)
        seidfile.close()
        print("\nCoach ID\t\t\t\t: ",se_idlist1[0][0])
        print("Coach Name\t\t\t\t: ",se_idlist1[0][1])
        print("Coach Joined Date (dd/MM/yy)\t\t: ",se_idlist1[0][2])
        print("Coach Terminated Date (dd/MM/yy)\t: ",se_idlist1[0][3])
        print("Coach Hourly Rate\t\t\t: ",se_idlist1[0][4])
        print("Coach Phone Number\t\t\t: ",se_idlist1[0][5])
        print("Coach Address\t\t\t\t: ",se_idlist1[0][6])
        print("Coach Sport Center Code\t\t\t: ",se_idlist1[0][7])
        print("Coach Sport Center Name\t\t\t: ",se_idlist1[0][8])
        print("Coach Sport Code\t\t\t: ",se_idlist1[0][9])
        print("Coach Sport Name\t\t\t: ",se_idlist1[0][10])
        print("Coach Rating\t\t\t\t: ",se_idlist1[0][11])
        seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(seidx == 0):
            admin_f3()
        else:
            main_menu()    

    elif(adminf3_opt == 2):
        import os
        filesize = os.path.getsize("All_Sport_Center_Coach.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                admin_menu()
            else:
                main_menu()
                
        se_ovlist = []
        se_ov = open("All_Sport_Center_Coach.txt","r")
        se_ovoptlist = ["Excellent","Good","Bad","No Rate"]
        se_ovopt = input("\nExcellent\t(4 to 5)\nGood\t\t(2.5 to 3.99)\nBad\t\t(1 to 2.49)\nNo Rate\t\t(0)\nEnter Your Option : ")
        while(se_ovopt not in se_ovoptlist):
            se_ovopt = input("\nWrong Option !!!\nPlease Enter Exactly Same Word !!!\nExcellent\t(4 to 5)\nGood\t\t(2.5 to 3.99)\nBad\t\t(1 to 2.49)\nNo Rate\t\t(0)\nEnter Your Option : ")
        dcolist = []
        if(se_ovopt == "Excellent"):
            for line in se_ov:
                line = line.strip()
                line = line.split("\t")
                if(float(line[11]) >= 4 and float(line[11]) <= 5):
                    #print(line)
                    dcolist.append(line)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1

        elif(se_ovopt == "Good"):
            for line in se_ov:
                line = line.strip()
                line = line.split("\t")
                if(float(line[11]) >= 2.5 and float(line[11]) <= 3.99):
                    #print(line)
                    dcolist.append(line)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1
        elif(se_ovopt == "Bad"):
            for line in se_ov:
                line = line.strip()
                line = line.split("\t")
                if(float(line[11]) >= 1 and float(line[11]) <= 2.49):
                    #print(line)
                    dcolist.append(line)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1

        else:
            for line in se_ov:
                line = line.strip()
                line = line.split("\t")
                if(float(line[11]) == 0):
                    #print(line)
                    dcolist.append(line)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1
        
        se_ov.close()
        seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(seidx == 0):
            admin_f3()
        else:
            main_menu() 
                
    elif(adminf3_opt == 3):
        print("\nSport Center :\n1. Sport Center Branch A\n2. Sport Center Branch B\n3. Sport Center Branch C")
        ss_no = int(input("Enter Choosen Sport Center : "))
        while(ss_no > 3 or ss_no < 1):
            ss_no = int(input("\nWrong Choice !!!\nEnter Choosen Sport Center : "))
        if(ss_no == 1):
            import os
            filesize = os.path.getsize("Sport_Center_BranchA_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sports Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            se_idlist = []
            se_id = open("Sport_Center_BranchA_Sports.txt","r")
            for line in se_id:
                line = line.strip()
                line = line.split("\t")
                se_idlist.append(line[0])
            print("\nAvailable Sport Code : ")
            print(se_idlist)
            se_id.close()
            se_idlist1 = []
            se_id1 = input("\nWITHOUT 'SP' (JUST NUMBER) !!!\nEnter Sport Code : ")
            while(code3+se_id1 not in se_idlist):
                se_id1 = input("\nSport Code not Exist !!!\nWITHOUT 'SP' (JUST NUMBER) !!!\nEnter Sport Code : ")
            seidfile = open("Sport_Center_BranchA_Sports.txt","r")
            for line in seidfile:
                if(line.startswith(code3+se_id1)):
                   line = line.strip()
                   line = line.split("\t")
                   se_idlist1.append(line)
            #print(se_idlist1)
            seidfile.close()
            print("\nSport Code\t\t\t: ",se_idlist1[0][0])
            print("Sport Name\t\t\t: ",se_idlist1[0][1])
            print("Sport Hourly Rate\t\t: ",se_idlist1[0][2])
            print("Sport's Sport Center Code\t: ",se_idlist1[0][3])
            print("Sport's Sport Center Name\t: ",se_idlist1[0][4])

            
            seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(seidx == 0):
                admin_f3()
            else:
                main_menu()

        elif(ss_no == 2):
            import os
            filesize = os.path.getsize("Sport_Center_BranchB_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sports Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            se_idlist = []
            se_id = open("Sport_Center_BranchB_Sports.txt","r")
            for line in se_id:
                line = line.strip()
                line = line.split("\t")
                se_idlist.append(line[0])
            print("\nAvailable Sport Code : ")
            print(se_idlist)
            se_id.close()
            se_idlist1 = []
            se_id1 = input("\nWITHOUT 'SP' (JUST NUMBER) !!!\nEnter Sport Code : ")
            while(code3+se_id1 not in se_idlist):
                se_id1 = input("\nSport Code not Exist !!!\nWITHOUT 'SP' (JUST NUMBER) !!!\nEnter Sport Code : ")
            seidfile = open("Sport_Center_BranchB_Sports.txt","r")
            for line in seidfile:
                if(line.startswith(code3+se_id1)):
                   line = line.strip()
                   line = line.split("\t")
                   se_idlist1.append(line)
            #print(se_idlist1)
            seidfile.close()
            print("\nSport Code\t\t\t: ",se_idlist1[0][0])
            print("Sport Name\t\t\t: ",se_idlist1[0][1])
            print("Sport Hourly Rate\t\t: ",se_idlist1[0][2])
            print("Sport's Sport Center Code\t: ",se_idlist1[0][3])
            print("Sport's Sport Center Name\t: ",se_idlist1[0][4])

            
            seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(seidx == 0):
                admin_f3()
            else:
                main_menu()
        
        else:
            import os
            filesize = os.path.getsize("Sport_Center_BranchC_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Sports Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    admin_menu()
                else:
                    main_menu()
            se_idlist = []
            se_id = open("Sport_Center_BranchC_Sports.txt","r")
            for line in se_id:
                line = line.strip()
                line = line.split("\t")
                se_idlist.append(line[0])
            print("\nAvailable Sport Code : ")
            print(se_idlist)
            se_id.close()
            se_idlist1 = []
            se_id1 = input("\nWITHOUT 'SP' (JUST NUMBER) !!!\nEnter Sport Code : ")
            while(code3+se_id1 not in se_idlist):
                se_id1 = input("\nSport Code not Exist !!!\nWITHOUT 'SP' (JUST NUMBER) !!!\nEnter Sport Code : ")
            seidfile = open("Sport_Center_BranchC_Sports.txt","r")
            for line in seidfile:
                if(line.startswith(code3+se_id1)):
                   line = line.strip()
                   line = line.split("\t")
                   se_idlist1.append(line)
            #print(se_idlist1)
            seidfile.close()
            print("\nSport Code\t\t\t: ",se_idlist1[0][0])
            print("Sport Name\t\t\t: ",se_idlist1[0][1])
            print("Sport Hourly Rate\t\t: ",se_idlist1[0][2])
            print("Sport's Sport Center Code\t: ",se_idlist1[0][3])
            print("Sport's Sport Center Name\t: ",se_idlist1[0][4])

            
            seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(seidx == 0):
                admin_f3()
            else:
                main_menu()

    elif(adminf3_opt == 4):
        import os
        filesize = os.path.getsize("Student_info.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nNo Student Record Exist in this Sport Center !!!\nFor now No Student Registered!!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                admin_menu()
            else:
                main_menu()
        se_idlist = []
        se_id = open("Student_info.txt","r")
        for line in se_id:
            line = line.strip()
            line = line.split("\t")
            se_idlist.append(line[0])
        print("\nAvailable Student ID : ")
        print(se_idlist)
        se_id.close()
        se_idlist1 = []
        se_id1 = input("\nWITHOUT 'RT' (JUST NUMBER) !!!\nEnter Student ID : ")
        while(code5+se_id1 not in se_idlist):
            se_id1 = input("\nStudent ID not Exist !!!\nWITHOUT 'RT' (JUST NUMBER) !!!\nEnter Student ID : ")
        seidfile = open("Student_info.txt","r")
        for line in seidfile:
            if(line.startswith(code5+se_id1)):
                line = line.strip()
                line = line.split("\t")
                se_idlist1.append(line)
        #print(se_idlist1)
        seidfile.close()
        print("\nStudent ID\t\t: ",se_idlist1[0][0])
        print("Student Username\t: ",se_idlist1[0][1])
        print("Student Name\t\t: ",se_idlist1[0][2])
        print("Student Address\t\t: ",se_idlist1[0][3])
        print("Student Phone Number\t: ",se_idlist1[0][4])
        print("Student Sport Name\t: ",se_idlist1[0][5])

            
        seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(seidx == 0):
            admin_f3()
        else:
            main_menu()   
        
    else:
        admin_menu()

#ADMIN FUNC 4. SORT AND DISPLAY [def admin_f4():]
def admin_f4():
    import os
    filesize = os.path.getsize("All_Sport_Center_Coach.txt")
    #print(filesize)
    while (filesize == 0):
        nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
        if( nosize_opt == 0 ):
            admin_menu()
        else:
            main_menu()
    print("\n\n\t***Admin Functionalities - Sort & Display Record***\n\nRecord Option :\n1. Coaches in ascending order by Names\n2. Coaches Hourly Pay Rate in ascending order\n3. Coaches Overall Performance in Ascending Order\n4. Admin Functionalities Menu")
    adminf4_opt = int(input("Enter Your Option : "))
    while (adminf4_opt > 4 or adminf4_opt < 1):
        adminf4_opt = int(input("\nWrong Option !!!\nEnter Your Option : "))
    sortfile = open("All_Sport_Center_Coach.txt","r")
    sortfile1 = open("All_Sport_Center_Coach.txt","r")
    sortlist = []
    dcolist = []
    if(adminf4_opt == 1):
        for line in sortfile:
            line = line.strip()
            line = line.split("\t")
            sortlist.append(line[1])
        #print(sortlist)
        sortfile.close()
        for i in range(0, len(sortlist) - 1):
            for j in range(0, len(sortlist) - 1 - i):
                if(sortlist [j] > sortlist[j+1]):
                   sortlist[j], sortlist[j+1] = sortlist [j+1], sortlist[j]
        #print(sortlist)
        sortline1 = sortfile1.readlines()
        sort_x = 0
        sort_xx = 0
        for i in range(len(sortlist)):
            sort_xx = sortlist[0+sort_x]
            for line in sortline1:
                line = line.strip()
                line = line.split("\t")
                if(sort_xx in line):
                    dcolist.append(line)
            sort_x = sort_x + 1
        #print(dcolist)
        sortfile1.close()
        dupelist =[]
        for i in dcolist:
            if i not in dupelist:
                dupelist.append(i)
        dcolist = dupelist
        dco_cnt = len(dcolist)
        dco_x = 0
        for i in range (dco_cnt):
            print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
            print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
            print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
            print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
            print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
            print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
            print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
            print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
            print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
            print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
            print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
            print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
            dco_x = dco_x + 1
        seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(seidx == 0):
            admin_f4()
        else:
            main_menu()

    elif(adminf4_opt == 2):
        for line in sortfile:
            line = line.strip()
            line = line.split("\t")
            sortlist.append(line[4])
        #print(sortlist)
        sortfile.close()
        for i in range(0, len(sortlist) - 1):
            for j in range(0, len(sortlist) - 1 - i):
                if(sortlist [j] > sortlist[j+1]):
                   sortlist[j], sortlist[j+1] = sortlist [j+1], sortlist[j]
        #print(sortlist)
        sortline1 = sortfile1.readlines()
        sort_x = 0
        sort_xx = 0
        for i in range(len(sortlist)):
            sort_xx = sortlist[0+sort_x]
            for line in sortline1:
                line = line.strip()
                line = line.split("\t")
                if(sort_xx in line):
                    dcolist.append(line)
            sort_x = sort_x + 1
        #print(dcolist)
        sortfile1.close()
        dupelist =[]
        for i in dcolist:
            if i not in dupelist:
                dupelist.append(i)
        dcolist = dupelist
        dco_cnt = len(dcolist)
        dco_x = 0
        for i in range (dco_cnt):
            print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
            print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
            print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
            print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
            print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
            print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
            print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
            print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
            print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
            print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
            print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
            print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
            dco_x = dco_x + 1
        seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(seidx == 0):
            admin_f4()
        else:
            main_menu()

    elif(adminf4_opt == 3):
        for line in sortfile:
            line = line.strip()
            line = line.split("\t")
            sortlist.append(line[11])
        #print(sortlist)
        sortfile.close()
        for i in range(0, len(sortlist) - 1):
            for j in range(0, len(sortlist) - 1 - i):
                if(sortlist [j] > sortlist[j+1]):
                   sortlist[j], sortlist[j+1] = sortlist [j+1], sortlist[j]
        #print(sortlist)
        sortline1 = sortfile1.readlines()
        sort_x = 0
        sort_xx = 0
        for i in range(len(sortlist)):
            sort_xx = sortlist[0+sort_x]
            for line in sortline1:
                line = line.strip()
                line = line.split("\t")
                if(sort_xx in line):
                    dcolist.append(line)
            sort_x = sort_x + 1
        #print(dcolist)
        sortfile1.close()
        dupelist =[]
        for i in dcolist:
            if i not in dupelist:
                dupelist.append(i)
        dcolist = dupelist
        dco_cnt = len(dcolist)
        dco_x = 0
        for i in range (dco_cnt):
            print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
            print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
            print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
            print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
            print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
            print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
            print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
            print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
            print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
            print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
            print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
            print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
            dco_x = dco_x + 1
        seidx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(seidx == 0):
            admin_f4()
        else:
            main_menu()

    else:
        admin_menu()

#ADMIN FUNC 5 - MODIFY RECORD [def admin_f5():]
def admin_f5():
    code1 = "CC" #For Coach ID
    code3 = "SP" #For Sport Code.
    code4 = "RM" #For Hourly Rate
    code6 = "DL" #For Schedule ID
    print("\n\n\t***Admin Functionalities - Modify Record***\n\nRecord Option :\n1. Coach\n2. Sport\n3. Sport Schedule\n4. Admin Functionalities Menu")
    adminf5_opt = int(input("Enter Your Option : "))
    while (adminf5_opt > 4 or adminf5_opt < 1):
        adminf5_opt = int(input("\nWrong Option !!!\nEnter Your Option : "))
    if(adminf5_opt == 1):
        import os
        filesize = os.path.getsize("All_Sport_Center_Coach.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nNo Coach Record Exist in this Sport Center !!!\nAdd Coach Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                admin_menu()
            else:
                main_menu()

        admodfile = open("All_Sport_Center_Coach.txt","r") #closed
        admodfile1 = open("All_Sport_Center_Coach.txt","r") #closed
        admodlist = []
        for line in admodfile :
            line = line.strip()
            line = line.split()
            admodlist.append(line[0])
            admodlist.append(line[1])
        admodfile.close()
        print("\nAvailable Coach ID, Name : ")
        print(admodlist)
        admodid = input("\nWITHOUT 'CC' !!!\nEnter Coach ID : ")
        while code1+admodid not in admodlist:
            admodid = input("\nCoach ID not Exist !!!\nWITHOUT 'CC' !!!\nEnter Coach ID : ")
        admodlist1 = []
        for line in admodfile1:
            line = line.strip()
            line = line.split("\t")
            if(code1+admodid in line):
                admodlist1.append(line)
        admodfile1.close()
        print(admodlist1)
        ad11 = admodlist1[0][11]
        ad1 = input("Coach Name\t\t\t\t: ")
        ad2 = input("Coach Joined Date (dd/MM/yy)\t\t: ")
        ad3 = input("Coach Terminated Date (dd/MM/yy)\t: ")
        ad5 = input("Coach Phone Number\t\t\t: ")
        ad6 = input("Coach Address\t\t\t\t: ")
        scclist = ["LC1","LC2","LC3"]
        ad7 = input("\nLC1 for Sport Center Branch A\nLC2 for Sport Center Branch B\nLC3 for Sport Center Branch C\nCoach Sport Center Code\t\t\t: ")
        while ad7 not in scclist:
            ad7 = input("\nWrong Code !!!\nCoach Sport Center Code\t\t\t: ")
        if(ad7 == "LC1"):
            ad8 = "Branch A"
            print("Coach Sport Center Name\t\t\t: ",ad8) 
            adsnfile = open("Sport_Center_BranchA_Sports.txt","r")
            adsnfile1 = open("Sport_Center_BranchA_Sports.txt","r")
            adsnlist = []
            adsnlist1 = []
            for line in adsnfile:
                line = line.strip()
                line = line.split("\t")
                adsnlist.append(line[0])
            print("\nAvailable Sport Code :")
            print(adsnlist)
            adsnfile.close()
            ad9 = input("WITH 'SP' !!!\nCoach Sport Code : ")
            while(ad9 not in adsnlist):
                ad9 = input("\nSport Code not Exist in this Sport Center !!!\nCoach Sport Code : ")
            for line in adsnfile1:
                line = line.strip()
                line = line.split("\t")
                if(ad9 in line):
                    adsnlist1.append(line)
            #print(adsnlist1)
            adsnfile1.close()
            ad4 = adsnlist1[0][2]
            ad10 = adsnlist1[0][1]
            print("Coach Sport Name\t\t\t: "+ad10+"\nCoach Hourly Rate\t\t\t: "+ad4)

            adsnfile2 = open("Sport_Center_BranchB_Coach.txt","r")
            adsnline2 = adsnfile2.readlines()
            adsnfile2.close()
            newline1 = ""
            for line in adsnline2:
                if(code1+admodid in line):
                    line = ""
                newline1 += line
            adsnwrite = open("Sport_Center_BranchB_Coach.txt","w")
            adsnwrite.write(newline1)
            adsnwrite.close()

            adsnfile3 = open("Sport_Center_BranchC_Coach.txt","r")
            adsnline3 = adsnfile3.readlines()
            adsnfile3.close()
            newline2 = ""
            for line in adsnline3:
                if(code1+admodid in line):
                    line = ""
                newline2 += line
            adsnwrite1 = open("Sport_Center_BranchC_Coach.txt","w")
            adsnwrite1.write(newline2)
            adsnwrite1.close()

            adsnfile4 = open("Sport_Center_BranchA_Coach.txt","r")
            linex = adsnfile4.read()
            adsnfile4.close()
            #print(linex)
            if(code1+admodid in linex):
                adsnfile6 = open("Sport_Center_BranchA_Coach.txt","r")
                lines = adsnfile6.readlines()
                adsnfile6.close()
                newline = ""
                for line in lines:
                    if(code1+admodid in line):
                        line = code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n"
                    newline += line
                adsnfile1 = open("Sport_Center_BranchA_Coach.txt","w")
                adsnfile1.write(newline)
                adsnfile1.close()  
            else:
                adsnfile7 = open("Sport_Center_BranchA_Coach.txt","a")
                adsnfile7.write(code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n")
                adsnfile7.close()

            adsnfile5 = open("All_Sport_Center_Coach.txt","r")
            adsnline5 = adsnfile5.readlines()
            newline4 = ""
            adsnfile5.close()
            for line in adsnline5:
                if(code1+admodid in line):
                    line = code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n"
                newline4 += line
            adsnwrite3 = open("All_Sport_Center_Coach.txt","w")
            adsnwrite3.write(newline4)
            adsnwrite3.close()
            
            
            
        elif(ad7 == "LC2"):
            ad8 = "Branch B"
            print("Coach Sport Center Name\t\t\t: ",ad8) 
            adsnfile = open("Sport_Center_BranchB_Sports.txt","r")
            adsnfile1 = open("Sport_Center_BranchB_Sports.txt","r")
            adsnlist = []
            adsnlist1 = []
            for line in adsnfile:
                line = line.strip()
                line = line.split("\t")
                adsnlist.append(line[0])
            print("\nAvailable Sport Code :")
            print(adsnlist)
            adsnfile.close()
            ad9 = input("WITH 'SP' !!!\nCoach Sport Code : ")
            while(ad9 not in adsnlist):
                ad9 = input("\nSport Code not Exist in this Sport Center !!!\nCoach Sport Code : ")
            for line in adsnfile1:
                line = line.strip()
                line = line.split("\t")
                if(ad9 in line):
                    adsnlist1.append(line)
            #print(adsnlist1)
            adsnfile1.close()
            ad4 = adsnlist1[0][2]
            ad10 = adsnlist1[0][1]
            print("Coach Sport Name\t\t\t: "+ad10+"\nCoach Hourly Rate\t\t\t: "+ad4)
            adsnfile2 = open("Sport_Center_BranchA_Coach.txt","r")
            adsnline2 = adsnfile2.readlines()
            adsnfile2.close()
            newline1 = ""
            for line in adsnline2:
                if(code1+admodid in line):
                    line = ""
                newline1 += line
            adsnwrite = open("Sport_Center_BranchA_Coach.txt","w")
            adsnwrite.write(newline1)
            adsnwrite.close()
            adsnfile3 = open("Sport_Center_BranchC_Coach.txt","r")
            adsnline3 = adsnfile3.readlines()
            adsnfile3.close()
            newline2 = ""
            for line in adsnline3:
                if(code1+admodid in line):
                    line = ""
                newline2 += line
            adsnwrite1 = open("Sport_Center_BranchC_Coach.txt","w")
            adsnwrite1.write(newline2)
            adsnwrite1.close()
            
            adsnfile4 = open("Sport_Center_BranchB_Coach.txt","r")
            linex = adsnfile4.read()
            adsnfile4.close()
            #print(linex)
            if(code1+admodid in linex):
                adsnfile6 = open("Sport_Center_BranchB_Coach.txt","r")
                lines = adsnfile6.readlines()
                adsnfile6.close()
                newline = ""
                for line in lines:
                    if(code1+admodid in line):
                        line = code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n"
                    newline += line
                adsnfile1 = open("Sport_Center_BranchB_Coach.txt","w")
                adsnfile1.write(newline)
                adsnfile1.close()  
            else:
                adsnfile7 = open("Sport_Center_BranchB_Coach.txt","a")
                adsnfile7.write(code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n")
                adsnfile7.close()
                
            adsnfile5 = open("All_Sport_Center_Coach.txt","r")
            adsnline5 = adsnfile5.readlines()
            newline4 = ""
            adsnfile5.close()
            for line in adsnline5:
                if(code1+admodid in line):
                    line = code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n"
                newline4 += line
            adsnwrite3 = open("All_Sport_Center_Coach.txt","w")
            adsnwrite3.write(newline4)
            adsnwrite3.close()

        else:
            ad8 = "Branch C"
            print("Coach Sport Center Name\t\t\t: ",ad8) 
            adsnfile = open("Sport_Center_BranchC_Sports.txt","r")
            adsnfile1 = open("Sport_Center_BranchC_Sports.txt","r")
            adsnlist = []
            adsnlist1 = []
            for line in adsnfile:
                line = line.strip()
                line = line.split("\t")
                adsnlist.append(line[0])
            print("\nAvailable Sport Code :")
            print(adsnlist)
            adsnfile.close()
            ad9 = input("WITH 'SP' !!!\nCoach Sport Code : ")
            while(ad9 not in adsnlist):
                ad9 = input("\nSport Code not Exist in this Sport Center !!!\nCoach Sport Code : ")
            for line in adsnfile1:
                line = line.strip()
                line = line.split("\t")
                if(ad9 in line):
                    adsnlist1.append(line)
            print(adsnlist1)
            adsnfile1.close()
            ad4 = adsnlist1[0][2]
            ad10 = adsnlist1[0][1]
            print("Coach Sport Name\t\t\t: "+ad10+"\nCoach Hourly Rate\t\t\t: "+ad4)
            adsnfile2 = open("Sport_Center_BranchA_Coach.txt","r")
            adsnline2 = adsnfile2.readlines()
            adsnfile2.close()
            newline1 = ""
            for line in adsnline2:
                if(code1+admodid in line):
                    line = ""
                newline1 += line
            adsnwrite = open("Sport_Center_BranchA_Coach.txt","w")
            adsnwrite.write(newline1)
            adsnwrite.close()
            adsnfile3 = open("Sport_Center_BranchB_Coach.txt","r")
            adsnline3 = adsnfile3.readlines()
            adsnfile3.close()
            newline2 = ""
            for line in adsnline3:
                if(code1+admodid in line):
                    line = ""
                newline2 += line
            adsnwrite1 = open("Sport_Center_BranchB_Coach.txt","w")
            adsnwrite1.write(newline2)
            adsnwrite1.close()
            
            adsnfile4 = open("Sport_Center_BranchC_Coach.txt","r")
            linex = adsnfile4.read()
            adsnfile4.close()
            #print(linex)
            if(code1+admodid in linex):
                adsnfile6 = open("Sport_Center_BranchC_Coach.txt","r")
                lines = adsnfile6.readlines()
                adsnfile6.close()
                newline = ""
                for line in lines:
                    if(code1+admodid in line):
                        line = code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n"
                    newline += line
                adsnfile1 = open("Sport_Center_BranchC_Coach.txt","w")
                adsnfile1.write(newline)
                adsnfile1.close()  
            else:
                adsnfile7 = open("Sport_Center_BranchC_Coach.txt","a")
                adsnfile7.write(code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n")
                adsnfile7.close()
                
            adsnfile5 = open("All_Sport_Center_Coach.txt","r")
            adsnline5 = adsnfile5.readlines()
            newline4 = ""
            adsnfile5.close()
            for line in adsnline5:
                if(code1+admodid in line):
                    line = code1+admodid+"\t"+ad1+"\t"+ad2+"\t"+ad3+"\t"+ad4+"\t"+ad5+"\t"+ad6+"\t"+ad7+"\t"+ad8+"\t"+ad9+"\t"+ad10+"\t"+ad11+"\n"
                newline4 += line
            adsnwrite3 = open("All_Sport_Center_Coach.txt","w")
            adsnwrite3.write(newline4)
            adsnwrite3.close()
        admodx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(admodx == 0):
            admin_f5()
        else:
            main_menu()


    elif(adminf5_opt == 2):
        modsp3 = "LC1"
        modsp33 = "LC2"
        modsp333 = "LC3"
        modsp4 = "Branch A"
        modsp44 = "Branch B"
        modsp444 = "Branch C"
        import os
        filesize = os.path.getsize("All_Sport_Center_Sports.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nNo Sport Record Exist in this Sport Center !!!\nAdd Sport Record First !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                admin_menu()
            else:
                main_menu()

        modspfile = open("All_Sport_Center_Sports.txt","r")
        modsplist = []
        for line in modspfile:
            line = line.strip()
            line = line.split("\t")
            modsplist.append(line[0])
            modsplist.append(line[1])
        modspfile.close()
        print("\nAvailable Sport Code, Sport Name : ")
        print(modsplist)
        modspcd = input("\nWITHOUT 'SP' !!!\nEnter Sport Code\t\t\t: ")
        while code3+modspcd not in modsplist:
            modspcd = input("\nSport Code not Exist !!!\nWITHOUT 'SP' !!!\nEnter Sport Code\t\t\t: ")
        print("\nAvailable Sport Name : ")
        sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
        print(sp_namelist)
        modsp1 = input("Enter Sport Name\t\t\t: ")
        while(modsp1 not in sp_namelist):
            modsp1 = input("\nWrong Input !!!\nEnter Exactly Same like in Avaiable Sport !!!\nEnter Sport Name\t\t\t: ")
        modsp2 = int(input("\n\nRange is 100 to 500\nEnter Sport Hourly Rate\t\t:"))
        while (modsp2 > 500 or modsp2 < 100):
            modsp2 = int(input("\nWrong Number !!!\n Range is 100 to 500\nEnter Sport Hourly Rate\t\t:"))

        modspfile1 = open("Sport_Center_BranchA_Sports.txt","r")
        modspline1 = modspfile1.readlines()
        newline1 = ""
        modspfile1.close()
        for line in modspline1:
            if(code3+modspcd in line):
                line = code3+modspcd+"\t"+modsp1+"\t"+code4+str(modsp2)+"\t"+modsp3+"\t"+modsp4+"\n"
            newline1 += line
        modspwrite1 = open("Sport_Center_BranchA_Sports.txt","w")
        modspwrite1.write(newline1)
        modspwrite1.close()

        modspfile2 = open("Sport_Center_BranchB_Sports.txt","r")
        modspline2 = modspfile2.readlines()
        newline2 =""
        modspfile2.close()
        for line in modspline2 :
            if(code3+modspcd in line):
                line = code3+modspcd+"\t"+modsp1+"\t"+code4+str(modsp2)+"\t"+modsp33+"\t"+modsp44+"\n"
            newline2 += line
        modspwrite2 = open("Sport_Center_BranchB_Sports.txt","w")
        modspwrite2.write(newline2)
        modspwrite2.close()

        modspfile3 = open("Sport_Center_BranchC_Sports.txt","r")
        modspline3 = modspfile3.readlines()
        newline3 = ""
        modspfile3.close()
        for line in modspline3:
            if(code3+modspcd in line):
                line = code3+modspcd+"\t"+modsp1+"\t"+code4+str(modsp2)+"\t"+modsp333+"\t"+modsp444+"\n"
            newline3 += line
        modspwrite3 = open("Sport_Center_BranchC_Sports.txt","w")
        modspwrite3.write(newline3)
        modspwrite3.close()

        modspfile4 = open("All_Sport_Center_Sports.txt","r")
        modspline4 = modspfile4.readlines()
        newline4 = ""
        modspfile4.close()
        for line in modspline4:
            if(code3+modspcd in line):
                line = code3+modspcd+"\t"+modsp1+"\t"+code4+str(modsp2)+"\t"+modsp3+"\t"+modsp4+"\n"
            newline4 += line
        modspwrite4 = open("All_Sport_Center_Sports.txt","w")
        modspwrite4.write(newline4)
        modspwrite4.close()
        modspx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(modspx == 0):
            admin_f5()
        else:
            main_menu()


    elif(adminf5_opt == 3):
        import os
        filesize = os.path.getsize("All_Sport_Center_Schedule.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nCurrently No Schedule Available in this Sport Center !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                admin_menu()
            else:
                main_menu()
        scmodfile = open("All_Sport_Center_Schedule.txt","r")
        scmodfile1 = open("All_Sport_Center_Coach.txt","r")
        scmodfile2 = open("All_Sport_Center_Coach.txt","r")
        scmodlist = []
        scmodlist1 = []
        scmodlist2 = []
        for line in scmodfile:
            line = line.strip()
            line = line.split("\t")
            scmodlist.append(line[0])
        print("\nAvailable Schedule ID : ")
        print(scmodlist)
        scmodfile.close()
        scid = input("\nWithout 'DL'!!!\nEnter Schedule ID : ")
        while(code6+scid not in scmodlist):
            scid = input("\nWrong Input !!!\nWithout 'DL'!!!\nEnter Schedule ID : ")
        for line in scmodfile1:
            line = line.strip()
            line = line.split("\t")
            scmodlist1.append(line[0])
            scmodlist1.append(line[1])
        print("\nAvailable Coach ID, Coach Name : ")
        print(scmodlist1)
        scmodfile1.close()
        scco = input("\nWITHOUT 'CC' !!!\nEnter Coach ID : ")
        while(code1+scco not in scmodlist1):
            scco = input("\nWrong Input !!!\nEnter Coach ID : ")
        for line in scmodfile2:
            line = line.strip()
            line = line.split("\t")
            if(code1+scco in line):
                scmodlist2.append(line)
        #print(scmodlist2)
        scmodfile2.close()
        scco_nm = scmodlist2[0][1]
        scco_sp = scmodlist2[0][10]
        scco_scc = scmodlist2[0][7]
        scco_scn = scmodlist2[0][8]
        print("\nEnter Coach Name\t: "+scco_nm+"\nEnter Coach Sport Name\t: "+scco_sp+"\nEnter Coach Sport Center Code : "+scco_scc+"\nEnter Coach Sport Center Name : "+scco_scn)
        sctime = input("Enter Time (dd/MM/yy/hh:mm - hh:mm) : ")
        if(scco_scc == "LC1"):
            adsnfile2 = open("Sport_Center_BranchB_Schedule.txt","r")
            adsnline2 = adsnfile2.readlines()
            adsnfile2.close()
            newline1 = ""
            for line in adsnline2:
                if(code6+scid in line):
                    line = ""
                newline1 += line
            adsnwrite = open("Sport_Center_BranchB_Schedule.txt","w")
            adsnwrite.write(newline1)
            adsnwrite.close()

            adsnfile3 = open("Sport_Center_BranchC_Schedule.txt","r")
            adsnline3 = adsnfile3.readlines()
            adsnfile3.close()
            newline2 = ""
            for line in adsnline3:
                if(code6+scid in line):
                    line = ""
                newline2 += line
            adsnwrite1 = open("Sport_Center_BranchC_Schedule.txt","w")
            adsnwrite1.write(newline2)
            adsnwrite1.close()

            adsnfile4 = open("Sport_Center_BranchA_Schedule.txt","r")
            linex = adsnfile4.read()
            adsnfile4.close()
            #print(linex)
            if(code6+scid in linex):
                adsnfile6 = open("Sport_Center_BranchA_Schedule.txt","r")
                lines = adsnfile6.readlines()
                adsnfile6.close()
                newline = ""
                for line in lines:
                    if(code6+scid in line):
                        line = code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n"
                    newline += line
                adsnfile1 = open("Sport_Center_BranchA_Schedule.txt","w")
                adsnfile1.write(newline)
                adsnfile1.close()  
            else:
                adsnfile7 = open("Sport_Center_BranchA_Schedule.txt","a")
                adsnfile7.write(code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n")
                adsnfile7.close()

            adsnfile5 = open("All_Sport_Center_Schedule.txt","r")
            adsnline5 = adsnfile5.readlines()
            newline4 = ""
            adsnfile5.close()
            for line in adsnline5:
                if(code6+scid in line):
                    line = code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n"
                newline4 += line
            adsnwrite3 = open("All_Sport_Center_Schedule.txt","w")
            adsnwrite3.write(newline4)
            adsnwrite3.close()

        elif(scco_scc == "LC2"):
            adsnfile2 = open("Sport_Center_BranchA_Schedule.txt","r")
            adsnline2 = adsnfile2.readlines()
            adsnfile2.close()
            newline1 = ""
            for line in adsnline2:
                if(code6+scid in line):
                    line = ""
                newline1 += line
            adsnwrite = open("Sport_Center_BranchA_Schedule.txt","w")
            adsnwrite.write(newline1)
            adsnwrite.close()

            adsnfile3 = open("Sport_Center_BranchC_Schedule.txt","r")
            adsnline3 = adsnfile3.readlines()
            adsnfile3.close()
            newline2 = ""
            for line in adsnline3:
                if(code6+scid in line):
                    line = ""
                newline2 += line
            adsnwrite1 = open("Sport_Center_BranchC_Schedule.txt","w")
            adsnwrite1.write(newline2)
            adsnwrite1.close()

            adsnfile4 = open("Sport_Center_BranchB_Schedule.txt","r")
            linex = adsnfile4.read()
            adsnfile4.close()
            #print(linex)
            if(code6+scid in linex):
                adsnfile6 = open("Sport_Center_BranchB_Schedule.txt","r")
                lines = adsnfile6.readlines()
                adsnfile6.close()
                newline = ""
                for line in lines:
                    if(code6+scid in line):
                        line = code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n"
                    newline += line
                adsnfile1 = open("Sport_Center_BranchB_Schedule.txt","w")
                adsnfile1.write(newline)
                adsnfile1.close()  
            else:
                adsnfile7 = open("Sport_Center_BranchB_Schedule.txt","a")
                adsnfile7.write(code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n")
                adsnfile7.close()

            adsnfile5 = open("All_Sport_Center_Schedule.txt","r")
            adsnline5 = adsnfile5.readlines()
            newline4 = ""
            adsnfile5.close()
            for line in adsnline5:
                if(code6+scid in line):
                    line = code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n"
                newline4 += line
            adsnwrite3 = open("All_Sport_Center_Schedule.txt","w")
            adsnwrite3.write(newline4)
            adsnwrite3.close()

        else:
            adsnfile2 = open("Sport_Center_BranchB_Schedule.txt","r")
            adsnline2 = adsnfile2.readlines()
            adsnfile2.close()
            newline1 = ""
            for line in adsnline2:
                if(code6+scid in line):
                    line = ""
                newline1 += line
            adsnwrite = open("Sport_Center_BranchB_Schedule.txt","w")
            adsnwrite.write(newline1)
            adsnwrite.close()

            adsnfile3 = open("Sport_Center_BranchA_Schedule.txt","r")
            adsnline3 = adsnfile3.readlines()
            adsnfile3.close()
            newline2 = ""
            for line in adsnline3:
                if(code6+scid in line):
                    line = ""
                newline2 += line
            adsnwrite1 = open("Sport_Center_BranchA_Schedule.txt","w")
            adsnwrite1.write(newline2)
            adsnwrite1.close()

            adsnfile4 = open("Sport_Center_BranchC_Schedule.txt","r")
            linex = adsnfile4.read()
            adsnfile4.close()
            #print(linex)
            if(code6+scid in linex):
                adsnfile6 = open("Sport_Center_BranchC_Schedule.txt","r")
                lines = adsnfile6.readlines()
                adsnfile6.close()
                newline = ""
                for line in lines:
                    if(code6+scid in line):
                        line = code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n"
                    newline += line
                adsnfile1 = open("Sport_Center_BranchC_Schedule.txt","w")
                adsnfile1.write(newline)
                adsnfile1.close()  
            else:
                adsnfile7 = open("Sport_Center_BranchC_Schedule.txt","a")
                adsnfile7.write(code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n")
                adsnfile7.close()

            adsnfile5 = open("All_Sport_Center_Schedule.txt","r")
            adsnline5 = adsnfile5.readlines()
            newline4 = ""
            adsnfile5.close()
            for line in adsnline5:
                if(code6+scid in line):
                    line = code6+scid+"\t"+code1+scco+"\t"+scco_nm+"\t"+scco_sp+"\t"+scco_scc+"\t"+scco_scn+"\t"+sctime+"\n"
                newline4 += line
            adsnwrite3 = open("All_Sport_Center_Schedule.txt","w")
            adsnwrite3.write(newline4)
            adsnwrite3.close()
        modspx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(modspx == 0):
            admin_f5()
        else:
            main_menu()


    else:
        admin_menu()
    



#Public Student Main Menu [def ps_menu():]
def ps_menu():
    print("\n\n\t***WELCOME  TO REAL CHAMPIONS SPORT ACADEMY SITE***\n\nPublic Student Option :\n1. View Detail\n2. Register\n3. Login\n4. Main Menu\n5. Exit")
    pubstu_opt = int(input("Enter Your Option : "))
    while (pubstu_opt > 5 or pubstu_opt < 1):
        pubstu_opt=int(input("\nWrong Option !!!\nRe-enter Your Option : "))
    if(pubstu_opt == 1):
        ps_func()
    elif(pubstu_opt == 2):
        newst_reg()
    elif(pubstu_opt == 3):
        stulog()
    elif(pubstu_opt == 4):
        main_menu()
    else:
        exit()




#Public Student FUNCTION - View Sport & Schedudle [def ps_func():]
def ps_func():
    print("\n\nAvailable Option :\n1. View Detail of Sports\n2. View Details of Sport Schedule\n3. Public Student Menu")
    pubstuf1_opt = int(input("Enter Your Option : "))
    while (pubstuf1_opt > 3 or pubstuf1_opt < 1):
        pubstuf1_opt = int(input("\nWrong Option !!!\n Enter Your Option : "))
    if(pubstuf1_opt == 1):
        print("\n\nSport Center :\n1. Sport Center Branch A\n2. Sport Center Branch B\n3. Sport Center Branch C")
        ss_no = int(input("Enter Choosen Sport Center : "))
        while(ss_no > 3 or ss_no < 1):
            ss_no = int(input("Wrong Input !!!\nEnter Choosen Sport Center : "))
        if(ss_no == 1):
            import os
            filesize = os.path.getsize("Sport_Center_BranchA_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nCurrently No Sports Available in this Sport Center !!!\nEnter '0' to Public Student or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    ps_menu()
                else:
                    main_menu()
            pubstfile = open("Sport_Center_BranchA_Sports.txt","r")
            pubstlist = []
            for line in pubstfile:
                line = line.strip()
                line = line.split("\t")
                pubstlist.append(line)
            pubstfile.close()
            pubst_cnt = len(pubstlist)
            pubst_x = 0
            for i in range(pubst_cnt):
                print("\nSport Number "+str(pubst_x+1)+"\nSport Code\t\t\t: ",pubstlist[0+pubst_x][0])
                print("Sport Name\t\t\t: ",pubstlist[0+pubst_x][1])
                print("Sport Hourly Rate\t\t: ",pubstlist[0+pubst_x][2])
                print("Sport's Sport Center Code\t: ",pubstlist[0+pubst_x][3])
                print("Sport's Sport Center Name\t: ",pubstlist[0+pubst_x][4])
                pubst_x = pubst_x + 1
            pubstx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(pubstx == 0):
                ps_func()
            else:
                main_menu()

        elif(ss_no == 2):
            import os
            filesize = os.path.getsize("Sport_Center_BranchB_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nCurrently No Sports Available in this Sport Center !!!\nEnter '0' to Public Student Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    ps_menu()
                else:
                    main_menu()
            pubstfile = open("Sport_Center_BranchB_Sports.txt","r")
            pubstlist = []
            for line in pubstfile:
                line = line.strip()
                line = line.split("\t")
                pubstlist.append(line)
            pubstfile.close()
            pubst_cnt = len(pubstlist)
            pubst_x = 0
            for i in range(pubst_cnt):
                print("\nSport Number "+str(pubst_x+1)+"\nSport Code\t\t\t: ",pubstlist[0+pubst_x][0])
                print("Sport Name\t\t\t: ",pubstlist[0+pubst_x][1])
                print("Sport Hourly Rate\t\t: ",pubstlist[0+pubst_x][2])
                print("Sport's Sport Center Code\t: ",pubstlist[0+pubst_x][3])
                print("Sport's Sport Center Name\t: ",pubstlist[0+pubst_x][4])
                pubst_x = pubst_x + 1
            pubstx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(pubstx == 0):
                ps_func()
            else:
                main_menu()
        else:
            import os
            filesize = os.path.getsize("Sport_Center_BranchC_Sports.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nCurrently No Sports Available in this Sport Center !!!\nEnter '0' to Public Student Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    ps_menu()
                else:
                    main_menu()
            pubstfile = open("Sport_Center_BranchC_Sports.txt","r")
            pubstlist = []
            for line in pubstfile:
                line = line.strip()
                line = line.split("\t")
                pubstlist.append(line)
            pubstfile.close()
            pubst_cnt = len(pubstlist)
            pubst_x = 0
            for i in range(pubst_cnt):
                print("\nSport Number "+str(pubst_x+1)+"\nSport Code\t\t\t: ",pubstlist[0+pubst_x][0])
                print("Sport Name\t\t\t: ",pubstlist[0+pubst_x][1])
                print("Sport Hourly Rate\t\t: ",pubstlist[0+pubst_x][2])
                print("Sport's Sport Center Code\t: ",pubstlist[0+pubst_x][3])
                print("Sport's Sport Center Name\t: ",pubstlist[0+pubst_x][4])
                pubst_x = pubst_x + 1
            pubstx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(pubstx == 0):
                ps_func()
            else:
                main_menu()

    elif(pubstuf1_opt == 2):
        print("\n\nSport Center :\n1. Sport Center Branch A\n2. Sport Center Branch B\n3. Sport Center Branch C\n4. All Sport Center")
        ss_no = int(input("Enter Choosen Sport Center : "))
        while(ss_no > 4 or ss_no < 1):
            ss_no = int(input("Wrong Input !!!\nEnter Choosen Sport Center : "))
        if(ss_no == 1):
            import os
            filesize = os.path.getsize("Sport_Center_BranchA_Schedule.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nCurrently No Schedule Available in this Sport Center !!!\nEnter '0' to Public Student Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    ps_menu()
                else:
                    main_menu()
            pubstfile1 = open("Sport_Center_BranchA_Schedule.txt","r")
            pubstlist1 = []
            for line in pubstfile1:
                line = line.strip()
                line = line.split("\t")
                pubstlist1.append(line)
            #print(pubstlist1)
            pubstfile1.close()
            pubst1_cnt = len(pubstlist1)
            pubst1_x = 0
            for i in range (pubst1_cnt):
                print("\nSchedule Number "+str(pubst1_x+1)+"\nSchedule ID\t\t\t: ",pubstlist1[0+pubst1_x][0])
                print("Coach ID\t\t\t: ",pubstlist1[0+pubst1_x][1])
                print("Coach Name\t\t\t: ",pubstlist1[0+pubst1_x][2])
                print("Coach's Sport Name\t\t: ",pubstlist1[0+pubst1_x][3])
                print("Coach Sport Center Code\t\t: ",pubstlist1[0+pubst1_x][4])
                print("Coach Sport Center Name\t\t: ",pubstlist1[0+pubst1_x][5])
                print("Time (dd/MM/yy/hh:mm - hh:mm)\t: ",pubstlist1[0+pubst1_x][6])
                pubst1_x = pubst1_x + 1
            pubstx1 = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(pubstx1 == 0):
                ps_func()
            else:
                main_menu()

        elif(ss_no == 2):
            import os
            filesize = os.path.getsize("Sport_Center_BranchB_Schedule.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nCurrently No Schedule Available in this Sport Center !!!\nEnter '0' to Public Student Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    ps_menu()
                else:
                    main_menu()
            pubstfile1 = open("Sport_Center_BranchB_Schedule.txt","r")
            pubstlist1 = []
            for line in pubstfile1:
                line = line.strip()
                line = line.split("\t")
                pubstlist1.append(line)
            #print(pubstlist1)
            pubstfile1.close()
            pubst1_cnt = len(pubstlist1)
            pubst1_x = 0
            for i in range (pubst1_cnt):
                print("\nSchedule Number "+str(pubst1_x+1)+"\nSchedule ID\t\t\t: ",pubstlist1[0+pubst1_x][0])
                print("Coach ID\t\t\t\t: ",pubstlist1[0+pubst1_x][1])
                print("Coach Name\t\t\t: ",pubstlist1[0+pubst1_x][2])
                print("Coach's Sport Name\t\t: ",pubstlist1[0+pubst1_x][3])
                print("Coach Sport Center Code\t\t: ",pubstlist1[0+pubst1_x][4])
                print("Coach Sport Center Name\t\t: ",pubstlist1[0+pubst1_x][5])
                print("Time (dd/MM/yy/hh:mm - hh:mm)\t: ",pubstlist1[0+pubst1_x][6])
                pubst1_x = pubst1_x + 1
            pubstx1 = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(pubstx1 == 0):
                ps_func()
            else:
                main_menu()

        elif (ss_no == 3):
            import os
            filesize = os.path.getsize("Sport_Center_BranchC_Schedule.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nCurrently No Schedule Available in this Sport Center !!!\nEnter '0' to Public Student Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    ps_menu()
                else:
                    main_menu()
            pubstfile1 = open("Sport_Center_BranchC_Schedule.txt","r")
            pubstlist1 = []
            for line in pubstfile1:
                line = line.strip()
                line = line.split("\t")
                pubstlist1.append(line)
            #print(pubstlist1)
            pubstfile1.close()
            pubst1_cnt = len(pubstlist1)
            pubst1_x = 0
            for i in range (pubst1_cnt):
                print("\nSchedule Number "+str(pubst1_x+1)+"\nSchedule ID\t\t\t: ",pubstlist1[0+pubst1_x][0])
                print("Coach ID\t\t\t\t: ",pubstlist1[0+pubst1_x][1])
                print("Coach Name\t\t\t: ",pubstlist1[0+pubst1_x][2])
                print("Coach's Sport Name\t\t: ",pubstlist1[0+pubst1_x][3])
                print("Coach Sport Center Code\t\t: ",pubstlist1[0+pubst1_x][4])
                print("Coach Sport Center Name\t\t: ",pubstlist1[0+pubst1_x][5])
                print("Time (dd/MM/yy/hh:mm - hh:mm)\t: ",pubstlist1[0+pubst1_x][6])
                pubst1_x = pubst1_x + 1
            pubstx1 = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(pubstx1 == 0):
                ps_func()
            else:
                main_menu()

        else:
            import os
            filesize = os.path.getsize("All_Sport_Center_Schedule.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nCurrently No Schedule Available in this Sport Center !!!\nEnter '0' to Public Student Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    ps_menu()
                else:
                    main_menu()
        
            pubstfile1 = open("All_Sport_Center_Schedule.txt","r")
            pubstlist1 = []
            for line in pubstfile1:
                line = line.strip()
                line = line.split("\t")
                pubstlist1.append(line)
            #print(pubstlist1)
            pubstfile1.close()
            pubst1_cnt = len(pubstlist1)
            pubst1_x = 0
            for i in range (pubst1_cnt):
                print("\nSchedule Number "+str(pubst1_x+1)+"\nSchedule ID\t\t\t: ",pubstlist1[0+pubst1_x][0])
                print("Coach ID\t\t\t\t: ",pubstlist1[0+pubst1_x][1])
                print("Coach Name\t\t\t: ",pubstlist1[0+pubst1_x][2])
                print("Coach's Sport Name\t\t: ",pubstlist1[0+pubst1_x][3])
                print("Coach Sport Center Code\t\t: ",pubstlist1[0+pubst1_x][4])
                print("Coach Sport Center Name\t\t: ",pubstlist1[0+pubst1_x][5])
                print("Time (dd/MM/yy/hh:mm - hh:mm)\t: ",pubstlist1[0+pubst1_x][6])
                pubst1_x = pubst1_x + 1
            pubstx1 = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(pubstx1 == 0):
                ps_func()
            else:
                main_menu()
    else:
        ps_menu()




#NEW STUDENT REGISTER [def newst_reg():]
def newst_reg():
    print("\n\n\t***REGISTRATION PAGE***")
    code5 = "RT" #For Student ID
    regstufile1 = open("Student_user_pass.txt","a")
    regstufile2 = open("Student_info.txt","a")
    regstufile3 = open("Student_user_pass.txt","r")
    regstufile4 = open("Student_info.txt","r")
    stuserlist = []
    stuidlist = []

    for line in regstufile3 :
        line = line.strip()
        line = line.split("\t")
        stuserlist.append(line[0])
    #print(stuserlist)
    for line in regstufile4 :
        line = line.strip()
        line = line.split("\t")
        stuidlist.append(line[0])
    #print(stuidlist)
    regstufile3.close()
    regstufile4.close()
    stu_user = input("Enter Username : ")
    while stu_user in stuserlist:
        stu_user = input("\nUsername Taken !!!\nEnter Username : ")
    stu_pass = input("Enter Password : ")
    minword = len(stu_pass)
    #print(minword)
    while(minword < 8 or minword > 16):
        stu_pass=input("\nThe password Range is 8 - 16 Character\nExample : password123\nEnter Password : ")
        minword = len(stu_pass)
    stu_id = input("\nWITHOUT 'RT' (JUST NUMBER) !!!\nRange for Student ID 100 - 999\nEnter Student ID : ")
    while(int(stu_id) > 999 or int(stu_id) < 100 or code5+stu_id in stuidlist):
        stu_id = input("\nWrong Number or ID Exist!!!\nWITHOUT 'RT' (JUST NUMBER) !!!\nRange for Student ID 100 - 999\nEnter Student ID : ")
    stu_nm = input("Enter Student Name : ")
    stu_ad = input("Enter Student Address : ")
    stu_pn = input("Enter Student Phone Number : ")
    print("\nAvailable Sport to add : ")
    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
    print(sp_namelist)
    stu_sn= input("\nEnter Student Sport Name\t\t: ")
    while(stu_sn not in sp_namelist):
        stu_sn = input("\nWrong Option !!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Sport Name\t\t: ")
    regstufile1.write(stu_user+"\t"+stu_pass+"\n")
    regstufile2.write(code5+stu_id+"\t"+stu_user+"\t"+stu_nm+"\t"+stu_ad+"\t"+stu_pn+"\t"+stu_sn+"\n")
    regstufile1.close()
    regstufile2.close()
    endreg_opt = int(input("\nSuccesfull Register :)\nEnter '0' to Log-in Page or 'ANY NUMBER' to Public Student Menu : "))
    if(endreg_opt == 0):
        stulog()
    else:
        ps_menu()



#STUDENT LOGIN PAGE [def stulog():]
def stulog():
    print("\n\n\t***Student Log-In Page***")
    logfile1 = open("Student_user_pass.txt","r")
    loglist = []

    for line in logfile1:
        line = line.strip()
        line = line.split("\t")
        loglist.append(line)
    #print(loglist)
    logfile1.close()
    log_cnt = len(loglist)
    log_x = 0
    log_flag = 0
    user_log = input("\nUsername : ")
    pass_log = input("Password : ")
    for i in range (log_cnt):
        if(user_log in  loglist[0+log_x] and pass_log in loglist[0+log_x]):
            log_flag = 1
        log_x = log_x + 1
    if(log_flag == 1):
        astulog_menu(user_log)# AFTER LOGIN STUDENT FUNC MENU [astulog_menu(user_log)]
    else:
        faillog = int(input("\nAccount Error !!!\nWrong Account or Account not Exist\nEnter '0' to Try Again or 'ANY NUMBER' to Public Student Menu  : "))
        if(faillog == 0):
            stulog()
        else:
            ps_menu()



#REGISTERED STUDENT MENU / AFTER LOGIN STUDENT MENU [def astulog_menu(user_log):]
def astulog_menu(user_log):
    #print(user_log)
    print("\n\nSUCCESS LOGIN :)\n\nRegistered Student Option :\n1. View Detail\n2. Modify Self Record\n3. Provide Feedback and Star Coach\n4. Public Student Menu\n5. Exit")
    alogmenu_opt = int(input("\nEnter Your Option : "))
    while (alogmenu_opt > 5 or alogmenu_opt < 1):
        alogmenu_opt = int(input("\nWrong Option !!!\nEnter Your Option : "))
    if(alogmenu_opt == 1):
        astulog_f1(user_log)    #REGISTERED STUDENT F1 - VIEW DETAIL [astulog_f1(user_log)]
    elif(alogmenu_opt == 2):
        astulog_f2(user_log)    #RESGISTED STUDENT F2 - MODIFY SELF RECORD [astulog_f2(user_log)]
    elif(alogmenu_opt == 3):
        astulog_f3(user_log)    #REGISTERD STUDENT F3 - prov feed and rate [astulog_f3(user_log)]
    elif(alogmenu_opt == 4):
        ps_menu()   #PUBLIC STUDENT MENU
    else:
        exit()

    

#REGISTERED STUDENT F1 - VIEW DETAIL [def astulog_f1(user_log):
def astulog_f1(user_log):
    #print(user_log)
    print("\n\n\t***Registered Student Function - View Detail\n\nDetail Option :\n1. Coach\n2. Self-Record\n3. Registered Sport Schedule\n4. Registered Student Menu")
    alogstu_opt = int(input("Enter Your Option : "))
    while (alogstu_opt > 4 or alogstu_opt < 1):
        alogstu_opt = int(input("\nWrong Option !!!\nEnter Your Option : "))
    if(alogstu_opt == 1):
            import os
            filesize = os.path.getsize("All_Sport_Center_Coach.txt")
            #print(filesize)
            while (filesize == 0):
                nosize_opt = int(input("\nNo Coach Exist in this Sport Center !!!\nEnter '0' to Registered Student Menu or 'ANY NUMBER' to Main Menu : "))
                if( nosize_opt == 0 ):
                    astulog_menu(user_log)  #REGISTERED STUDENT FUNC MENU [astulog_menu(user_log):]
                else:
                    main_menu()
            dcofile = open("All_Sport_Center_Coach.txt","r")
            dcolist = []
            for line in dcofile:
                line = line.strip()
                line = line.split("\t")
                dcolist.append(line)
            dcofile.close()
            #print(dcolist)
            dco_cnt = len(dcolist)
            dco_x = 0
            for i in range (dco_cnt):
                print("\nCoach Number "+str(dco_x+1)+"\nCoach ID\t\t\t\t: ",dcolist[0+dco_x][0])
                print("Coach Name\t\t\t\t: ",dcolist[0+dco_x][1])
                print("Coach Joined Date (dd/MM/yy)\t\t: ",dcolist[0+dco_x][2])
                print("Coach Terminated Date (dd/MM/yy)\t: ",dcolist[0+dco_x][3])
                print("Coach Hourly Rate\t\t\t: ",dcolist[0+dco_x][4])
                print("Coach Phone Number\t\t\t: ",dcolist[0+dco_x][5])
                print("Coach Address\t\t\t\t: ",dcolist[0+dco_x][6])
                print("Coach Sport Center Code\t\t\t: ",dcolist[0+dco_x][7])
                print("Coach Sport Center Name\t\t\t: ",dcolist[0+dco_x][8])
                print("Coach Sport Code\t\t\t: ",dcolist[0+dco_x][9])
                print("Coach Sport Name\t\t\t: ",dcolist[0+dco_x][10])
                print("Coach Rating\t\t\t\t: ",dcolist[0+dco_x][11])
                dco_x = dco_x + 1
            dcox = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
            if(dcox == 0):
                astulog_f1(user_log)     #REGISTERED FUNC 1 MENU [astulog_f1(user_log)
            else:
                main_menu()  #MAIN MENU

    elif(alogstu_opt == 2):
        testuser = user_log
        #print(testuser)
        rstfile = open("Student_info.txt","r")
        rstlist = []
        for line in rstfile:
            line = line.strip()
            line = line.split("\t")
            if(testuser in line):
                rstlist.append(line)
        #print(rstlist)
        rstfile.close()
        print("\nStudent ID\t\t: ",rstlist[0][0])
        print("Student Username\t: ",rstlist[0][1])
        print("Student Name\t\t: ",rstlist[0][2])
        print("Student Address\t\t: ",rstlist[0][3])
        print("Student Phone Number\t: ",rstlist[0][4])
        print("Student Sport Name\t: ",rstlist[0][5])
        rstx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(rstx == 0):
            astulog_f1(user_log)     #REGISTERED FUNC MENU [astulog_f1(user_log)
        else:
            main_menu()      #MAIN MENU

    elif(alogstu_opt == 3):
        import os
        filesize = os.path.getsize("All_Sport_Center_Schedule.txt")
        #print(filesize)
        while (filesize == 0):
            nosize_opt = int(input("\nNo Schedule Exist !!!\nEnter '0' to Admin Func Menu or 'ANY NUMBER' to Main Menu : "))
            if( nosize_opt == 0 ):
                astulog_menu(user_log)  #REGISTERED STUDENT FUNC 1 [astulog_menu(user_log):]
            else:
                main_menu()     #MAIN MENU
        testuser = user_log
        rstfile = open("Student_info.txt","r")
        rstfile1 = open("All_Sport_Center_Schedule.txt","r")
        rstlist = []
        rstlist1 = []
        for line in rstfile:
            line = line.strip()
            line = line.split("\t")
            if(testuser in line):
                rstlist.append(line[5])
        print(rstlist)
        testsp = rstlist[0]
        #print(testsp)
        for line in rstfile1:
            line = line.strip()
            line = line.split("\t")
            if(testsp in line):
                rstlist1.append(line)
        #print(rstlist1)
        rstfile.close()
        rstfile1.close()
        rst1_x = 0
        rstcnt = len(rstlist1)
        if(rstcnt == 0):
            rstx = int(input("\nCurrently No Schedule for Your Selected Sport\nEnter '0' to Registered Student Menu or 'ANY NUMBER' to Main Menu : "))
            if(rstx == 0):
                astulog_menu(user_log)   #REGISTERED FUNC MENU [astulog_menu(user_log)
            else:
                main_menu()  #MAIN MENU
        
        for i in range(rstcnt):
            print("\nSchedule Number "+str(rst1_x+1)+"\nSchedule ID\t\t\t: ",rstlist1[0+rst1_x][0])
            print("Coach ID\t\t\t: ",rstlist1[0+rst1_x][1])
            print("Coach Name\t\t\t: ",rstlist1[0+rst1_x][2])
            print("Sport Name\t\t\t: ",rstlist1[0+rst1_x][3])
            print("Sport Center Code\t\t: ",rstlist1[0+rst1_x][4])
            print("Sport Center Name\t\t: ",rstlist1[0+rst1_x][5])
            print("Time (dd/MM/yy/hh:mm - hh:mm)\t: ",rstlist1[0+rst1_x][6])
            rst1_x = rst1_x + 1
        rstx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
        if(rstx == 0):
            astulog_f1(user_log) #REGISTERED FUNC 1 [astulog_f1(user_log)
        else:
            main_menu() #MAIN MENU    
    else:
        astulog_menu(user_log) #REGISTERED FUNC MENU [astulog_menu(user_log)
                 


#REGISTERED STUDENT F2 - MODIFY SELF RECORD [def astulog_f2(user_log):]
def astulog_f2(user_log):
    #print(user_log)
    testuser = user_log
    print("\n\n\t***Modify Self Record***")
    modstfile = open("Student_info.txt","r")
    modstfile2 = open("Student_info.txt","r")
    modstlist = []
    for line in modstfile:
        line = line.strip()
        line = line.split("\t")
        if(testuser in line):
            modstlist.append(line)
    #print(modstlist)
    mod6 = modstlist[0][0]
    modstfile.close()
    mod1 = input("Enter Student Name : ")
    mod2 = input("Enter Student Address : ")
    mod3 = input("Enter Student Phone Number : ")
    print("\nAvailable Sport to add : ")
    sp_namelist = ["Swimming","Badminton","Football","Archery","Gymnastics","Volleyball","Basketball","Cricket","Tennis","Table Tennis"]
    print(sp_namelist)
    mod4 = input("Enter Student Sport Name : ")
    while (mod4 not in sp_namelist):
        mod4 = input("\nWrong Option !!!\nPlease Enter Exactly Same Word Like in Option :)\nEnter Student Sport Name\t: ")
    modread = modstfile2.readlines()
    mod_file = ""
    for line in modread:
        if(testuser in line):
            line = mod6+"\t"+testuser+"\t"+mod1+"\t"+mod2+"\t"+mod3+"\t"+mod4+"\n"
        mod_file = mod_file + line
    modstfile2.close()
    #print(mod_file)
    modstfile3 = open("Student_info.txt","w")
    modstfile3.write(mod_file)
    modstfile3.close()
    modx = int(input("\nEnter '0' to Continue or 'ANY NUMBER' to Main Menu : "))
    if(modx == 0):
        astulog_menu(user_log)   #REGISTERED FUNC MENU [astulog_menu(user_log)
    else:
        main_menu()      #MAIN MENU   



#REGISTERED STUDENT F3 - PROVIDE FEEDBACK AND GIVE RATING (def astulog_f3(user_log):]
def astulog_f3(user_log):
    #print(user_log)
    import os
    filesize = os.path.getsize("All_Sport_Center_Coach.txt")
    #print(filesize)
    while (filesize == 0):
        nosize_opt = int(input("\nNo Coach Exist in this Sport Center !!!\nEnter '0' to Registered Student Menu or 'ANY NUMBER' to Main Menu : "))
        if(nosize_opt == 0 ):
            astulog_menu(user_log)      #REGISTERED STUDENT FUNC MENU [astulog_menu(user_log):]
        else:
            main_menu()         #MAIN MENU
    testuser = user_log
    print("\n\n\t***FEEDBACK AND RATING***")
    prffile = open("Student_info.txt","r")         #clossed
    prffile0 = open("All_Sport_Center_Coach.txt","r") #closed
    prffile1 = open("Student_Feedback_Rating.txt","a")  #closed
    prffile2 = open("Student_Feedback_Rating.txt","r")  #closed
    prffile3 = open("All_Sport_Center_Coach.txt","r") #closed
    prffile4 = open("All_Sport_Center_Coach.txt","r")#closed
    prffile6 = open("Sport_Center_BranchA_Coach.txt","r")#closed
    prffile8 = open("Sport_Center_BranchB_Coach.txt","r")#closed
    prffile10 = open("Sport_Center_BranchC_Coach.txt","r")#closed
    prflist = []
    prflist1 = []
    for line in prffile:
        line = line.strip()
        line = line.split("\t")
        if(testuser in line):       #b12 change to testuser
            prflist.append(line)
    #print(prflist)
    prffile.close
    testsn = prflist[0][5]
    #print(testsn)

    for line in prffile0:
        line = line.strip()
        line = line.split("\t")
        if(testsn in line):
            prflist1.append(line[0])
            prflist1.append(line[1])
    print("\nAvailable Coach ID, Name : ")
    print(prflist1)
    prffile0.close()
    testnum = len(prflist1)
    while (testnum == 0):
        empopt = int(input("No Coach Available for your Selected Sport !!!\nEnter '0' to Registered Student Menu or 'ANY NUMBER' to Main Menu : "))
        if(empopt == 0):
            astulog_menu(user_log)       #REGISTERED STUDENT MENU
        else:
            main_menu()          #MAIN MENU

    prfco = input("\nEnter Choosen Coach ID (WITH 'CC') : ")
    while (prfco not in prflist1):
        prfco = input("\nCoach ID not Exist !!!\nEnter Choosen Coach : ")
    prffeed = input("Enter Feedback for Coach : ")
    prfrate = input("\nRange 1 - 5 !!!\nEnter Rating for Coach : ")
    while (int(prfrate) > 5 or int(prfrate) < 1):
        prfrate = input("\nWrong Rating !!!\nRange 1 - 5 !!!\nEnter Rating for Coach : ")
    prffile1.write(prfco+"\t"+testuser+"\t"+testsn+"\t"+prffeed+"\t"+prfrate+"\n")
    prffile1.close()

    prf_cnt = 0
    tot_rate = 0
    for line in prffile2:
        line = line.strip()
        line = line.split("\t")
        if prfco in line: 
            tot_rate = tot_rate + int(line[4])
            prf_cnt = prf_cnt + 1
    #print(prf_cnt)
    #print(tot_rate)
    avert = round(tot_rate / prf_cnt,2)
    #print(avert)
    prffile2.close()

    prflist2 = []
    for line in prffile3:
        line = line.strip()
        line = line.split("\t")
        if(prfco in line): 
            prflist2.append(line)
            #print(prflist2)
            d1 = prflist2[0][0]
            d2 = prflist2[0][1]
            d3 = prflist2[0][2]
            d4 = prflist2[0][3]
            d5 = prflist2[0][4]
            d6 = prflist2[0][5]
            d7 = prflist2[0][6]
            d8 = prflist2[0][7]
            d9 = prflist2[0][8]
            d10 =prflist2[0][9]
            d11 = prflist2[0][10]
    prffile3.close()
    newallco = ""
    prfdata = prffile4.readlines()
    for line in prfdata:
        if(prfco in line): 
            #print(line)
            line = d1+"\t"+d2+"\t"+d3+"\t"+d4+"\t"+d5+"\t"+d6+"\t"+d7+"\t"+d8+"\t"+d9+"\t"+d10+"\t"+d11+"\t"+str(avert)+"\n"
            #print(line)
        newallco += line
    #print(newallco)        
    prffile4.close()
    prffilewr = open("All_Sport_Center_Coach.txt","w")
    prffilewr.write(newallco)
    prffilewr.close()

    newallco1 = ""
    prfdata = prffile6.readlines()
    for line in prfdata:
        if(prfco in line): 
            #print(line)
            line = d1+"\t"+d2+"\t"+d3+"\t"+d4+"\t"+d5+"\t"+d6+"\t"+d7+"\t"+d8+"\t"+d9+"\t"+d10+"\t"+d11+"\t"+str(avert)+"\n"
            #print(line)
        newallco1 += line
    #print(newallco1)        
    prffile6.close()
    prffilewr1 = open("Sport_Center_BranchA_Coach.txt","w")
    prffilewr1.write(newallco1)
    prffilewr1.close()

    newallco2 = ""
    prfdata = prffile8.readlines()
    for line in prfdata:
        if(prfco in line): 
            #print(line)
            line = d1+"\t"+d2+"\t"+d3+"\t"+d4+"\t"+d5+"\t"+d6+"\t"+d7+"\t"+d8+"\t"+d9+"\t"+d10+"\t"+d11+"\t"+str(avert)+"\n"
            #print(line)
        newallco2 += line
    #print(newallco2)        
    prffile8.close()
    prffilewr2 = open("Sport_Center_BranchB_Coach.txt","w")
    prffilewr2.write(newallco2)
    prffilewr2.close()
        
    newallco3 = ""
    prfdata = prffile10.readlines()
    for line in prfdata:
        if(prfco in line):
            #print(line)
            line = d1+"\t"+d2+"\t"+d3+"\t"+d4+"\t"+d5+"\t"+d6+"\t"+d7+"\t"+d8+"\t"+d9+"\t"+d10+"\t"+d11+"\t"+str(avert)+"\n"
            #print(line)
        newallco3 += line
    #print(newallco3)        
    prffile10.close()
    prffilewr3 = open("Sport_Center_BranchC_Coach.txt","w")
    prffilewr3.write(newallco3)
    prffilewr3.close()
    srfx = int(input("\nEnter '0' to Registered Student Func Menu or 'ANY NUMBER' to Main Menu : "))
    if(srfx == 0):
        astulog_menu(user_log)       #REGISTERED FUNC MENU [astulog_menu(user_log)
    else:
        main_menu()      #MAIN MENU


main_menu()















    



 




        
        
    
    
                
            
            
            

                                

                
            
                    
                           
            
                
















                        
