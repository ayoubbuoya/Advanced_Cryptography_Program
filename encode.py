from cryptography.fernet import Fernet
from pyfiglet import figlet_format as Figlet
import sys
#Home Function       [1]
def banner() :
    '''   Home  Function '''
    global message
    print("")
    print("-"*74)
    print(Figlet("   Buoya   "))
    print("")
    print("-"*74)
    print("")
    print("="*37)
    print("")
    message=input("        Enter Your Message : ")
    print("")
    print("="*37)
    print("")
#Generate Key           [2]
def Write_Key() :
    '''Generate A key And save It Into A file'''
    global key
    key=Fernet.generate_key()
    with open("key.key","wb") as Key_File :
        Key_File.write(key)

#Encrypt Fuction     [3]   
def encrypt_msg(message,key) :
    '''Encrypt Entered Msg '''
    global Encrypt_Msg
    message=message.encode()
    #Intialise Fernet Class
    f=Fernet(key)
    #Encrypt Msg
    Encrypt_Msg=f.encrypt(message)
    #Convert From byte To Str
    Encrypt_Msg=Encrypt_Msg.decode()
    print("+"*37)
    print("")
    print(Encrypt_Msg)
    print("")
    print("+"*37)
    Ask_User()
#Function          [3].{2}
def Put_In_File(filename,file_data) :
    '''Put The Encrypt Message In A File '''
    File=open(filename,"wb")
    #Convert To byte
    File.write(file_data.encode())
#Function Ask User  [3].{1} 
def Ask_User() :
    '''Ask User If he would To Save The Encypt Msg In A file '''
    global User_Ans
    global filename
    print("")
    print("Do You Want To Put This Enrypt_Msg In A File ? ")
    print("")
    print("Answer With Y Or N ")
    print("")
    User_Ans=input("Ans>> ") 
    #Check Answer User
    if User_Ans=="y" or User_Ans=="Y" or User_Ans=="Yes" or User_Ans=="yes" :
       print("")
       print("Enter File Name : ")
       print("")
       filename=input()
       Put_In_File(filename,Encrypt_Msg)
    else :
       print("")
       print("Ok,End Program ")
       sys.exit()
#######$##$$Main Fuction###
def main() : 
    #First,Banner Fuction 
    banner()   
    #Second,Write Key
    Write_Key()
    #Finaly Encrypt message
    encrypt_msg(message,key)
########Start_Program#######
main()        