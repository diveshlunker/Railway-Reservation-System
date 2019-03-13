#_________________HEADER_________________
from pickle import load,dump 
import time 
import random
import os
#_______________________CLASS TICKETS_________________
class tickets:
    def __init__(self):
        self.no_ofac1stclass=0
        self.totaf=0
        self.no_ofac2ndclass=0
        self.no_ofac3rdclass=0
        self.no_ofsleeper=0
        self.no_oftickets=0
        self.name=''
        self.age=''
        self.resno=0
        self.status=''       \
#__________RETURNS RESERVATION NUMBER___________
    def ret(self):
        return(self.resno)

#___________RETURNS NAME_____________
    def retname(self):
        return(self.name)
#_________________DISPLAYS THE DATA_______________
    def display(self):
        f=0
        fin1=open("tickets.dat","rb")
        if not fin1:
            print "ERROR"
        else:
            print
            n=int(raw_input("ENTER PNR NUMBER : "))
            print "\n\n"
            print ("FETCHING DATA . . .".center(80))
            time.sleep(1)
            print
            print('PLEASE WAIT...!!'.center(80))
            time.sleep(1)
            os.system('cls')
            try:
                while True:
                    tick=load(fin1)
                    if(n==tick.ret()):
                        f=1
                        print "="*80
                        print("PNR STATUS".center(80))
                        print"="*80
                        print 
                        print "PASSENGER'S NAME :",tick.name
                        print
                        print "PASSENGER'S AGE :",tick.age
                        print
                        print "PNR NO :",tick.resno
                        print
                        print "STATUS :",tick.status
                        print
                        print "NO OF SEATS BOOKED : ",tick.no_oftickets
                        print
            except:
                pass
            fin1.close()
            if(f==0):
                print
                print "WRONG PNR NUMBER..!!"
                print                
    def pending(self):
         self.status="WAITING LIST"
         print "PNR NUMBER :",self.resno
         print
         time.sleep(1.2)
         print "STATUS = ",self.status
         print
         print "NO OF SEATS BOOKED : ",self.no_oftickets
         print
    def confirmation (self):
        self.status="CONFIRMED"
        print "PNR NUMBER : ",self.resno
        print
        time.sleep(1.5)
        print "STATUS = ",self.status
        print
    def cancellation(self):
        z=0
        f=0
        fin=open("tickets.dat","rb")
        fout=open("temp.dat","ab")
        print
        r= int(raw_input("ENTER PNR NUMBER : "))
        try:
            while(True):
                tick=load(fin)
                z=tick.ret()
                if(z!=r):
                    dump(tick,fout)
                elif(z==r):
                     f=1
        except:
            pass
        fin.close()
        fout.close()
        os.remove("tickets.dat")
        os.rename("temp.dat","tickets.dat")
        if (f==0):
            print
            print "NO SUCH RESERVATION NUMBER FOUND"
            print
            time.sleep(2)
            os.system('cls')        
        else:
            print
            print "TICKET CANCELLED"
            print
#__________________RESERVES THE TICKET_______________
    def reservation(self):
        trainno=int(raw_input("ENTER THE TRAIN NO:"))
        z=0
        f=0
        fin2=open("trdetails.dat")
        fin2.seek(0)
        if not fin2:
            print "ERROR"
        else:            
            try:
                while True:
                    tr=load(fin2)
                    z=tr.gettrainno()
                    n=tr.gettrainname()
                    if (trainno==z):
                        print
                        print "TRAIN NAME IS : ",n
                        f=1
                        print
                        print "-"*80
                        no_ofac1st=tr.getno_ofac1stclass()
                        no_ofac2nd=tr.getno_ofac2ndclass()
                        no_ofac3rd=tr.getno_ofac3rdclass()
                        no_ofsleeper=tr.getno_ofsleeper()
                    if(f==1):
                        fout1=open("tickets.dat","ab")
                        print
                        self.name=raw_input("ENTER THE PASSENGER'S NAME ")
                        print
                        self.age=int(raw_input("PASSENGER'S AGE : "))
                        print
                        print"\t\t SELECT A CLASS YOU WOULD LIKE TO TRAVEL IN :- "
                        print "1.AC FIRST CLASS"
                        print
                        print "2.AC SECOND CLASS"
                        print
                        print "3.AC THIRD CLASS"
                        print
                        print "4.SLEEPER CLASS"
                        print
                        c=int(raw_input("\t\t\tENTER YOUR CHOICE = "))
                        os.system('cls')
                        amt1=0
                        if(c==1):
                            self.no_oftickets=int(raw_input("ENTER NO_OF FIRST CLASS AC SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=1000*self.no_oftickets
                                i=i+1
                            print
                            print "PROCESSING. .",
                            time.sleep(0.5)
                            print ".",
                            time.sleep(0.3)
                            print'.'
                            time.sleep(2)
                            os.system('cls')
                            print "TOTAL AMOUNT TO BE PAID = ",amt1
                            self.resno=int(random.randint(1000,2546))
                            x=no_ofac1st-self.totaf
                            print
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break
                        elif(c==2):
                            self.no_oftickets=int(raw_input("ENTER NO_OF SECOND CLASS AC SEATS TO BE BOOKED :  "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=900*self.no_oftickets
                                i=i+1
                            print
                            print "PROCESSING. .",
                            time.sleep(0.5)
                            print ".",
                            time.sleep(0.3)
                            print'.'
                            time.sleep(2)
                            os.system('cls')
                            print "TOTAL AMOUNT TO BE PAID = ",amt1
                            self.resno=random.randint(1000,2546)
                            x=no_ofac2nd-self.totaf
                            print
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break
                       
                        elif(c==3):
                            self.no_oftickets=int(raw_input("ENTER NO_OF THIRD CLASS AC SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=800*self.no_oftickets
                                i=i+1
                            print
                            print "PROCESSING. .",
                            time.sleep(0.5)
                            print ".",
                            time.sleep(0.3)
                            print'.'
                            time.sleep(2)
                            os.system('cls')
                            print "TOTAL AMOUNT TO BE PAID = ",amt1
                            self.resno=random.randint(1000,2546)
                            x=no_ofac3rd-self.totaf
                            print
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break                      
                        elif(c==4):
                            self.no_oftickets=int(raw_input("ENTER NO_OF SLEEPER CLASS SEATS TO BE BOOKED : "))
                            i=1
                            while(i<=self.no_oftickets):
                                self.totaf=self.totaf+1
                                amt1=550*self.no_oftickets
                                i=i+1
                            print
                            print "PROCESSING. .",
                            time.sleep(0.5)
                            print ".",
                            time.sleep(0.3)
                            print'.'
                            time.sleep(2)
                            os.system('cls')
                            print "TOTAL AMOUNT TO BE PAID = ",amt1
                            self.resno=random.randint(1000,2546)
                            x=no_ofsleeper-self.totaf
                            print
                            if(x>0):
                                self.confirmation()
                                dump(self,fout1)
                                break
                            else:
                                self.pending()
                                dump(tick,fout1)
                                break        
            except:
                pass
            if(f==0):
                time.sleep(2)
                print"\n\n\n\n\n\n\t\t\t\tNO SUCH TRAINS FOUND !!"
                time.sleep(2)
                print
                print
                print  
#____________________CLASS TRAIN__________________
class train:
    def __init__(self):
        self.trainno=0
        self.no_ofac1stclass=0
        self.no_ofac2ndclass=0
        self.no_ofac3rdclass=0
        self.no_ofsleeper=0
        self.totalseats=0
        self.trainname=''
        self.startingpt=""
        self.destination=''        
#_______________________GETS INPUT__________________
    def getinput(self):
        print"="*80
        print "\t\t\t  ENTER THE TRAIN DETAILS"
        print
        print"="*80
        self.trainname=raw_input("ENTER THE TRAIN NAME : ").upper()
        print
        self.trainno=int(raw_input("ENTER THE TRAIN NUMBER: "))
        print
        self.no_ofac1stclass=int(raw_input("ENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED : "))
        print
        self.no_ofac2ndclass=int(raw_input("ENTER NO_OF AC SECOND CLASS SEATS TO BE RESERVED : "))
        print
        self.no_ofac3rdclass=int(raw_input("ENTER NO_OF AC THIRD CLASS SEATS TO BE RESERVED : "))
        print
        self.no_ofsleeper=int(raw_input("ENTER NO_OF SLEEPER CLASS SEATS TO BE RESERVED : "))
        print
        self.startingpt=raw_input("ENTER THE STARTING POINT : ")
        print
        self.destination=raw_input("ENTER THE DESTINATION POINT : ")
        os.system('cls')   
    #___________________DISPALYS  DATA_________________
    def output(self):
        print"="*80
        print
        print "THE ENTERED TRAIN NAME IS : ",self.trainname
        print "THE TRAIN  NUMBER IS : ",self.trainno
        print "STARTING POINT ENTERED IS : ",self.startingpt
        print "DESTINATION POINT ENTERED IS : ",self.destination
        print "NO_OF AC FIRST CLASS SEATS RESERVED ARE :",self.no_ofac1stclass
        print "NO_OF AC SECOND CLASS SEATS RESERVED ARE :",self.no_ofac2ndclass
        print "NO_OF AC THIRD CLASS SEATS RESERVED ARE :",self.no_ofac3rdclass
        print "NO_OF SLEEPER CLASS SEATS RESERVED ARE :",self.no_ofsleeper
        print
        print "="*80
#_______RETURNS TRAIN NAME,NUMBER,CLASS,STARTING PT.,DESTINATION____________
    def gettrainname(self):
        return (self.trainname)
    def gettrainno(self):
        return(self.trainno)
    def getno_ofac1stclass(self):
        return(self.no_ofac1stclass)
    def getno_ofac2ndclass(self):
         return(self.no_ofac2ndclass)
    def getno_ofac3rdclass(self):
        return(self.no_ofac3rdclass)
    def getno_ofsleeper(self):
        return (self.no_ofsleeper)
    def getstartingpt(self):
        return (self.startingpt)
    def getdestination(self):
        return (self.destination)



#_________________MAIN____________________
#__________CALLS ALL THE FUNCTIONS ACCORDING TO USER CHOICE.______________________
def menu():
    tr=train()
    tick=tickets()
    print
    print "WELCOME TO ASIMA AGENCY".center(80)   
    while True:
            print
            print "="*80
            print " \t\t\t\t  RAILWAY"
            print
            print "="*80
            print
            print "\t\t\t1. **UPDATE TRAIN DETAILS."
            print
            print "\t\t\t2. TRAIN DETAILS. "
            print
            print "\t\t\t3. RESERVATION OF TICKETS."
            print
            print "\t\t\t4. CANCELLATION OF TICKETS. "
            print
            print "\t\t\t5. DISPLAY PNR STATUS."
            print
            print "\t\t\t6. QUIT."
            print"** - office use......"
            ch=int(raw_input("\t\t\tENTER YOUR CHOICE : "))
            os.system('cls')
            print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tLOADING. .",
            time.sleep(1)
            print ("."),
            time.sleep(0.5)
            print (".")
            time.sleep(2)
            os.system('cls')
            if ch==1:
                j="*****"
                r=raw_input("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tENTER THE PASSWORD: ")
                os.system('cls')
                if (j==r):
                    x='y'
                    while (x.lower()=='y'):
                        fout=open("trdetails.dat","ab")
                        tr.getinput()
                        dump(tr,fout)
                        fout.close()
                        print"\n\n\n\n\n\n\n\n\n\n\n\t\t\tUPDATING TRAIN LIST PLEASE WAIT . .",
                        time.sleep(1)
                        print ("."),
                        time.sleep(0.5)
                        print ("."),
                        time.sleep(2)
                        os.system('cls')
                        print "\n\n\n\n\n\n\n\n\n\n\n"
                        x=raw_input("\t\tDO YOU WANT TO ADD ANY MORE TRAINS DETAILS ? ")
                        os.system('cls')
                    continue
                elif(j<>r):
                    print"\n\n\n\n\n"
                    print "WRONG PASSWORD".center(80)
            elif ch==2:              
                fin=open("trdetails.dat",'rb')
                if not fin:
                    print "ERROR"
                else:
                    try:
                        while True:
                            print"*"*80
                            print"\t\t\t\tTRAIN DETAILS"
                            print"*"*80
                            print
                            tr=load(fin)
                            tr.output()



                            raw_input("PRESS ENTER TO VIEW NEXT TRAIN DETAILS")
                            os.system('cls')
                    except EOFError:
                         pass            
            elif ch==3:
                print'='*80
                print "\t\t\t\tRESERVATION OF TICKETS"
                print'='*80
                print
                tick.reservation()                
            elif ch==4:
                print"="*80
                print"\t\t\t\tCANCELLATION OF TICKETS"
                print
                print"="*80
                print
                tick.cancellation()
            elif ch==5:
                print "="*80
                print("PNR STATUS".center(80))
                print"="*80
                print
                tick.display()
            elif ch==6:
                quit()               
            raw_input("PRESS ENTER TO GO TO BACK MENU".center(80))
            os.system('cls')
print"\t\t\t\tWELCOME TO GSS RAILWAYS"
print
print"\n\n\n\n\t\t\tBy:-"
print"\t\t\t\tASIMA \n
print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tLOADING. .",
time.sleep(1)
print ("."),
time.sleep(0.5)
print (".")
time.sleep(2)
os.system('cls')
menu()
print”\t\t\t\t\n\n\n\n\n\t THANK YOU.....”
print”\n\t\t\t\DONE BY:-“
print”\t\t\t\t ASIMA”
print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tLOADING. .",
time.sleep(1)
print ("."),
time.sleep(0.5)
print (".")
time.sleep(2)
os.system('cls')

