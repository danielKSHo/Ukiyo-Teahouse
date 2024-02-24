#Importing the Tkinter module
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Importing the Tkcalendar module (use 'pip install pillow' in the terminal)
from tkcalendar import *

#Importing the Pillow module (use 'pip install pillow' in the terminal)
from PIL import ImageTk, Image

#Importing the Datetime module 
from datetime import datetime

#Importing the Random module
import random

#####Adding "Start" Screen#####
def Start():
    StartWindow(Tk())

#####Start Screen###################################################################################################################
class StartWindow:
    
    #Creating Screen
    def __init__(self, startScreen):
        self.startScreen = startScreen
        self.startScreen.resizable(False, False)
        self.startScreen.configure(background = "#DC7CA1")

    #Title
        #Tab
        self.startScreen.title("Ukiyo Teahouse")
        #Screen
        self.startTitle = Label(self.startScreen, text = "Ukiyo Teahouse", width = 30, height = 2, background = "#ffffff", font = ("Tahoma", 48))
        self.startTitle.grid(row = 2, columnspan = 6)
        #Border
        self.startTopBorder = LabelFrame(self.startScreen, width = 816, height = 20, background = "#211F34")
        self.startTopBorder.grid(row = 1, columnspan = 6)
        self.startBottomBorder = LabelFrame(self.startScreen, width = 816, height = 20, background = "#211F34")
        self.startBottomBorder.grid(row = 3, columnspan = 6)

    #Screen Spacing
        self.startTopSpace = LabelFrame(self.startScreen, width = 816, height = 58, background = "#DC7CA1")
        self.startTopSpace.grid(row = 0, columnspan = 6)
        self.startMiddleSpace = LabelFrame(self.startScreen, width = 816, height = 91, background = "#DC7CA1")
        self.startMiddleSpace.grid(row = 4, columnspan = 6)
        self.startBottomSpace = LabelFrame(self.startScreen, width = 816, height = 91, background = "#DC7CA1")
        self.startBottomSpace.grid(row = 7, columnspan = 6)

    #Start Frame
        self.startFrame = LabelFrame(self.startScreen, padx = 10, pady = 10, background = "#211F34")
        self.startFrame.grid(row = 5, column = 1, rowspan = 2, columnspan = 4)

        #Buttons
        
            #Login
        self.startLoginButton = Button(self.startFrame, text = "Login", padx = 124, pady = 14, font = ("Tahoma", 28), command = self.Login)
        self.startLoginButton.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
            #Create Customer
        self.startCreateCustButton = Button(self.startFrame, text = "Create Customer Account", padx = 0, pady = 14, font = ("Tahoma", 28), command = self.CCA)
        self.startCreateCustButton.grid(row = 1, column = 0,  columnspan = 3, padx = 10, pady = 10)
            #Menu
        self.startMenuButton = Button(self.startFrame, text = "Menu", padx = 0, pady = 60, font = ("Tahoma", 28), command = self.Menu)
        self.startMenuButton.grid(row = 0, column = 3, rowspan = 2, padx = 10, pady = 10)
        self.startScreen.mainloop()

#####Adding "Login" Screen#####
    def Login(self):
        self.Login = Toplevel(self.startScreen)
        self.app = LoginWindow(self.Login)

#####Adding "Create Customer Account" Screen#####
    def CCA(self):
        self.CCA = Toplevel(self.startScreen)
        self.app = CCAWindow(self.CCA)

#####Adding "Menu" Screen#####
    def Menu(self):
        self.Menu = Toplevel(self.startScreen)
        self.app = MenuWindow(self.Menu)

#####Login Screen###################################################################################################################
class LoginWindow:
    
    #Creating Screen
    def __init__(self, loginScreen):
        self.loginScreen = loginScreen
        self.loginScreen.resizable(False, False)
        self.loginScreen.configure(background = "#DC7CA1")

    #Title

        #Tab
        self.loginScreen.title("Login")
        #Screen
        self.loginTitle = Label(self.loginScreen, text = "Login", width = 30, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.loginTitle.grid(row = 1, columnspan = 6)
        #Border
        self.loginTopBorder = LabelFrame(self.loginScreen, width = 816, height = 15, background = "#211F34")
        self.loginTopBorder.grid(row = 0, columnspan = 6)
        self.loginBottomBorder = LabelFrame(self.loginScreen, width = 816, height = 15, background = "#211F34")
        self.loginBottomBorder.grid(row = 2, columnspan = 6)

    #Screen Spacing
        self.loginTopSpace = LabelFrame(self.loginScreen, width = 816, height = 91, background = "#DC7CA1")
        self.loginTopSpace.grid(row = 3, columnspan = 6)
        self.loginBottomSpace = LabelFrame(self.loginScreen, width = 816, height = 91, background = "#DC7CA1")
        self.loginBottomSpace.grid(row = 5, columnspan = 6)

    #Login Frame
        self.loginFrame = LabelFrame(self.loginScreen, padx = 10, pady = 10, background = "#211F34")
        self.loginFrame.grid(row = 4, columnspan = 4)

        #Username
        
            #Label
        self.loginUsernameLabel = Label(self.loginFrame, text = "Username", width = 8, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 28))
        self.loginUsernameLabel.grid(row = 0, column = 0, padx = 10, pady = 5)
            #Entry
        self.loginUsernameEntry = Entry(self.loginFrame, width = 15, borderwidth = 3, font = ("Tahoma", 28))
        self.loginUsernameEntry.grid(row = 0, column = 1, padx = 10, pady = 5)

        #Password
        
            #Label
        self.loginPasswordLabel = Label(self.loginFrame, text = "Password", width = 8, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 28))
        self.loginPasswordLabel.grid(row = 1, column = 0, padx = 10, pady = 5)
            #Entry
        self.loginPasswordEntry = Entry(self.loginFrame, width = 15, borderwidth = 3, font = ("Tahoma", 28))
        self.loginPasswordEntry.grid(row = 1, column = 1, padx = 10, pady = 5)
        
        #Buttons

            #Login
        self.loginButton = Button(self.loginFrame, text = "Login", padx = 165, pady = 3, font = ("Tahoma", 28), command = self.Login_ReadRecord)
        self.loginButton.grid(row = 2, column = 0,  columnspan = 2, padx = 10, pady = 10)
        
            #Reset Password
        self.loginResetPasswordButton = Button(self.loginFrame, text = "Reset Password", padx = 100, font = ("Tahoma", 28), command = self.ResetPassword)
        self.loginResetPasswordButton.grid(row = 3, column = 0,  columnspan = 2, padx = 10, pady = 10)
            
    def Login_ReadRecord(self):
        #Passing the input entry boxes through to the Login_ReadRecord function

        global loginUsername
        loginUsername = self.loginUsernameEntry.get()
        self.loginPassword = self.loginPasswordEntry.get()

        #Presence Check For Username and Password
        if len(loginUsername) == 0 or len(self.loginPassword) == 0:
            self.loginMessage = "Fill in all login details"

        else:
            
            self.UsernameFound = False
            
            ##Staff Account##

            #Converting text file row into a 2 dimensional array
            self.StaffAccountFile = open("StaffAccount.txt","r")
            self.StaffAccountList = [row.split(',') for row in self.StaffAccountFile]

            #Searching for existing staff Username
            self.StaffAccountFile = open("StaffAccount.txt","r")
            self.Count = -1
            for row in self.StaffAccountFile:
                self.Count += 1

                #Checking staff Username through every row 
                if loginUsername == self.StaffAccountList[self.Count][1]:
                    
                    #Username found in a specific row
                    self.UsernameFound = True
                    self.loginMessage = "Username in\nStaffAccount Record " + str(self.Count)

                    #Checking if the Password matches with the Username in the same row
                    if self.loginPassword == self.StaffAccountList[self.Count][2]:
                        #Password matches with the Username
                        messagebox.showinfo("Access Granted", "Access Granted!\nYou now have access to: " + loginUsername + "'s Staff Account")
                        self.loginMessage = "Proceed to\nthe next screen"
                        self.StaffAccount()
                        
                    else:
                        #Password does not match with the Username
                        messagebox.showinfo("Access Denied", "Access Denied!\nPassword does not match with the Username")
                        self.loginMessage = "Enter the correct\nPassword for the\nUsername: " + loginUsername

                else:
                    pass

            self.StaffAccountFile.close()

            ##Customer Account##

            #Converting text file row into a 2 dimensional array
            self.CustomerAccountFile = open("CustomerAccount.txt","r")
            self.CustomerAccountList = [row.split(',') for row in self.CustomerAccountFile]

            #Searching for existing staff Username
            self.CustomerAccountFile = open("CustomerAccount.txt","r")
            self.Count = -1
            for row in self.CustomerAccountFile:
                self.Count += 1
                
                #Checking customer Username through every row 
                if loginUsername == self.CustomerAccountList[self.Count][1]:
                    
                    #Username found in a specific row
                    self.UsernameFound = True
                    self.loginMessage = "Username in\nCustomer Account Record " + str(self.Count)

                    #Checking if the Password matches with the Username in the same row
                    if self.loginPassword == self.CustomerAccountList[self.Count][2]:
                        #Password matches with the Username
                        messagebox.showinfo("Access Granted", "Access Granted!\nYou now have access to: " + loginUsername + "'s Customer Account")
                        self.loginMessage = "Proceed to\nthe next screen"
                        global CustomerID
                        CustomerID = self.CustomerAccountList[self.Count][0]
                        self.CustomerAccount()
                        
                    else:
                        #Password does not match with the Username
                        messagebox.showinfo("Access Denied", "Access Denied!\nPassword does not match with the Username")
                        self.loginMessage = "Enter the correct\nPassword for the\nUsername: " + loginUsername

                else:
                    pass

            self.CustomerAccountFile.close()

            #Done searching for existing Username
            if self.UsernameFound == False:
                #No Username found
                messagebox.showinfo("Access Denied", "There is no Username\nknown as: " + loginUsername)
                self.loginMessage = "Enter a valid Username"
  
        #Login Message Frame
        self.loginSearchFrame = LabelFrame(self.loginScreen, padx = 10, pady = 10, background = "#211F34")
        self.loginSearchFrame.grid(row = 4, column = 5, columnspan = 1)
        
        #Login Message
        self.loginSearchLabel = Label(self.loginSearchFrame, text = self.loginMessage, width = 20, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 20))
        self.loginSearchLabel.grid(row = 0, column = 0, padx = 10, pady = 5)

#####Adding "Reset Password" Screen#####
    def ResetPassword(self):
            self.ResetPassword = Toplevel(self.loginScreen)
            self.app = ResetPasswordWindow(self.ResetPassword)

#####Adding "Staff Account" Screen#####
    def StaffAccount(self):
            self.StaffAccount = Toplevel(self.loginScreen)
            self.app = StaffAccountWindow(self.StaffAccount)

#####Adding "Customer Account" Screen#####
    def CustomerAccount(self):
            self.CustomerAccount = Toplevel(self.loginScreen)
            self.app = CustomerAccountWindow(self.CustomerAccount)

#####Reset Password Screen###################################################################################################################
class ResetPasswordWindow:
    
    #Creating Screen
    def __init__(self, rpScreen):
        self.rpScreen = rpScreen
        self.rpScreen.resizable(False, False)
        self.rpScreen.configure(background = "#DC7CA1")

    #Title

        #Tab
        self.rpScreen.title("Reset Password")
        #Screen
        self.rpTitle = Label(self.rpScreen, text = "Reset Password", width = 30, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.rpTitle.grid(row = 1, columnspan = 6)
        #Border
        self.rpTopBorder = LabelFrame(self.rpScreen, width = 816, height = 15, background = "#211F34")
        self.rpTopBorder.grid(row = 0, columnspan = 6)
        self.rpBottomBorder = LabelFrame(self.rpScreen, width = 816, height = 15, background = "#211F34")
        self.rpBottomBorder.grid(row = 2, columnspan = 6)

    #Screen Spacing
        self.rpTopSpace = LabelFrame(self.rpScreen, width = 816, height = 91, background = "#DC7CA1")
        self.rpTopSpace.grid(row = 3, columnspan = 6)
        self.rpBottomSpace = LabelFrame(self.rpScreen, width = 816, height = 91, background = "#DC7CA1")
        self.rpBottomSpace.grid(row = 5, columnspan = 6)

    #Login Frame
        self.rpFrame = LabelFrame(self.rpScreen, padx = 10, pady = 10, background = "#211F34")
        self.rpFrame.grid(row = 4, columnspan = 4)

        #Username
        
            #Label
        self.rpUsernameLabel = Label(self.rpFrame, text = "Username", width = 10, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 28))
        self.rpUsernameLabel.grid(row = 0, column = 0, padx = 10, pady = 5)
            #Entry
        self.rpUsernameEntry = Entry(self.rpFrame, width = 15, borderwidth = 3, font = ("Tahoma", 28))
        self.rpUsernameEntry.grid(row = 0, column = 1, padx = 10, pady = 5)

        #Backup Key
        
            #Label
        self.rpBackupKeyLabel = Label(self.rpFrame, text = "Backup Key", width = 10, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 28))
        self.rpBackupKeyLabel.grid(row = 1, column = 0, padx = 10, pady = 5)
            #Entry
        self.rpBackupKeyEntry = Entry(self.rpFrame, width = 15, borderwidth = 3, font = ("Tahoma", 28))
        self.rpBackupKeyEntry.grid(row = 1, column = 1, padx = 10, pady = 5)

            #Login
        self.loginButton = Button(self.rpFrame, text = "Reset", padx = 165, pady = 3, font = ("Tahoma", 28), command = self.RP_ReadRecord)
        self.loginButton.grid(row = 2, column = 0,  columnspan = 2, padx = 10, pady = 10)
                    
    def RP_ReadRecord(self):
        #Passing the input entry boxes through to the RP_ReadRecord function

        self.rpUsername = self.rpUsernameEntry.get()
        self.rpBackupKey = self.rpBackupKeyEntry.get()

        #Presence Check For Username and Backup Key
        if len(self.rpUsername) == 0 or len(self.rpBackupKey) == 0:
            self.rpMessage = "Fill in all reset\npassword details"

        else:
            
            self.UsernameFound = False

             ##Staff Account##

            #Converting text file row into a 2 dimensional array
            self.StaffAccountFile = open("StaffAccount.txt","r")
            self.StaffAccountList = [row.split(',') for row in self.StaffAccountFile]

            #Searching for existing staff Username
            self.StaffAccountFile = open("StaffAccount.txt","r")
            self.Count = -1
            for row in self.StaffAccountFile:
                self.Count += 1
                
                #Checking customer Username through every row 
                if self.rpUsername == self.StaffAccountList[self.Count][1]:
                    
                    #Username found in a specific row
                    self.UsernameFound = True
                    self.rpMessage = "Username in\nCustomer Account Record " + str(self.Count)

                    #Checking if the Backup Key matches with the Username in the same row
                    if self.rpBackupKey == (self.StaffAccountList[self.Count][3])[0:-1]:
                        #Backup Key matches with the Username
                        messagebox.showinfo("Access Granted", "Access Granted!\nYou now can reset the password for: " + self.rpUsername + "'s Staff Account")
                        self.rpMessage = "Enter the\nNew Password"
                        self.StaffAccountPassword = self.StaffAccountList[self.Count][2]
                        self.NewPassword()
                        
                    else:
                        #Backup Key does not match with the Username
                        messagebox.showinfo("Access Denied", "Access Denied!\nThe Backup Key does not match with the Username")
                        self.rpMessage = "Enter the correct\nBackup Key for the\nUsername: " + self.rpUsername

                else:
                    pass

            self.StaffAccountFile.close()

            ##Customer Account##

            #Converting text file row into a 2 dimensional array
            self.CustomerAccountFile = open("CustomerAccount.txt","r")
            self.CustomerAccountList = [row.split(',') for row in self.CustomerAccountFile]

            #Searching for existing staff Username
            self.CustomerAccountFile = open("CustomerAccount.txt","r")
            self.Count = -1
            for row in self.CustomerAccountFile:
                self.Count += 1
                
                #Checking customer Username through every row 
                if self.rpUsername == self.CustomerAccountList[self.Count][1]:
                    
                    #Username found in a specific row
                    self.UsernameFound = True
                    self.rpMessage = "Username in\nCustomer Account Record " + str(self.Count)

                    #Checking if the Backup Key matches with the Username in the same row
                    if self.rpBackupKey == (self.CustomerAccountList[self.Count][3])[0:-1]:
                        #Backup Key matches with the Username
                        messagebox.showinfo("Access Granted", "Access Granted!\nYou now can reset the password for: " + self.rpUsername + "'s Customer Account")
                        self.rpMessage = "Enter the\nNew Password"
                        self.CustomerAccountPassword = self.CustomerAccountList[self.Count][2]
                        self.NewPassword()
                        
                    else:
                        #Backup Key does not match with the Username
                        messagebox.showinfo("Access Denied", "Access Denied!\nThe Backup Key does not match with the Username")
                        self.rpMessage = "Enter the correct\nBackup Key for the\nUsername: " + self.rpUsername

                else:
                    pass

            self.CustomerAccountFile.close()

            #Done searching for existing Username
            if self.UsernameFound == False:
                #No Username found
                messagebox.showinfo("Access Denied", "There is no Username\nknown as: " + self.rpUsername)
                self.rpMessage = "Enter a valid Username"
  
        #Reset Password Message Frame
        self.rpSearchFrame = LabelFrame(self.rpScreen, padx = 10, pady = 10, background = "#211F34")
        self.rpSearchFrame.grid(row = 4, column = 5, columnspan = 1)
        
        #Reset Password Message
        self.rpSearchLabel = Label(self.rpSearchFrame, text = self.rpMessage, width = 20, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 20))
        self.rpSearchLabel.grid(row = 0, column = 0, padx = 10, pady = 5)

    def NewPassword(self):
        
        #New Password
        
            #Label
        self.rpNewPasswordLabel = Label(self.rpFrame, text = "New\nPassword", width = 10, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 28))
        self.rpNewPasswordLabel.grid(row = 0, column = 0, padx = 10, pady = 5)
            #Entry
        self.rpNewPasswordEntry = Entry(self.rpFrame, width = 15, borderwidth = 3, font = ("Tahoma", 28))
        self.rpNewPasswordEntry.grid(row = 0, column = 1, padx = 10, pady = 5)

        #Confirm New Password
        
            #Label
        self.rpConfirmNewPasswordLabel = Label(self.rpFrame, text = "Confirm New\nPassword", width = 10, pady = 15, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 28))
        self.rpConfirmNewPasswordLabel.grid(row = 1, column = 0, padx = 10, pady = 5)
            #Entry
        self.rpConfirmNewPasswordEntry = Entry(self.rpFrame, width = 15, borderwidth = 3, font = ("Tahoma", 28))
        self.rpConfirmNewPasswordEntry.grid(row = 1, column = 1, padx = 10, pady = 5)

            #Submit
        self.submitButton = Button(self.rpFrame, text = "Submit", padx = 165, pady = 3, font = ("Tahoma", 28), command = self.RP_AmendRecord)
        self.submitButton.grid(row = 2, column = 0,  columnspan = 2, padx = 10, pady = 10)

    def RP_AmendRecord(self):
        #Passing the input entry boxes through to the RP_AmendRecord function
        self.rpNewPassword = self.rpNewPasswordEntry.get()
        self.rpConfirmNewPassword = self.rpConfirmNewPasswordEntry.get()

        #Presense Check
        if len(self.rpNewPassword) == 0 or len(self.rpConfirmNewPassword) == 0:
            messagebox.showinfo("Could not update record", "Fill in both password entries")

        else:

            #Same Password Check
            if self.rpNewPassword != self.rpConfirmNewPassword:
                messagebox.showinfo("Could not update record", "Both password entries must be the same")

            else:
                
                #Try command is used so the correct file (customer or staff) is read and amended
                
                try:
                    #Opens the staff account file for reading
                    self.StaffAccountFile = open("StaffAccount.txt","r")

                    #Reading the content of the file using read() function and storing them in a new variable
                    self.StaffAccountPasswordRead = self.StaffAccountFile.read()

                    #Searching and replacing the existing password using the replace() function
                    self.StaffAccountPasswordRead = self.StaffAccountPasswordRead.replace(self.StaffAccountPassword, self.rpNewPassword)
                    self.StaffAccountFile.close()

                    #Opens the staff account file for writing
                    self.StaffAccountFile = open("StaffAccount.txt","w")

                    #Writing the replaced data in the text file
                    self.StaffAccountFile.write(self.StaffAccountPasswordRead)    
                    self.StaffAccountFile.close()

                    #Message for user that the existing password has been replaced
                    messagebox.showinfo("Staff record has been amended", "The Password: " + self.StaffAccountPassword + "\nhas been replaced by\nthe Password: " + self.rpNewPassword)

                except:
                    #Opens the customer account file for reading
                    self.CustomerAccountFile = open("CustomerAccount.txt","r")

                    #Reading the content of the file using read() function and storing them in a new variable
                    self.CustomerAccountPasswordRead = self.CustomerAccountFile.read()

                    #Searching and replacing the existing password using the replace() function
                    self.CustomerAccountPasswordRead = self.CustomerAccountPasswordRead.replace(self.CustomerAccountPassword, self.rpNewPassword)
                    self.CustomerAccountFile.close()

                    #Opens the customer account file for writing
                    self.CustomerAccountFile = open("CustomerAccount.txt","w")

                    #Writing the replaced data in the text file
                    self.CustomerAccountFile.write(self.CustomerAccountPasswordRead)
                    self.CustomerAccountFile.close()

                    #Message for user that the existing password has been replaced
                    messagebox.showinfo("Customer reocrd has been amended", "The Password: " + self.CustomerAccountPassword + "\nhas been replaced by\nthe Password: " + self.rpNewPassword)

                self.rpScreen.destroy()
                
#####Staff Account Screen###################################################################################################################
class StaffAccountWindow:

    #Creating Screen
    def __init__(self, saScreen):
        self.saScreen = saScreen     
        self.saScreen.resizable(False, False)
        self.saScreen.configure(background = "#734599")

        #Title

        #Tab
        self.saScreen.title("Staff Account")
        #Screen
        self.staffTitle = Label(self.saScreen, text = "Staff Account", width = 20, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.staffTitle.grid(row = 1, columnspan = 6)
        #Border
        self.staffTopBorder = LabelFrame(self.saScreen, width = 546, height = 15, background = "#211F34")
        self.staffTopBorder.grid(row = 0, columnspan = 6)
        self.staffBottomBorder = LabelFrame(self.saScreen, width = 546, height = 15, background = "#211F34")
        self.staffBottomBorder.grid(row = 2, columnspan = 6)

        #Screen Spacing
        self.saTopSpace = LabelFrame(self.saScreen, width = 546, height = 71, background = "#734599")
        self.saTopSpace.grid(row = 3, columnspan = 6)
        self.saBottomSpace = LabelFrame(self.saScreen, width = 546, height = 71, background = "#734599")
        self.saBottomSpace.grid(row = 5, columnspan = 6)

        #Menu Frame
        self.saFrame = LabelFrame(self.saScreen, padx = 10, pady = 10, background = "#211F34")
        self.saFrame.grid(row = 4, columnspan = 6)

        #Buttons

            #Create Staff Account
        self.saCSAButton = Button(self.saFrame, text = "Create Staff Account", width = 18, pady = 5, font = ("Tahoma", 24), command = self.CSA)
        self.saCSAButton.grid(row = 0, column = 0, padx = 10, pady = 10)
            #Staff Account HIstory
        self.saSADButton = Button(self.saFrame, text = "Staff Account Details", width = 18, pady = 5,  font = ("Tahoma", 24), command = self.SAD)
        self.saSADButton.grid(row = 1, column = 0, padx = 10, pady = 10)
            #Customer Invoice History
        self.saCIHButton = Button(self.saFrame, text = "Customer Invoice History", width = 18, pady = 5, font = ("Tahoma", 24), command = self.CIHs)
        self.saCIHButton.grid(row = 2, column = 0, padx = 10, pady = 10)
            #Stock
        self.saStockButton = Button(self.saFrame, text = "Stock", width = 10, pady = 5, font = ("Tahoma", 24), )#command = Drinks)
        self.saStockButton.grid(row = 0, column = 1, padx = 10, pady = 10)
            #Job Roles
        self.saJobRolesButton = Button(self.saFrame, text = "Job Roles", width = 10, pady = 5, font = ("Tahoma", 24), command = self.JR)
        self.saJobRolesButton.grid(row = 1, column = 1, padx = 10, pady = 10)
            #Coupon Codes
        self.saCouponCodesButton = Button(self.saFrame, text = "Coupon Codes", width = 10, pady = 5, font = ("Tahoma", 24), )#command = Drinks)
        self.saCouponCodesButton.grid(row = 2, column = 1, padx = 10, pady = 10)

#####Adding "Create Staff Account" Screen#####
    def CSA(self):
        self.CSA = Toplevel(self.saScreen)
        self.app = CSAWindow(self.CSA)

#####Adding "Staff Account Details" Screen#####
    def SAD(self):
        self.SAD = Toplevel(self.saScreen)
        self.app = SADWindow(self.SAD)
        
#####Adding "Customer Invoice History" Screen#####
    def CIHs(self):
        self.CIHs = Toplevel(self.saScreen)
        self.app = CIHsWindow(self.CIHs)

#####Adding "Job Roles" Screen#####
    def JR(self):
        self.JR = Toplevel(self.saScreen)
        self.app = JRWindow(self.JR)

#####Create Staff Account Screen####################################################################################################
class CSAWindow:
        
    #Creating screen
    def __init__(self,csaScreen):
        self.csaScreen = csaScreen           
        self.csaScreen.resizable(False, False)
        self.csaScreen.configure(background = "#734599")

    #Title

        #Tab
        self.csaScreen.title("Create Staff Account") 
        #Screen
        self.csaTitle = Label(self.csaScreen, text = "Create Staff Account", width = 30, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.csaTitle.grid(row = 1, columnspan = 11)
        #Border
        self.csaTopBorder = LabelFrame(self.csaScreen, width = 816, height = 15, background = "#211F34")
        self.csaTopBorder.grid(row = 0, columnspan = 11)
        self.csaBottomBorder = LabelFrame(self.csaScreen, width = 816, height = 15, background = "#211F34")
        self.csaBottomBorder.grid(row = 2, columnspan = 11)

    #Screen Spacing
        self.csaTopSpace = LabelFrame(self.csaScreen, width = 816, height = 45, background = "#734599")
        self.csaTopSpace.grid(row = 3, columnspan = 11)
        self.csaBottomSpace = LabelFrame(self.csaScreen, width = 816, height = 45, background = "#734599")
        self.csaBottomSpace.grid(row = 5, columnspan = 11)

    #Staff Details Section

        #Frame
        self.csaStaffDetailsFrame = LabelFrame(self.csaScreen, padx = 10, pady = 10, background = "#211F34")
        self.csaStaffDetailsFrame.grid(row = 4, column = 1, columnspan = 4)

            #Title 
        self.csaStaffDetailsTitle = Label(self.csaStaffDetailsFrame, text = "Staff Details", width = 15, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.csaStaffDetailsTitle.grid(row = 0, columnspan = 2)

            #Forname

                #Label
        self.csaFornameLabel = Label(self.csaStaffDetailsFrame, text = "Forename", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaFornameLabel.grid(row = 1, column = 0, padx = 5, pady = 5)
                #Entry Box
        self.csaFornameEntry = Entry(self.csaStaffDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaFornameEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
        
            #Surname

                #Label
        self.csaSurnameLabel = Label(self.csaStaffDetailsFrame, text = "Surname", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaSurnameLabel.grid(row = 2, column = 0, padx = 5, pady = 5)
                #Entry Box
        self.csaSurnameEntry = Entry(self.csaStaffDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaSurnameEntry.grid(row = 2, column = 1, padx = 5, pady = 5)
        
            #Phone Number

                #Label
        self.csaPhoneNoLabel = Label(self.csaStaffDetailsFrame, text = "Phone\nNumber", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaPhoneNoLabel.grid(row = 3, column = 0, padx = 5)
                #Entry Box
        self.csaPhoneNoEntry = Entry(self.csaStaffDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaPhoneNoEntry.grid(row = 3, column = 1, padx = 5)
        
            #Email

                #Label
        self.csaEmailLabel = Label(self.csaStaffDetailsFrame, text = "Email", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaEmailLabel.grid(row = 4, column = 0, padx = 5, pady = 5)
                #Entry Box
        self.csaEmailEntry = Entry(self.csaStaffDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaEmailEntry.grid(row = 4, column = 1, padx = 5, pady = 5)
        
            #Address
        
                #Label
        self.csaAddressLabel = Label(self.csaStaffDetailsFrame, text = "Address", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaAddressLabel.grid(row = 5, column = 0, padx = 5, pady = 5)
                #Entry Box
        self.csaAddressEntry = Entry(self.csaStaffDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaAddressEntry.grid(row = 5, column = 1, padx = 5, pady = 5)
        
            #Postcode

                #Label
        self.csaPostcodeLabel = Label(self.csaStaffDetailsFrame, text = "Postcode", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaPostcodeLabel.grid(row = 6, column = 0, padx = 5, pady = 5)
                #Entry Box
        self.csaPostcodeEntry = Entry(self.csaStaffDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaPostcodeEntry.grid(row = 6, column = 1, padx = 5, pady = 5)


            #Opening files and creating lists for the dropdown menus
        
                #Converting text file row into lists
        self.JobRolesFile = open("JobRoles.txt","r")
        self.JobRolesList = [row.split(',') for row in self.JobRolesFile]

                #Creating Job ID list
        self.csaJobIDList = []

                #Searching for existing jobIDs
        self.JobRolesFile = open("JobRoles.txt","r")
        self.Count = -1
        for row in self.JobRolesFile:
            self.Count += 1
            self.csaJobIDList.append(self.JobRolesList[self.Count][0])

        self.csaJobID = StringVar()
        self.csaJobID.set(self.csaJobIDList[0])

                #Creating Job Type list
        self.csaJobTypeList = ["Full-Time", "Part-Time", "Temporary"]
        
        self.csaJobType = StringVar()
        self.csaJobType.set(self.csaJobTypeList[0])

            #Job ID
        
                #Label
        self.dropLabel = Label(self.csaStaffDetailsFrame, text = "Job ID", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dropLabel.grid(row = 7, column = 0, padx = 5, pady = 5)
                #Dropdown Menu
        self.drop = OptionMenu(self.csaStaffDetailsFrame, self.csaJobID, *self.csaJobIDList)
        self.drop.grid(row = 7, column = 1, padx = 5, pady = 5)

            #Job Type
        
                #Label
        self.drop1Label = Label(self.csaStaffDetailsFrame, text = "Job Type", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drop1Label.grid(row = 8, column = 0, padx = 5, pady = 5)
                #Dropdown Menu
        self.drop1 = OptionMenu(self.csaStaffDetailsFrame, self.csaJobType, *self.csaJobTypeList)
        self.drop1.grid(row = 8, column = 1, padx = 5, pady = 5)

        
    #Login Details Section

        #Frame
        self.csaLoginDetailsFrame = LabelFrame(self.csaScreen, padx = 10, pady = 10, background = "#211F34")
        self.csaLoginDetailsFrame.grid(row = 4, column = 6, columnspan = 4)

            #Title
        self.csaLoginDetailsTitle = Label(self.csaLoginDetailsFrame, text = "Login Details", width = 15, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.csaLoginDetailsTitle.grid(row = 0, columnspan = 2)

            #Username

                #Label
        self.csaUsernameLabel = Label(self.csaLoginDetailsFrame, text = "Username", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaUsernameLabel.grid(row = 1, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.csaUsernameEntry = Entry(self.csaLoginDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaUsernameEntry.grid(row = 1, column = 1, padx = 5, pady = 10)
        
            #Password

                #Label
        self.csaPasswordLabel = Label(self.csaLoginDetailsFrame, text = "Password", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaPasswordLabel.grid(row = 2, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.csaPasswordEntry = Entry(self.csaLoginDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaPasswordEntry.grid(row = 2, column = 1, padx = 5, pady = 10)
        
            #Backup Key

                #Label
        self.csaBackupKeyLabel = Label(self.csaLoginDetailsFrame, text = "Backup Key", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.csaBackupKeyLabel.grid(row = 4, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.csaBackupKeyEntry = Entry(self.csaLoginDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.csaBackupKeyEntry.grid(row = 4, column = 1, padx = 5, pady = 10)

        #Submit Button 
        self.csaSubmitButton = Button(self.csaLoginDetailsFrame, text = "Submit", padx = 80, font = ("Tahoma", 21), command = self.CSA_AddRecord)
        self.csaSubmitButton.grid(row = 6, columnspan = 2, padx = 10, pady = 10)

    def CSA_AddRecord(self):

        #Passing the input entry boxes through to the CSA_AddRecord function
        self.sForname = self.csaFornameEntry.get()
        self.sSurname = self.csaSurnameEntry.get()
        self.sPhoneNo = self.csaPhoneNoEntry.get()
        self.sEmail = self.csaEmailEntry.get()
        self.sAddress = self.csaAddressEntry.get()
        self.sPostcode = self.csaPostcodeEntry.get()
        self.JobID = "J#" + str(self.csaJobIDList.index(self.csaJobID.get()))
        self.JobType = self.csaJobType.get()

        self.sUsername = self.csaUsernameEntry.get()
        self.sPassword = self.csaPasswordEntry.get()
        self.sBackupKey = self.csaBackupKeyEntry.get()

        if len(self.sForname) == 0 or len(self.sSurname) == 0 or len(self.sPhoneNo) == 0 or len(self.sEmail) == 0 or len(self.sAddress) == 0 or len(self.sPostcode) == 0 or len(self.sUsername) == 0 or len(self.sPassword) == 0 or len(self.sBackupKey) == 0:
            messagebox.showinfo("Could not add new record", "Could not add new record\nFill in all Login and Staff Details")

        else:

            if len(self.sPhoneNo) != 11:
                messagebox.showinfo("Could not add new record", "Phone number must be 11 characters")
                
            else:

                try:
                    int(self.sPhoneNo)
                    intPhoneNo = True
                except ValueError:
                    messagebox.showinfo("Could not add new record", "Phone number must be an integer")
                    intPhoneNo = False

                if intPhoneNo == True:
                    #Reads all the records in the staff details file for primary key incrementation
                    self.StaffDetailsFile = open("StaffDetails.txt","r")

                    self.csaCountRow = 0

                    for row in self.StaffDetailsFile:
                        self.csaCountRow += 1

                    self.StaffDetailsFile.close()

                    #Adds a record in the staff details file
                    self.StaffDetailsFile = open("StaffDetails.txt","a")

                    self.StaffDetailsFile.write("S#" + str(self.csaCountRow + 1) + "," + self.sForname + "," + self.sSurname + "," + self.sPhoneNo + "," + self.sEmail + "," + self.sAddress + "," + self.sPostcode + "," + self.JobID + "," + self.JobType + "\n")

                    self.StaffDetailsFile.close()
                    
                    #Adds a record in the customer account file
                    self.StaffAccountFile = open("StaffAccount.txt","a")

                    self.StaffAccountFile.write("S#" + str(self.csaCountRow + 1) + "," + self.sUsername + "," + self.sPassword + "," + self.sBackupKey + "\n")

                    self.StaffAccountFile.close()

                    #Messagebox to indicate to the user that the staff account has been made
                    messagebox.showinfo("Staff Account has been made", "Staff Account: " + self.sUsername + "\nhas been made")

                    self.csaScreen.destroy()
                    
                else:
                    pass
                
#####Staff Account Details Screen###################################################################################################################
class SADWindow:

    #Creating Screen
    def __init__(self, sadScreen):
        self.sadScreen = sadScreen     
        self.sadScreen.resizable(False, False)
        self.sadScreen.configure(background = "#734599")

        #Title

        #Tab
        self.sadScreen.title("Staff Account Details")
        #Screen
        self.sadTitle = Label(self.sadScreen, text = "Staff Account Details", width = 22, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.sadTitle.grid(row = 1, columnspan = 6)
        #Border
        self.sadTopBorder = LabelFrame(self.sadScreen, width = 600, height = 15, background = "#211F34")
        self.sadTopBorder.grid(row = 0, columnspan = 6)
        self.sadBottomBorder = LabelFrame(self.sadScreen, width = 600, height = 15, background = "#211F34")
        self.sadBottomBorder.grid(row = 2, columnspan = 6)

        #Screen Spacing
        self.sadTopSpace = LabelFrame(self.sadScreen, width = 600, height = 71, background = "#734599")
        self.sadTopSpace.grid(row = 3, columnspan = 6)
        self.sadBottomSpace = LabelFrame(self.sadScreen, width = 600, height = 71, background = "#734599")
        self.sadBottomSpace.grid(row = 6, columnspan = 6)

        #Button Frame
        self.sadButtonFrame = LabelFrame(self.sadScreen, padx = 10, pady = 10, background = "#211F34")
        self.sadButtonFrame.grid(row = 4, column = 0, columnspan = 6)
        
                #Order By Label
        self.sadOrderLabel = Label(self.sadButtonFrame, text = "Order by", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.sadOrderLabel.grid(row = 4, column = 0, padx = 5, pady = 10)
        
                #Booking ID
        self.sadStaffIDButton = Button(self.sadButtonFrame, text = "ID", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_StaffID)
        self.sadStaffIDButton.grid(row = 4, column = 1, padx = 10, pady = 10)
        
                #Booking Type
        self.sadStaffTypeButton = Button(self.sadButtonFrame, text = "Forename", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_StaffForename)
        self.sadStaffTypeButton.grid(row = 4, column = 2, padx = 10, pady = 10)

                #Booking Time
        self.sadStaffSurnameButton = Button(self.sadButtonFrame, text = "Surname", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_StaffSurname)
        self.sadStaffSurnameButton.grid(row = 4, column = 3, padx = 10, pady = 10)

        #Invoice Search

        #Converting text file row into lists
        self.StaffDetailsFile = open("StaffDetails.txt","r")
        self.StaffDetailsList = [row.split(',') for row in self.StaffDetailsFile]

        self.InvoiceHistory()

    def OrderBy_StaffID(self):
        self.sadScrollbarFrame.destroy()
        self.StaffDetailsFile = open("StaffDetails.txt","r")
        self.StaffDetailsList = [row.split(',') for row in self.StaffDetailsFile]
        self.InvoiceHistory()
        
    def OrderBy_StaffForename(self):
        self.sadScrollbarFrame.destroy()
        self.StaffDetailsList = sorted(self.StaffDetailsList, key=lambda x: x[1])
        self.InvoiceHistory()
        
    def OrderBy_StaffSurname(self):
        self.sadScrollbarFrame.destroy()
        self.StaffDetailsList = sorted(self.StaffDetailsList, key=lambda x: x[2])
        self.InvoiceHistory()
        
    def InvoiceHistory(self):

        #Scrollbar Frame
        self.sadScrollbarFrame = LabelFrame(self.sadScreen, padx = 10, pady = 10, background = "#211F34")
        self.sadScrollbarFrame.grid(row = 5, column = 1, columnspan = 4)
        
        #Adding a Canvas for a Scrollbar
        self.sadCanvas = Canvas(self.sadScrollbarFrame)
        self.sadCanvas.pack(side = LEFT)

        #Adding a Scrollbar to the Canvas
        self.sadScrollbar = ttk.Scrollbar(self.sadScrollbarFrame, orient = VERTICAL, command = self.sadCanvas.yview)
        self.sadScrollbar.pack(side = RIGHT, fill = Y)
        
        #Configuring the Canvas
        self.sadCanvas.configure(yscrollcommand = self.sadScrollbar.set)
        self.sadCanvas.bind("<Configure>", lambda e: self.sadCanvas.configure(scrollregion = self.sadCanvas.bbox("all")))

        #Invoice Button Frame
        self.sadInvoiceFrame = LabelFrame(self.sadCanvas, padx = 10, pady = 10, background = "#211F34")
        self.sadInvoiceFrame.grid(row = 0, column = 0)

        self.sadCanvas.create_window((0, 0), window = self.sadInvoiceFrame)
        
        #Searching for existing staff Username
        self.StaffDetailsFile = open("StaffAccount.txt","r")

        self.sadRadioButtonVar = IntVar()
        self.sadRadioButtonVar.set(None)
    
        self.Count = -1
        for row in self.StaffDetailsFile:
           self.Count += 1

           self.sadStaffIDButton = Radiobutton(self.sadInvoiceFrame, text = self.StaffDetailsList[self.Count][0], variable = self.sadRadioButtonVar, value = self.Count + 1,
                                                 command = self.VSAD, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
           self.sadStaffIDButton.grid(row = self.Count, column = 0, padx = 20, pady = 10)
           
           self.sadStaffForename = Label(self.sadInvoiceFrame, text = self.StaffDetailsList[self.Count][1],
                                         foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
           self.sadStaffForename.grid(row = self.Count, column = 1, padx = 20, pady = 10)

           self.sadStaffSurname = Label(self.sadInvoiceFrame, text = self.StaffDetailsList[self.Count][2],
                                         foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
           self.sadStaffSurname.grid(row = self.Count, column = 2, padx = 20, pady = 10)

#####Adding "View Staff Account Details" Screen#####
    def VSAD(self):
        
        global StaffID
        StaffID = "S#" + str(self.sadRadioButtonVar.get())

        global JobID
        JobID = self.StaffDetailsList[self.sadRadioButtonVar.get() - 1][7]
        
        self.StaffDetailsFile.close()
        
        self.VSAD = Toplevel(self.sadScreen)
        self.app = VSADWindow(self.VSAD)

#####Customer Invoice History Screen for Staff Account Access###################################################################################################################
class CIHsWindow:

    #Creating Screen
    def __init__(self, cihScreen):
        self.cihScreen = cihScreen     
        self.cihScreen.resizable(False, False)
        self.cihScreen.configure(background = "#734599")

        #Title

        #Tab
        self.cihScreen.title("Customer Invoice History")
        #Screen
        self.cihTitle = Label(self.cihScreen, text = "Customer Invoice History", width = 22, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.cihTitle.grid(row = 1, columnspan = 6)
        #Border
        self.cihTopBorder = LabelFrame(self.cihScreen, width = 600, height = 15, background = "#211F34")
        self.cihTopBorder.grid(row = 0, columnspan = 6)
        self.cihBottomBorder = LabelFrame(self.cihScreen, width = 600, height = 15, background = "#211F34")
        self.cihBottomBorder.grid(row = 2, columnspan = 6)

        #Screen Spacing
        self.cihTopSpace = LabelFrame(self.cihScreen, width = 600, height = 71, background = "#734599")
        self.cihTopSpace.grid(row = 3, columnspan = 6)
        self.cihBottomSpace = LabelFrame(self.cihScreen, width = 600, height = 71, background = "#734599")
        self.cihBottomSpace.grid(row = 6, columnspan = 6)

        #Button Frame
        self.cihButtonFrame = LabelFrame(self.cihScreen, padx = 10, pady = 10, background = "#211F34")
        self.cihButtonFrame.grid(row = 4, column = 0, columnspan = 6)
        
                #Order By Label
        self.cihOrderLabel = Label(self.cihButtonFrame, text = "Order by", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cihOrderLabel.grid(row = 4, column = 0, padx = 5, pady = 10)
        
                #Booking ID
        self.cihBookingIDButton = Button(self.cihButtonFrame, text = "ID", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_BookingID)
        self.cihBookingIDButton.grid(row = 4, column = 1, padx = 10, pady = 10)
        
                #Booking Type
        self.cihBookingTypeButton = Button(self.cihButtonFrame, text = "Type", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_BookingType)
        self.cihBookingTypeButton.grid(row = 4, column = 2, padx = 10, pady = 10)

                #Booking Time
        self.cihBookingTimeButton = Button(self.cihButtonFrame, text = "Time", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_BookingTime)
        self.cihBookingTimeButton.grid(row = 4, column = 3, padx = 10, pady = 10)

        #Invoice Search

        #Converting text file row into lists
        self.CustomerBookingFile = open("CustomerBooking.txt","r")
        self.CustomerBookingList = [row.split(',') for row in self.CustomerBookingFile]

        self.InvoiceHistory()

    def OrderBy_BookingID(self):
        self.cihScrollbarFrame.destroy()
        self.CustomerBookingFile = open("CustomerBooking.txt","r")
        self.CustomerBookingList = [row.split(',') for row in self.CustomerBookingFile]
        self.InvoiceHistory()
        
    def OrderBy_BookingType(self):
        self.cihScrollbarFrame.destroy()
        self.CustomerBookingList = sorted(self.CustomerBookingList, key=lambda x: x[1])
        self.InvoiceHistory()
        
    def OrderBy_BookingTime(self):
        self.cihScrollbarFrame.destroy()
        self.CustomerBookingList = sorted(self.CustomerBookingList, key=lambda x: x[3])
        self.InvoiceHistory()
        
    def InvoiceHistory(self):

        #Scrollbar Frame
        self.cihScrollbarFrame = LabelFrame(self.cihScreen, padx = 10, pady = 10, background = "#211F34")
        self.cihScrollbarFrame.grid(row = 5, column = 1, columnspan = 4)
        
        #Adding a Canvas for a Scrollbar
        self.cihCanvas = Canvas(self.cihScrollbarFrame)
        self.cihCanvas.pack(side = LEFT)

        #Adding a Scrollbar to the Canvas
        self.cihScrollbar = ttk.Scrollbar(self.cihScrollbarFrame, orient = VERTICAL, command = self.cihCanvas.yview)
        self.cihScrollbar.pack(side = RIGHT, fill = Y)
        
        #Configuring the Canvas
        self.cihCanvas.configure(yscrollcommand = self.cihScrollbar.set)
        self.cihCanvas.bind("<Configure>", lambda e: self.cihCanvas.configure(scrollregion = self.cihCanvas.bbox("all")))

        #Invoice Button Frame
        self.cihInvoiceFrame = LabelFrame(self.cihCanvas, padx = 10, pady = 10, background = "#211F34")
        self.cihInvoiceFrame.grid(row = 0, column = 0)

        self.cihCanvas.create_window((0, 0), window = self.cihInvoiceFrame)
    
##        count = -1
##        for row in self.CustomerBookingFile:
##            count += 1
##            self.CustomerBookingList.sort(key = lambda date: datetime.strptime(date, "%m/%d/%y"))
##
##        
##        
##                                      
##        n = len(self.CustomerBookingList)
##        for index in range(1, n):
##            current = self.CustomerBookingList[index][2]
##            index2 = index
##            while index2 > 0 and self.CustomerBookingList[index2 -1][2] > current:
##                self.CustomerBookingList[index2][2] = self.CustomerBookingList[index2 -1][2]
##                index2 = index2 -1
##            self.CustomerBookingList[index2][2] = current
        #Output the results
        
        #Searching for existing staff Username
        self.CustomerBookingFile = open("CustomerBooking.txt","r")

        self.cihRadioButtonVar = IntVar()
        self.cihRadioButtonVar.set(None)
    
        self.Count = -1
        for row in self.CustomerBookingFile:
           self.Count += 1

           self.cihBookingIDButton = Radiobutton(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][0], variable = self.cihRadioButtonVar, value = self.Count + 1,
                                                 command = self.VCI, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
           self.cihBookingIDButton.grid(row = self.Count, column = 0, padx = 10, pady = 10)
           
           self.cihBookingType = Label(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][1],
                                         foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
           self.cihBookingType.grid(row = self.Count, column = 1, padx = 10, pady = 10)

           self.cihBookingDate = Label(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][2],
                                         foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
           self.cihBookingDate.grid(row = self.Count, column = 2, padx = 10, pady = 10)

           self.cihBookingTime = Label(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][3],
                                         foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
           self.cihBookingTime.grid(row = self.Count, column = 3, padx = 10, pady = 10)
    
#####Adding "Customer Invoice" Screen#####
    def VCI(self):
      
        global BookingID
        BookingID = "B#" + str(self.cihRadioButtonVar.get())

        global CustomerID
        CustomerID = (self.CustomerBookingList[self.cihRadioButtonVar.get() - 1][4])[0:-1]
        
        self.CustomerBookingFile.close()
        
        self.VCI = Toplevel(self.cihScreen)
        self.app = VCIWindow(self.VCI)

#####Create Staff Account Screen####################################################################################################
class JRWindow:
        
    #Creating screen
    def __init__(self,jrScreen):
        self.jrScreen = jrScreen           
        self.jrScreen.resizable(False, False)
        self.jrScreen.configure(background = "#734599")

    #Title

        #Tab
        self.jrScreen.title("Job Roles") 
        #Screen
        self.jrTitle = Label(self.jrScreen, text = "Job Roles", width = 30, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.jrTitle.grid(row = 1, columnspan = 6)
        #Border
        self.jrTopBorder = LabelFrame(self.jrScreen, width = 816, height = 15, background = "#211F34")
        self.jrTopBorder.grid(row = 0, columnspan = 6)
        self.jrBottomBorder = LabelFrame(self.jrScreen, width = 816, height = 15, background = "#211F34")
        self.jrBottomBorder.grid(row = 2, columnspan = 6)

    #Screen Spacing
        self.jrTopSpace = LabelFrame(self.jrScreen, width = 816, height = 45, background = "#734599")
        self.jrTopSpace.grid(row = 3, columnspan = 6)
        self.jrBottomSpace = LabelFrame(self.jrScreen, width = 816, height = 45, background = "#734599")
        self.jrBottomSpace.grid(row = 5, columnspan = 6)

    #Job Roles Section

        #Frame
        self.jrFrame = LabelFrame(self.jrScreen, padx = 10, pady = 10, background = "#211F34")
        self.jrFrame.grid(row = 4, column = 1, columnspan = 4)

            #Role

                #Label
        self.jrRoleLabel = Label(self.jrFrame, text = "Job Role", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.jrRoleLabel.grid(row = 0, column = 0, padx = 5, pady = 5)
                #Entry Box
        self.jrRoleEntry = Entry(self.jrFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.jrRoleEntry.grid(row = 0, column = 1, padx = 5, pady = 5)
        
            #Description

                #Label
        self.jrDescriptionLabel = Label(self.jrFrame, text = "Description", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.jrDescriptionLabel.grid(row = 1, column = 0, padx = 5, pady = 5)
                #Entry Box
        self.jrDescriptionEntry = Entry(self.jrFrame, width = 50, borderwidth = 3, font = ("Tahoma", 14))
        self.jrDescriptionEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

        #Submit Button 
        self.jrSubmitButton = Button(self.jrFrame, text = "Submit", padx = 80, font = ("Tahoma", 21), command = self.JR_AddRecord)
        self.jrSubmitButton.grid(row = 2, column = 1, columnspan = 2, padx = 10, pady = 10)

    def JR_AddRecord(self):

        #Passing the input entry boxes through to the JR_AddRecord function
        self.jRole = self.jrRoleEntry.get()
        self.jDescription = self.jrDescriptionEntry.get()


        if len(self.jRole) == 0 or len(self.jDescription) == 0:
            messagebox.showinfo("Could not add new record", "Could not add new record\nFill in all Login and Staff Details")

        else:
            #Reads all the records in the staff details file for primary key incrementation
            self.JobRolesFile = open("JobRoles.txt","r")

            self.jrCountRow = 0

            for row in self.JobRolesFile:
                self.jrCountRow += 1

            self.JobRolesFile.close()

            #Adds a record in the staff details file
            self.JobRolesFile = open("JobRoles.txt","a")

            self.JobRolesFile.write("J#" + str(self.jrCountRow) + "," + self.jRole + ",'" + self.jDescription + "'" + "\n")

            self.JobRolesFile.close()

            #Messagebox to indicate to the user that the staff account has been made
            messagebox.showinfo("Job Role has been added", "Job Role: " + self.jRole + "\nhas been added")

            self.jrScreen.destroy()

#####Customer Invoice History Screen for Customer Account Access###################################################################################################################
class CIHcWindow:

    #Creating Screen
    def __init__(self, cihScreen):
        self.cihScreen = cihScreen     
        self.cihScreen.resizable(False, False)
        self.cihScreen.configure(background = "#1F8EA8")

        #Title

        #Tab
        self.cihScreen.title("Customer Invoice History")
        #Screen
        self.cihTitle = Label(self.cihScreen, text = "Customer Invoice History", width = 22, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.cihTitle.grid(row = 1, columnspan = 6)
        #Border
        self.cihTopBorder = LabelFrame(self.cihScreen, width = 600, height = 15, background = "#211F34")
        self.cihTopBorder.grid(row = 0, columnspan = 6)
        self.cihBottomBorder = LabelFrame(self.cihScreen, width = 600, height = 15, background = "#211F34")
        self.cihBottomBorder.grid(row = 2, columnspan = 6)

        #Screen Spacing
        self.cihTopSpace = LabelFrame(self.cihScreen, width = 600, height = 71, background = "#1F8EA8")
        self.cihTopSpace.grid(row = 3, columnspan = 6)
        self.cihBottomSpace = LabelFrame(self.cihScreen, width = 600, height = 71, background = "#1F8EA8")
        self.cihBottomSpace.grid(row = 6, columnspan = 6)

        #Button Frame
        self.cihButtonFrame = LabelFrame(self.cihScreen, padx = 10, pady = 10, background = "#211F34")
        self.cihButtonFrame.grid(row = 4, column = 0, columnspan = 6)
        
                #Order By Label
        self.cihOrderLabel = Label(self.cihButtonFrame, text = "Order by", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cihOrderLabel.grid(row = 4, column = 0, padx = 5, pady = 10)
        
                #Booking ID
        self.cihBookingIDButton = Button(self.cihButtonFrame, text = "ID", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_BookingID)
        self.cihBookingIDButton.grid(row = 4, column = 1, padx = 10, pady = 10)
        
                #Booking Type
        self.cihBookingTypeButton = Button(self.cihButtonFrame, text = "Type", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_BookingType)
        self.cihBookingTypeButton.grid(row = 4, column = 2, padx = 10, pady = 10)

                #Booking Time
        self.cihBookingTimeButton = Button(self.cihButtonFrame, text = "Time", padx = 20, font = ("Tahoma", 21), command = self.OrderBy_BookingTime)
        self.cihBookingTimeButton.grid(row = 4, column = 3, padx = 10, pady = 10)

        #Invoice Search

        #Converting text file row into lists
        self.CustomerBookingFile = open("CustomerBooking.txt","r")
        self.CustomerBookingList = [row.split(',') for row in self.CustomerBookingFile]

        self.InvoiceHistory()

    def OrderBy_BookingID(self):
        self.cihScrollbarFrame.destroy()
        self.CustomerBookingFile = open("CustomerBooking.txt","r")
        self.CustomerBookingList = [row.split(',') for row in self.CustomerBookingFile]
        self.InvoiceHistory()
        
    def OrderBy_BookingType(self):
        self.cihScrollbarFrame.destroy()
        self.CustomerBookingList = sorted(self.CustomerBookingList, key=lambda x: x[1])
        self.InvoiceHistory()
        
    def OrderBy_BookingTime(self):
        self.cihScrollbarFrame.destroy()
        self.CustomerBookingList = sorted(self.CustomerBookingList, key=lambda x: x[3])
        self.InvoiceHistory()
        
    def InvoiceHistory(self):

        #Scrollbar Frame
        self.cihScrollbarFrame = LabelFrame(self.cihScreen, padx = 10, pady = 10, background = "#211F34")
        self.cihScrollbarFrame.grid(row = 5, column = 1, columnspan = 4)
        
        #Adding a Canvas for a Scrollbar
        self.cihCanvas = Canvas(self.cihScrollbarFrame)
        self.cihCanvas.pack(side = LEFT)

        #Adding a Scrollbar to the Canvas
        self.cihScrollbar = ttk.Scrollbar(self.cihScrollbarFrame, orient = VERTICAL, command = self.cihCanvas.yview)
        self.cihScrollbar.pack(side = RIGHT, fill = Y)
        
        #Configuring the Canvas
        self.cihCanvas.configure(yscrollcommand = self.cihScrollbar.set)
        self.cihCanvas.bind("<Configure>", lambda e: self.cihCanvas.configure(scrollregion = self.cihCanvas.bbox("all")))

        #Invoice Button Frame
        self.cihInvoiceFrame = LabelFrame(self.cihCanvas, padx = 10, pady = 10, background = "#211F34")
        self.cihInvoiceFrame.grid(row = 0, column = 0)

        self.cihCanvas.create_window((0, 0), window = self.cihInvoiceFrame)
    
##        count = -1
##        for row in self.CustomerBookingFile:
##            count += 1
##            self.CustomerBookingList.sort(key = lambda date: datetime.strptime(date, "%m/%d/%y"))
##
##        
##        
##                                      
##        n = len(self.CustomerBookingList)
##        for index in range(1, n):
##            current = self.CustomerBookingList[index][2]
##            index2 = index
##            while index2 > 0 and self.CustomerBookingList[index2 -1][2] > current:
##                self.CustomerBookingList[index2][2] = self.CustomerBookingList[index2 -1][2]
##                index2 = index2 -1
##            self.CustomerBookingList[index2][2] = current
        #Output the results
        
        #Searching for existing staff Username
        self.CustomerBookingFile = open("CustomerBooking.txt","r")

        self.cihRadioButtonVar = IntVar()
        self.cihRadioButtonVar.set(None)
    
        self.Count = -1
        for row in self.CustomerBookingFile:
           self.Count += 1

           if CustomerID == (self.CustomerBookingList[self.Count][4])[0:-1]:
               self.cihBookingIDButton = Radiobutton(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][0], variable = self.cihRadioButtonVar, value = self.Count + 1,
                                                     command = self.VCI, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
               self.cihBookingIDButton.grid(row = self.Count, column = 0, padx = 10, pady = 10)
               
               self.cihBookingIDType = Label(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][1],
                                             foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
               self.cihBookingIDType.grid(row = self.Count, column = 1, padx = 10, pady = 10)

               self.cihBookingIDDate = Label(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][2],
                                             foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
               self.cihBookingIDDate.grid(row = self.Count, column = 2, padx = 10, pady = 10)

               self.cihBookingIDTime = Label(self.cihInvoiceFrame, text = self.CustomerBookingList[self.Count][3],
                                             foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 12))
               self.cihBookingIDTime.grid(row = self.Count, column = 3, padx = 10, pady = 10)
           else:
               pass

#####Adding "Customer Invoice" Screen#####
    def VCI(self):

        global BookingID
        BookingID = "B#" + str(self.cihRadioButtonVar.get())

        global CustomerID
        CustomerID = (self.CustomerBookingList[self.cihRadioButtonVar.get() - 1][4])[0:-1]
        
        self.CustomerBookingFile.close()
        
        self.VCI = Toplevel(self.cihScreen)
        self.app = VCIWindow(self.VCI)


#####Customer Account Screen###################################################################################################################
class CustomerAccountWindow:

    #Creating Screen
    def __init__(self, caScreen):
        self.caScreen = caScreen     
        self.caScreen.resizable(False, False)
        self.caScreen.configure(background = "#1F8EA8")

        #Title

        #Tab
        self.caScreen.title("Customer Account")
        #Screen
        self.caTitle = Label(self.caScreen, text = "Customer Account", width = 20, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.caTitle.grid(row = 1, columnspan = 6)
        #Border
        self.caTopBorder = LabelFrame(self.caScreen, width = 546, height = 15, background = "#211F34")
        self.caTopBorder.grid(row = 0, columnspan = 6)
        self.caBottomBorder = LabelFrame(self.caScreen, width = 546, height = 15, background = "#211F34")
        self.caBottomBorder.grid(row = 2, columnspan = 6)

        #Screen Spacing
        self.caTopSpace = LabelFrame(self.caScreen, width = 546, height = 71, background = "#1F8EA8")
        self.caTopSpace.grid(row = 3, columnspan = 6)
        self.caBottomSpace = LabelFrame(self.caScreen, width = 546, height = 71, background = "#1F8EA8")
        self.caBottomSpace.grid(row = 5, columnspan = 6)

        #Menu Frame
        self.caFrame = LabelFrame(self.caScreen, padx = 10, pady = 10, background = "#211F34")
        self.caFrame.grid(row = 4, column = 1, columnspan = 4)

        #Buttons

            #Make a Booking
        self.caCustomersButton = Button(self.caFrame, text = "Make a Booking", width = 18, pady = 5,  font = ("Tahoma", 24), command = self.MAB)
        self.caCustomersButton.grid(row = 0, column = 0, padx = 10, pady = 10)
        
            #View Customer Invoice
        self.caStaffButton = Button(self.caFrame, text = "Customer Invoice History", width = 18, pady = 5, font = ("Tahoma", 24), command = self.CIHc)
        self.caStaffButton.grid(row = 1, column = 0, padx = 10, pady = 10)

#####Adding "Make a Booking" Screen#####
    def MAB(self):
        self.MAB = Toplevel(self.caScreen)
        self.app = MABWindow(self.MAB)

#####Adding "Customer Invoice History" Screen#####
    def CIHc(self):
        self.CIHc = Toplevel(self.caScreen)
        self.app = CIHcWindow(self.CIHc)

#####Make a Booking Screen####################################################################################################
class MABWindow:
    
    #Creating screen
    def __init__(self,mabScreen):
        self.mabScreen = mabScreen           
        self.mabScreen.resizable(False, False)
        self.mabScreen.configure(background = "#1F8EA8")

    #Title

        #Tab
        self.mabScreen.title("Make a Booking") 
        #Screen
        self.mabTitle = Label(self.mabScreen, text = "Make a Booking", width = 20, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.mabTitle.grid(row = 1, columnspan = 11)
        #Border
        self.mabTopBorder = LabelFrame(self.mabScreen, width = 546, height = 15, background = "#211F34")
        self.mabTopBorder.grid(row = 0, columnspan = 11)
        self.mabBottomBorder = LabelFrame(self.mabScreen, width = 546, height = 15, background = "#211F34")
        self.mabBottomBorder.grid(row = 2, columnspan = 11)

    #Screen Spacing
        self.mabTopSpace = LabelFrame(self.mabScreen, width = 546, height = 45, background = "#1F8EA8")
        self.mabTopSpace.grid(row = 3, columnspan = 11)
        self.mabBottomSpace = LabelFrame(self.mabScreen, width = 546, height = 45, background = "#1F8EA8")
        self.mabBottomSpace.grid(row = 5, columnspan = 11)

    #Customer Details Section

        #Frame
        self.mabCustomerDetailsFrame = LabelFrame(self.mabScreen, padx = 10, pady = 10, background = "#211F34")
        self.mabCustomerDetailsFrame.grid(row = 4, column = 1, columnspan = 9)

            #Title 
        self.mabCustomerDetailsTitle = Label(self.mabCustomerDetailsFrame, text = "Booking Details", width = 15, pady = 5, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.mabCustomerDetailsTitle.grid(row = 0, columnspan = 3)

            #Type Sub Title
        self.mabTypeTitle = Label(self.mabCustomerDetailsFrame, text = "Type", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.mabTypeTitle.grid(row = 1, column = 0, padx = 5, pady = 5)

                #Entry
        self.mabTypeEntry = Entry(self.mabCustomerDetailsFrame, width = 7, borderwidth = 3, font = ("Tahoma", 24))
        self.mabTypeEntry.grid(row = 2, column = 0, padx = 5, pady = 5)

            #Adding a variable for the radio buttons
        self.mabRadioButtonVar = StringVar()
        self.mabRadioButtonVar.set(None)
        
                #Dine-in
        
                    #Radio Button
        self.mabDine_inRadioButton = Radiobutton(self.mabCustomerDetailsFrame, text = "Dine-in", variable = self.mabRadioButtonVar, value = "Dine-in", command = self.MAB_GetType, width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.mabDine_inRadioButton.grid(row = 1, column = 1, padx = 5, pady = 5)

                #Takeout

                    #Radio Button
        self.mabTakeoutRadioButton = Radiobutton(self.mabCustomerDetailsFrame, text = "Takeout", variable = self.mabRadioButtonVar, value = "Takeout", command = self.MAB_GetType, width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.mabTakeoutRadioButton.grid(row = 2, column = 1, padx = 5, pady = 5)

                #Delivery

                    #Radio Button
        self.mabDeliveryRadioButton = Radiobutton(self.mabCustomerDetailsFrame, text = "Delivery", variable = self.mabRadioButtonVar, value = "Delivery", command = self.MAB_GetType, width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.mabDeliveryRadioButton.grid(row = 3, column = 1, padx = 5, pady = 5)

            #Date

        self.calendar = Calendar(self.mabCustomerDetailsFrame, selectmode = "day", year = 2022, month = 2, day = 9, foreground = "#211F34", background = "#1F8EA8", normalforeground = "#1F8EA8")
        self.calendar.grid(row = 4, rowspan = 3, column = 1, padx = 5, pady = 5)
        
                #Label
        self.mabDateLabel = Label(self.mabCustomerDetailsFrame, text = "Date", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.mabDateLabel.grid(row = 4, column = 0, padx = 5, pady = 5)

                #Entry
        self.mabDateEntry = Entry(self.mabCustomerDetailsFrame, width = 7, borderwidth = 3, font = ("Tahoma", 24))
        self.mabDateEntry.grid(row = 5, column = 0, padx = 5, pady = 5)

                #Button
        self.mabDateButton = Button(self.mabCustomerDetailsFrame, text = "Get Date", font = ("Tahoma", 24), command = self.MAB_GetDate)
        self.mabDateButton.grid(row = 6, column = 0, padx = 5, pady = 5)

        self.my_label = Label(self.mabCustomerDetailsFrame, text = "")
        self.my_label.grid(row = 6, column = 1, padx = 5, pady = 5)

            #Time
        
                #Label
        self.mabTimeLabel = Label(self.mabCustomerDetailsFrame, text = "Time", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.mabTimeLabel.grid(row = 7, column = 0, padx = 5, pady = 5)

                #Entry
        self.mabTimeEntry = Entry(self.mabCustomerDetailsFrame, width = 5, borderwidth = 3, font = ("Tahoma", 24))
        self.mabTimeEntry.grid(row = 7, column = 1, padx = 5, pady = 5)

        #Submit Button 
        self.mabSubmitButton = Button(self.mabCustomerDetailsFrame, text = "Submit", padx = 120, font = ("Tahoma", 21), command = self.MAB_AddRecord)
        self.mabSubmitButton.grid(row = 8, columnspan = 2, padx = 5, pady = 5)
    
    def MAB_GetType(self):
        self.mabTypeEntry.delete(0, "end")
        self.mabTypeEntry.insert(END, self.mabRadioButtonVar.get())
        
    def MAB_GetDate(self):
        self.mabDateEntry.delete(0, "end")
        self.mabDateEntry.insert(END, self.calendar.get_date())
    
    def MAB_AddRecord(self):
        #Passing the input from the entry boxes through to the MAB_AddRecord function
        self.BookingType = self.mabTypeEntry.get()
        self.BookingDate = self.mabDateEntry.get()
        self.BookingTime = self.mabTimeEntry.get()
        
        #Presence Check for Booking Type, Date, and Time
        if len(self.BookingType) == 0 or len(self.BookingDate) == 0 or len(self.BookingTime) == 0:
            messagebox.showinfo("Could not add new record", "Fill in all Booking Details")

        else:
            #Radio button selection
            if self.BookingType != "Dine-in" and self.BookingType != "Takeout" and self.BookingType != "Delivery":
                 messagebox.showinfo("Could not add new record", "Enter a valid Booking Type")
                
            else:
                #Reads all the records in the customer details file for primary key incrementation
                self.CustomerBookingFile = open("CustomerBooking.txt","r")

                self.mabCountRow = 0

                for row in self.CustomerBookingFile:
                    self.mabCountRow += 1

                self.CustomerBookingFile.close()

                #Converting text file row into lists
                self.CustomerAccountFile = open("CustomerAccount.txt","r")
                self.CustomerAccountList = [row.split(',') for row in self.CustomerAccountFile]

                #Searching for existing staff Username
                self.CustomerAccountFile = open("CustomerAccount.txt","r")
                self.Count = -1
                for row in self.CustomerAccountFile:
                    self.Count += 1

                    #Checking customer Username through every row 
                    if loginUsername == self.CustomerAccountList[self.Count][1]:

                        #Globalising CustomerID to be used for the "Add Customer Invoice" Screen
                        global CustomerID
                        CustomerID = self.CustomerAccountList[self.Count][0]

                        #Adds a record in the customer booking file
                        self.CustomerBookingFile = open("CustomerBooking.txt","a")

                        self.CustomerBookingFile.write("B#" + str(self.mabCountRow + 1) + "," + self.BookingType + "," + self.BookingDate + "," + self.BookingTime + "," + CustomerID + "\n")

                        self.CustomerBookingFile.close()
                        
                        self.Cart()

                    else:
                        pass

                self.CustomerAccountFile.close()

#####Adding "Cart" Screen#####
    def Cart(self):
        self.Cart = Toplevel(self.mabScreen)
        self.app = CartWindow(self.Cart)

#####Cart Screen####################################################################################################
class CartWindow:

    #Creating screen
    def __init__(self, cartScreen):
        self.cartScreen = cartScreen           
        self.cartScreen.resizable(False, False)
        self.cartScreen.configure(background = "#1F8EA8")
    
    #Title

        #Tab
        self.cartScreen.title("Cart") 
        #Screen
        self.cartTitle = Label(self.cartScreen, text = "Cart", width = 30, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.cartTitle.grid(row = 1, columnspan = 19)
        #Border
        self.cartTopBorder = LabelFrame(self.cartScreen, width = 816, height = 15, background = "#211F34")
        self.cartTopBorder.grid(row = 0, columnspan = 19)
        self.cartBottomBorder = LabelFrame(self.cartScreen, width = 816, height = 15, background = "#211F34")
        self.cartBottomBorder.grid(row = 2, columnspan = 19)

    #Screen Spacing
        self.cartTopSpace = LabelFrame(self.cartScreen, width = 816, height = 45, background = "#1F8EA8")
        self.cartTopSpace.grid(row = 3, columnspan = 19)
        self.cartBottomSpace = LabelFrame(self.cartScreen, width = 816, height = 45, background = "#1F8EA8")
        self.cartBottomSpace.grid(row = 5, columnspan = 19)
            
    #Left Section

        #Frame
        self.cartLeftFrame = LabelFrame(self.cartScreen, padx = 10, pady = 10, background = "#211F34")
        self.cartLeftFrame.grid(row = 4, column = 1, columnspan = 10)

            #Column Headings
        
                #Item
        self.cartItemColumn = Label(self.cartLeftFrame, text = "Item", width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cartItemColumn.grid(row = 0, column = 0, padx = 5, pady = 10)

                #Cost
        self.cartItemCostColumn = Label(self.cartLeftFrame, text = "Cost\n(£)", width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cartItemCostColumn.grid(row = 0, column = 1, padx = 5, pady = 10)

                #Quantity 
        self.cartItemQuantityColumn = Label(self.cartLeftFrame, text = "Quantity", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cartItemQuantityColumn.grid(row = 0, column = 2, columnspan = 3, padx = 5, pady = 10)
        
                #Line Cost 
        self.cartLineCostColumn = Label(self.cartLeftFrame, text = "Line Cost\n(£)", width = 6, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cartLineCostColumn.grid(row = 0, column = 5, padx = 5, pady = 10)

    #Right Section

        #Frame
        self.cartRightFrame = LabelFrame(self.cartScreen, padx = 10, pady = 10, background = "#211F34")
        self.cartRightFrame.grid(row = 4, column = 12, columnspan = 6)

        #Total Cost

            #Label
        self.cartTotalCostColumn = Label(self.cartRightFrame, text = "Total Cost\n(£)", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cartTotalCostColumn.grid(row = 0, column = 0, padx = 5, pady = 10)

            #Currency
        self.cartItemColumn = Label(self.cartRightFrame, text = "", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cartItemColumn.grid(row = 0, column = 1, padx = 5, pady = 10)
        
        #Update Button 
        self.cartUpdateButton = Button(self.cartRightFrame, text = "Update", padx = 2, font = ("Tahoma", 21), command = self.Cart_Update)
        self.cartUpdateButton.grid(row = 1, column = 0, padx = 10, pady = 10)

        #Menu Button 
        self.cartSubmitButton = Button(self.cartRightFrame, text = "Menu", padx = 2, font = ("Tahoma", 21), command = self.Menu)
        self.cartSubmitButton.grid(row = 1, column = 1, padx = 10, pady = 10)

        #Submit Button 
        self.cartSubmitButton = Button(self.cartRightFrame, text = "Submit", padx = 50, font = ("Tahoma", 21), command = self.Confirm)
        self.cartSubmitButton.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)

    #Declaring "invoice ready" variables for each item so the program knows when it can create the invoice
        self.InvoiceReadyItemA = "no"
        self.InvoiceReadyItemB = "no"
        self.InvoiceReadyItemC = "no"
        self.InvoiceReadyItemD = "no"
        
    #Setting the Quantity variable to 1 as default
        self.cartItemAQuantity = 1
        self.cartItemBQuantity = 1
        self.cartItemCQuantity = 1
        self.cartItemDQuantity = 1

    def Cart_Update(self):

        #Appetiser (A)

        try:
            #Item A Row

                #Item
            self.cartItemALabel = Label(self.cartLeftFrame, text = cartItemA, width = 15, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemALabel.grid(row = 1, column = 0, padx = 5, pady = 10)

                #Cost
            self.cartItemACostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(cartItemACost), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemACostLabel.grid(row = 1, column = 1, padx = 5, pady = 10)

                #Quantity
            self.cartItemAQuantityLabel = Label(self.cartLeftFrame, text = self.cartItemAQuantity, width = 2, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemAQuantityLabel.grid(row = 1, column = 3, padx = 5, pady = 10)

                    # -1 Button
            self.cartItemAQuantityButton1 = Button(self.cartLeftFrame, text = "-", pady = 6, font = ("Tahoma", 14), command = self.DecreaseQuantityA)
            self.cartItemAQuantityButton1.grid(row = 1, column = 2, padx = 5, pady = 10)

                    #+1 Button
            self.cartItemAQuantityButton2 = Button(self.cartLeftFrame, text = "+", pady = 6, font = ("Tahoma", 14), command = self.IncreaseQuantityA)
            self.cartItemAQuantityButton2.grid(row = 1, column = 4, padx = 5, pady = 10)
            
                #Line Cost

                    #Calculation
            self.cartItemALineCost = cartItemACost * self.cartItemAQuantity

                    #Display
            self.cartItemALineCostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(cartItemACost * self.cartItemAQuantity), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemALineCostLabel.grid(row = 1, column = 5, padx = 5, pady = 10)

            self.cartItemAMessage = ""

            self.InvoiceReadyItemA = "yes"
            
        except:
            self.cartItemAMessage = " Appetiser,"
            self.cartItemALineCost = 0

        #Main (B)

        try:
            #Item B Row

                #Item
            self.cartItemBLabel = Label(self.cartLeftFrame, text = cartItemB, width = 15, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemBLabel.grid(row = 2, column = 0, padx = 5, pady = 10)

                #Cost
            self.cartItemBCostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(cartItemBCost), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemBCostLabel.grid(row = 2, column = 1, padx = 5, pady = 10)

                #Quantity
            self.cartItemBQuantityLabel = Label(self.cartLeftFrame, text = self.cartItemBQuantity, width = 2, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemBQuantityLabel.grid(row = 2, column = 3, padx = 5, pady = 10)

                    # -1 Button
            self.cartItemBQuantityButton1 = Button(self.cartLeftFrame, text = "-", pady = 6, font = ("Tahoma", 14), command = self.DecreaseQuantityB)
            self.cartItemBQuantityButton1.grid(row = 2, column = 2, padx = 5, pady = 10)

                    #+1 Button
            self.cartItemBQuantityButton2 = Button(self.cartLeftFrame, text = "+", pady = 6, font = ("Tahoma", 14), command = self.IncreaseQuantityB)
            self.cartItemBQuantityButton2.grid(row = 2, column = 4, padx = 5, pady = 10)

                #Line Cost

                    #Calculation
            self.cartItemBLineCost = cartItemBCost * self.cartItemBQuantity

                    #Display
            self.cartItemBLineCostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(self.cartItemBLineCost), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemBLineCostLabel.grid(row = 2, column = 5, padx = 5, pady = 10)
            
            self.cartItemBMessage = ""

            self.InvoiceReadyItemB = "yes"
            
        except:
            self.cartItemBMessage = " Main,"
            self.cartItemBLineCost = 0

        #Dessert (C)
            
        try:
            #Item C Row

                #Item
            self.cartItemCLabel = Label(self.cartLeftFrame, text = cartItemC, width = 15, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemCLabel.grid(row = 3, column = 0, padx = 5, pady = 10)

                #Cost
            self.cartItemCCostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(cartItemCCost), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemCCostLabel.grid(row = 3, column = 1, padx = 5, pady = 10)

                #Quantity
            self.cartItemCQuantityLabel = Label(self.cartLeftFrame, text = self.cartItemCQuantity, width = 2, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemCQuantityLabel.grid(row = 3, column = 3, padx = 5, pady = 10)

                    # -1 Button
            self.cartItemCQuantityButton1 = Button(self.cartLeftFrame, text = "-", pady = 6, font = ("Tahoma", 14), command = self.DecreaseQuantityC)
            self.cartItemCQuantityButton1.grid(row = 3, column = 2, padx = 5, pady = 10)

                    #+1 Button
            self.cartItemCQuantityButton2 = Button(self.cartLeftFrame, text = "+", pady = 6, font = ("Tahoma", 14), command = self.IncreaseQuantityC)
            self.cartItemCQuantityButton2.grid(row = 3, column = 4, padx = 5, pady = 10)

                #Line Cost

                    #Calculation
            self.cartItemCLineCost = cartItemCCost * self.cartItemCQuantity

                    #Display
            self.cartItemCLineCostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(self.cartItemCLineCost), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemCLineCostLabel.grid(row = 3, column = 5, padx = 5, pady = 10)
            
            self.cartItemCMessage = ""

            self.InvoiceReadyItemC = "yes"
            
        except:
            self.cartItemCMessage = " Dessert,"
            self.cartItemCLineCost = 0

        #Drink (D)

        try:
            #Item D Row

                #Item
            self.cartItemDLabel = Label(self.cartLeftFrame, text = cartItemD, width = 15, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemDLabel.grid(row = 4, column = 0, padx = 5, pady = 10)

                #Cost
            self.cartItemDCostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(cartItemDCost), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemDCostLabel.grid(row = 4, column = 1, padx = 5, pady = 10)

                #Quantity
            self.cartItemDQuantityLabel = Label(self.cartLeftFrame, text = self.cartItemDQuantity, width = 2, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemDQuantityLabel.grid(row = 4, column = 3, padx = 5, pady = 10)

                    # -1 Button
            self.cartItemDQuantityButton1 = Button(self.cartLeftFrame, text = "-", pady = 6, font = ("Tahoma", 14), command = self.DecreaseQuantityD)
            self.cartItemDQuantityButton1.grid(row = 4, column = 2, padx = 5, pady = 10)

                    #+1 Button
            self.cartItemDQuantityButton2 = Button(self.cartLeftFrame, text = "+", pady = 6, font = ("Tahoma", 14), command = self.IncreaseQuantityD)
            self.cartItemDQuantityButton2.grid(row = 4, column = 4, padx = 5, pady = 10)

                #Line Cost

                    #Calculation
            self.cartItemDLineCost = cartItemDCost * self.cartItemDQuantity

                    #Display
            self.cartItemDLineCostLabel = Label(self.cartLeftFrame, text = "{:.2f}".format(self.cartItemDLineCost), width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
            self.cartItemDLineCostLabel.grid(row = 4, column = 5, padx = 5, pady = 10)
            
            self.cartItemDMessage = ""

            self.InvoiceReadyItemD = "yes"
            
        except:
            self.cartItemDMessage = " and Drink"
            
            if self.cartItemAMessage == "" and self.cartItemBMessage == "" and self.cartItemCMessage == "":
                self.cartItemDMessage = " Drink"
            self.cartItemDLineCost = 0

        #Messagebox if items of each food type are not selected
        try:
            self.cartMessage = self.cartItemAMessage + self.cartItemBMessage + self.cartItemCMessage + self.cartItemDMessage
            if self.cartMessage != "":
                messagebox.showinfo("Add all types to the cart", "Add" + self.cartMessage + " via the menu")
            
        except:
            print("failed")

        self.cartItemTotalCost = self.cartItemALineCost + self.cartItemBLineCost + self.cartItemCLineCost + self.cartItemDLineCost
        self.cartItemColumn = Label(self.cartRightFrame, text = "{:.2f}".format(self.cartItemTotalCost), width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.cartItemColumn.grid(row = 0, column = 1, padx = 5, pady = 10)
            
#####Quantity A#####
    #Decrease 
    def DecreaseQuantityA(self):
        self.cartItemAQuantity -= 1
        self.Cart_Update()
        
    #Increase 
    def IncreaseQuantityA(self):
        self.cartItemAQuantity += 1
        self.Cart_Update()

#####Quantity B#####
    #Decrease 
    def DecreaseQuantityB(self):
        self.cartItemBQuantity -= 1
        self.Cart_Update()

    #Increase
    def IncreaseQuantityB(self):
        self.cartItemBQuantity += 1
        self.Cart_Update()
            
#####Quantity C#####
    #Decrease 
    def DecreaseQuantityC(self):
        self.cartItemCQuantity -= 1
        self.Cart_Update()

    #Increase
    def IncreaseQuantityC(self):
        self.cartItemCQuantity += 1
        self.Cart_Update()

#####Quantity D#####
    #Decrease 
    def DecreaseQuantityD(self):
        self.cartItemDQuantity -= 1
        self.Cart_Update()

    #Increase
    def IncreaseQuantityD(self):
        self.cartItemDQuantity += 1
        self.Cart_Update()
            
#####Adding "Confirm" Screen#####
    def Confirm(self):

        #Invoice ready check
        if self.InvoiceReadyItemA == "yes" and self.InvoiceReadyItemB == "yes" and self.InvoiceReadyItemC == "yes" and self.InvoiceReadyItemD == "yes":
        
            #Reads all the records in the customer order file for primary key incrementation
            self.CustomerOrderFile = open("CustomerOrder.txt","r")

            self.cartCustomerOrderCountRow = 0

            for row in self.CustomerOrderFile:
                self.cartCustomerOrderCountRow += 1

            self.CustomerOrderFile.close()
            
            #Reads all the records in the staff details file for primary key incrementation
            self.StaffDetailsFile = open("StaffDetails.txt","r")

            self.cartStaffDetailsCountRow = 0

            for row in self.StaffDetailsFile:
                self.cartStaffDetailsCountRow += 1

            self.StaffDetailsFile.close()

            #Adds a record in the customer details file
            self.CustomerOrderFile = open("CustomerOrder.txt","a")

            self.CustomerOrderFile.write("B#" + str(self.cartCustomerOrderCountRow + 1) + ","

                                         #Item A
                                         #[,1], [,2], [,3], [,4],
                                         + str(cartItemA) + "," + str("{:.2f}".format(cartItemACost)) + ","
                                         + str(self.cartItemAQuantity) + "," + str("{:.2f}".format(self.cartItemALineCost)) + ","
                                         
                                         #Item B
                                         #[,5], [,6], [,7], [,8],
                                         + str(cartItemB) + "," + str("{:.2f}".format(cartItemBCost)) + ","
                                         + str(self.cartItemBQuantity) + "," + str("{:.2f}".format(self.cartItemBLineCost)) + ","
                                         
                                         #Item C
                                         #[,9], [,10], [,11], [,12],
                                         + str(cartItemC) + "," + str("{:.2f}".format(cartItemCCost)) + ","
                                         + str(self.cartItemCQuantity) + "," + str("{:.2f}".format(self.cartItemCLineCost)) + ","
                                         
                                         #Item D
                                         #[,13], [,14], [,15], [,16],
                                         + str(cartItemD) + "," + str("{:.2f}".format(cartItemDCost)) + ","
                                         + str(self.cartItemDQuantity) + "," + str("{:.2f}".format(self.cartItemDLineCost)) + ","

                                         #Item (A + B + C + D)
                                         #[,17],
                                         + str("{:.2f}".format(self.cartItemTotalCost)) + ","
                                         
                                         + "S#" + str(random.randint(1, self.cartStaffDetailsCountRow)) + "\n")

            self.CustomerOrderFile.close()

            messagebox.showinfo("Invoice made", "Invoice made\nYou can check your invoice on the customer screen")

            #Globalising and assigning yes to the "invoiceReady" variable so that the
            #"View Customer Invoice" button in the "Customer Account" screen can be used
            global invoiceReady
            invoiceReady = "yes"

            self.cartScreen.destroy()

        else:
            messagebox.showinfo("Could not make an invoice", "Could not make an invoice\nSelect one of each food type to proceed")
            
#####Adding "Menu" Screen#####
    def Menu(self):
        self.Menu = Toplevel(self.cartScreen)
        self.app = MenuWindow(self.Menu)

#####View Staff Account Details Screen####################################################################################################
class VSADWindow:
        
    #Creating screen
    def __init__(self, vsadScreen):
        self.vsadScreen = vsadScreen           
        self.vsadScreen.resizable(False, False)
        self.vsadScreen.configure(background = "#4EB027")

    #Title

        #Tab
        self.vsadScreen.title("Staff " + StaffID + " Job Role " + JobID) 
        #Screen
        self.vsadTitle = Label(self.vsadScreen, text = "Staff " + StaffID + " Job Role " + JobID, width = 25, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.vsadTitle.grid(row = 1, columnspan = 20)
        #Border
        self.vsadTopBorder = LabelFrame(self.vsadScreen, width = 681, height = 15, background = "#211F34")
        self.vsadTopBorder.grid(row = 0, columnspan = 20)
        self.vsadBottomBorder = LabelFrame(self.vsadScreen, width = 681, height = 15, background = "#211F34")
        self.vsadBottomBorder.grid(row = 2, columnspan = 20)

    #Screen Spacing
        self.vsadTopSpace = LabelFrame(self.vsadScreen, width = 681, height = 45, background = "#4EB027")
        self.vsadTopSpace.grid(row = 3, columnspan = 20)
        self.vsadBottomSpace = LabelFrame(self.vsadScreen, width = 681, height = 45, background = "#4EB027")
        self.vsadBottomSpace.grid(row = 7, columnspan = 20)
        
    ###Staff Details###
        
        #Converting text file row into lists
        self.StaffDetailsFile = open("StaffDetails.txt","r")
        self.StaffDetailsList = [row.split(',') for row in self.StaffDetailsFile]

        #Searching for existing record using CustomerID
        self.StaffDetailsFile = open("StaffDetails.txt","r")
        self.Count = -1
        for row in self.StaffDetailsFile:
            self.Count += 1

            #Checking customer Username through every row 
            if StaffID == self.StaffDetailsList[self.Count][0]:

                #Creating variables for the each of the elements in the record
                self.sForename = self.StaffDetailsList[self.Count][1]
                self.sSurname = self.StaffDetailsList[self.Count][2]
                self.sName = (self.sForename, self.sSurname)
                self.sPhone_Number = self.StaffDetailsList[self.Count][3]
                self.sEmail = self.StaffDetailsList[self.Count][4]
                self.sAddress = self.StaffDetailsList[self.Count][5]
                self.sPostcode = self.StaffDetailsList[self.Count][6]

                #Job Type
                self.jType = (self.StaffDetailsList[self.Count][8])[0:-1]

            else:
                pass

        self.StaffDetailsFile.close()

    ###Job Roles###
        
        #Converting text file row into lists
        self.JobRolesFile = open("JobRoles.txt","r")
        self.JobRolesList = [row.split(',') for row in self.JobRolesFile]

        #Searching for existing record using CustomerID
        self.JobRolesFile = open("JobRoles.txt","r")
        self.Count = -1
        for row in self.JobRolesFile:
            self.Count += 1

            #Checking customer Username through every row 
            if JobID == self.JobRolesList[self.Count][0]:

                #Creating variables for the each of the elements in the record
                self.jRole = self.JobRolesList[self.Count][1]
                self.jDescription = self.JobRolesList[self.Count][2]

            else:
                pass

        self.JobRolesFile.close()
                
        #Heading (x,y)

        #####Staff Details (1,0)#####

        #Frame
        self.vsadSFrame = LabelFrame(self.vsadScreen, padx = 10, pady = 10, background = "#211F34")
        self.vsadSFrame.grid(row = 4, column = 0, columnspan = 8)

            #Heading
        self.vsadSHeading = Label(self.vsadSFrame, text = "Staff", width = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.vsadSHeading.grid(row = 0, column = 0, columnspan = 2)

                #Name

                    #Label
        self.vsadSForenameLabel = Label(self.vsadSFrame, text = "Name", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSForenameLabel.grid(row = 1, column = 0)

                    #Display
        self.vsadSForenameDisplay = Label(self.vsadSFrame, text = self.sName, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSForenameDisplay.grid(row = 1, column = 1)

                #Phone Number

                    #Label
        self.vsadSPhoneNumberLabel = Label(self.vsadSFrame, text = "Phone\nNumber", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSPhoneNumberLabel.grid(row = 2, column = 0)

                    #Display
        self.vsadSPhoneNumberDisplay = Label(self.vsadSFrame, text = self.sPhone_Number, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSPhoneNumberDisplay.grid(row = 2, column = 1)

                #Email

                    #Label
        self.vsadSEmailLabel = Label(self.vsadSFrame, text = "Email", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSEmailLabel.grid(row = 3, column = 0)

                    #Display
        self.vsadSEmailDisplay = Label(self.vsadSFrame, text = self.sEmail, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSEmailDisplay.grid(row = 3, column = 1)

                #Address
        
                    #Label
        self.vsadSAddressLabel = Label(self.vsadSFrame, text = "Address", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSAddressLabel.grid(row = 4, column = 0)

                    #Display
        self.vsadSAddressDisplay = Label(self.vsadSFrame, text = self.sAddress, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSAddressDisplay.grid(row = 4, column = 1)
        
                #Postcode

                    #Label
        self.vsadSPostcodeLabel = Label(self.vsadSFrame, text = "Postcode", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSPostcodeLabel.grid(row = 5, column = 0)

                    #Display
        self.vsadSPostcodeDisplay = Label(self.vsadSFrame, text = self.sPostcode, width = 28, pady = 5, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadSPostcodeDisplay.grid(row = 5, column = 1)

        #####Job Role (1,0)#####

        #Frame
        self.vsadJFrame = LabelFrame(self.vsadScreen, padx = 10, pady = 10, background = "#211F34")
        self.vsadJFrame.grid(row = 4, column = 8, columnspan = 12)
        
                #Heading
        self.vsadJHeading = Label(self.vsadJFrame, text = "Job Role", width = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.vsadJHeading.grid(row = 0, column = 0, columnspan = 2)

##                #Blank Spaces
##        self.vsadJSpaceLabel = Label(self.vsadJFrame, text = "", width = 8, pady = 5, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
##        self.vsadJSpaceLabel.grid(row = 1, column = 0)
##
##        self.vsadJSpaceLabel = Label(self.vsadJFrame, text = "", width = 8, pady = 5, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
##        self.vsadJSpaceLabel.grid(row = 5, column = 0)
        
                #Type

                    #Label
        self.vsadJTypeLabel = Label(self.vsadJFrame, text = "Type", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadJTypeLabel.grid(row = 1, column = 0)

                    #Display
        self.vsadJTypeDisplay = Label(self.vsadJFrame, text = self.jType, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadJTypeDisplay.grid(row = 1, column = 1)
        
                #Role

                    #Label
        self.vsadJRoleLabel = Label(self.vsadJFrame, text = "Role", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadJRoleLabel.grid(row = 2, column = 0)

                    #Display
        self.vsadJRoleDisplay = Label(self.vsadJFrame, text = self.jRole, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadJRoleDisplay.grid(row = 2, column = 1)

                #Description

                    #Label
        self.vsadJDescriptionLabel = Label(self.vsadJFrame, text = "Description", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vsadJDescriptionLabel.grid(row = 3, column = 0)

                    #Display
        self.vsadJDescriptionDisplay = Label(self.vsadJFrame, text = self.jDescription, width = 50, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 11))
        self.vsadJDescriptionDisplay.grid(row = 4, column = 0, columnspan = 2)

        #Close Button 
        self.vsadCloseButton = Button(self.vsadJFrame, text = "Close", padx = 10, font = ("Tahoma", 21), command = self.Close)
        self.vsadCloseButton.grid(row = 5, column = 0, columnspan = 2)

    def Close(self):
        self.vsadScreen.destroy()

#####View Customer Invoice Screen####################################################################################################
class VCIWindow:
        
    #Creating screen
    def __init__(self, vciScreen):
        self.vciScreen = vciScreen           
        self.vciScreen.resizable(False, False)
        self.vciScreen.configure(background = "#4EB027")

    #Title

        #Tab
        self.vciScreen.title("Invoice " + BookingID + " Customer " + CustomerID) 
        #Screen
        self.vciTitle = Label(self.vciScreen, text = "Invoice " + BookingID + " Customer " + CustomerID, width = 30, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.vciTitle.grid(row = 1, columnspan = 20)
        #Border
        self.vciTopBorder = LabelFrame(self.vciScreen, width = 816, height = 15, background = "#211F34")
        self.vciTopBorder.grid(row = 0, columnspan = 20)
        self.vciBottomBorder = LabelFrame(self.vciScreen, width = 816, height = 15, background = "#211F34")
        self.vciBottomBorder.grid(row = 2, columnspan = 20)

    #Screen Spacing
        self.vciTopSpace = LabelFrame(self.vciScreen, width = 816, height = 45, background = "#4EB027")
        self.vciTopSpace.grid(row = 3, columnspan = 20)
        self.vciBottomSpace = LabelFrame(self.vciScreen, width = 816, height = 45, background = "#4EB027")
        self.vciBottomSpace.grid(row = 7, columnspan = 20)

    ###Booking Details###
        
        #Converting text file row into lists
        self.CustomerBookingFile = open("CustomerBooking.txt","r")
        self.CustomerBookingList = [row.split(',') for row in self.CustomerBookingFile]

        #Searching for the most recent existing record using the BookingID
        self.CustomerBookingFile = open("CustomerBooking.txt","r")
        self.Count = -1
        for row in self.CustomerBookingFile:
            self.Count += 1

            #Checking BookingID in the last line of the file
            if BookingID == self.CustomerBookingList[self.Count][0]:

                #Creating variables for the each of the elements in the record
                self.bType = self.CustomerBookingList[self.Count][1]
                self.bDate = self.CustomerBookingList[self.Count][2]
                self.bTime = self.CustomerBookingList[self.Count][3]

        else:
            pass

        self.CustomerBookingFile.close()
        
    ###Customer Details###
        
        #Converting text file row into lists
        self.CustomerDetailsFile = open("CustomerDetails.txt","r")
        self.CustomerDetailsList = [row.split(',') for row in self.CustomerDetailsFile]

        #Searching for existing record using CustomerID
        self.CustomerDetailsFile = open("CustomerDetails.txt","r")
        self.Count = -1
        for row in self.CustomerDetailsFile:
            self.Count += 1

            #Checking customer Username through every row 
            if CustomerID == self.CustomerDetailsList[self.Count][0]:

                #Creating variables for the each of the elements in the record
                self.cForename = self.CustomerDetailsList[self.Count][1]
                self.cSurname = self.CustomerDetailsList[self.Count][2]
                self.cName = (self.cForename, self.cSurname)
                self.cPhone_Number = self.CustomerDetailsList[self.Count][3]
                self.cEmail = self.CustomerDetailsList[self.Count][4]
                self.cAddress = self.CustomerDetailsList[self.Count][5]
                self.cPostcode = (self.CustomerDetailsList[self.Count][6])[0:-1]

            else:
                pass

        self.CustomerDetailsFile.close()

    ###Order Details###
        
        #Converting text file row into lists
        self.CustomerOrderFile = open("CustomerOrder.txt","r")
        self.CustomerOrderList = [row.split(',') for row in self.CustomerOrderFile]

        #Searching for the most recent existing record using the BookingID
        self.CustomerOrderFile = open("CustomerOrder.txt","r")
        self.Count = -1
        for row in self.CustomerOrderFile:
            self.Count += 1

            #Checking BookingID in the last line of the file
            if BookingID == self.CustomerOrderList[self.Count][0]:

                #Creating variables for the each of the elements in the record
                cartItemA = self.CustomerOrderList[self.Count][1]
                cartItemACost = self.CustomerOrderList[self.Count][2]
                self.oItemAQuantity = self.CustomerOrderList[self.Count][3]
                self.oItemALineCost = self.CustomerOrderList[self.Count][4]

                cartItemB = self.CustomerOrderList[self.Count][5]
                cartItemBCost = self.CustomerOrderList[self.Count][6]
                self.oItemBQuantity = self.CustomerOrderList[self.Count][7]
                self.oItemBLineCost = self.CustomerOrderList[self.Count][8]

                cartItemC = self.CustomerOrderList[self.Count][9]
                cartItemCCost = self.CustomerOrderList[self.Count][10]
                self.oItemCQuantity = self.CustomerOrderList[self.Count][11]
                self.oItemCLineCost = self.CustomerOrderList[self.Count][12]

                cartItemD = self.CustomerOrderList[self.Count][13]
                cartItemDCost = self.CustomerOrderList[self.Count][14]
                self.oItemDQuantity = self.CustomerOrderList[self.Count][15]
                self.oItemDLineCost = self.CustomerOrderList[self.Count][16]
                
                self.oTotalCost = self.CustomerOrderList[self.Count][17]

            else:
                pass

        self.CustomerBookingFile.close()

        #Heading (x,y)
        ######Restaurant Details (0,0)#####

        #Frame
        self.vciRFrame = LabelFrame(self.vciScreen, padx = 10, pady = 10, background = "#211F34")
        self.vciRFrame.grid(row = 4, column = 1, columnspan = 6)

            #Heading
        self.vciRHeading = Label(self.vciRFrame, text = "Restaurant", width = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.vciRHeading.grid(row = 0, column = 0, columnspan = 2)

                #Name

                    #Label
        self.vciRNameLabel = Label(self.vciRFrame, text = "Name", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRNameLabel.grid(row = 1, column = 0)

                    #Display
        self.vciRNameDisplay = Label(self.vciRFrame, text = "Ukiyo Teahouse", width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRNameDisplay.grid(row = 1, column = 1)

                #Phone Number

                    #Label
        self.vciRPhoneNumberLabel = Label(self.vciRFrame, text = "Phone\nNumber", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRPhoneNumberLabel.grid(row = 2, column = 0)

                    #Display
        self.vciRPhoneNumberDisplay = Label(self.vciRFrame, text = "02994960528", width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRPhoneNumberDisplay.grid(row = 2, column = 1)

                #Email

                    #Label
        self.vciREmailLabel = Label(self.vciRFrame, text = "Email", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciREmailLabel.grid(row = 3, column = 0)

                    #Display
        self.vciREmailDisplay = Label(self.vciRFrame, text = "UkiyoTeahouse@gmail.com", width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciREmailDisplay.grid(row = 3, column = 1)
        
                #Address
        
                    #Label
        self.vciRAddressLabel = Label(self.vciRFrame, text = "Address", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRAddressLabel.grid(row = 4, column = 0)

                    #Display
        self.vciRAddressDisplay = Label(self.vciRFrame, text = "29 Custom House St", width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRAddressDisplay.grid(row = 4, column = 1)

                #Postcode
        
                    #Label
        self.vciRPostcodeLabel = Label(self.vciRFrame, text = "Postcode", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRPostcodeLabel.grid(row = 5, column = 0)

                    #Display
        self.vciRPostcodeDisplay = Label(self.vciRFrame, text = "CF10 1AP", width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciRPostcodeDisplay.grid(row = 5, column = 1)



        #####Booking Details (1,0)#####

        #Frame
        self.vciBFrame = LabelFrame(self.vciScreen, padx = 10, pady = 10, background = "#211F34")
        self.vciBFrame.grid(row = 4, column = 7, columnspan = 6)
        
                #Heading
        self.vciBHeading = Label(self.vciBFrame, text = "Booking", width = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.vciBHeading.grid(row = 0, column = 0, columnspan = 2)

                #Blank Spaces
        self.vciBSpaceLabel = Label(self.vciBFrame, text = "", width = 8, pady = 5, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBSpaceLabel.grid(row = 1, column = 0)

        self.vciBSpaceLabel = Label(self.vciBFrame, text = "", width = 8, pady = 5, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBSpaceLabel.grid(row = 5, column = 0)
        
                #Type

                    #Label
        self.vciBTypeLabel = Label(self.vciBFrame, text = "Type", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBTypeLabel.grid(row = 2, column = 0)

                    #Display
        self.vciBTypeDisplay = Label(self.vciBFrame, text = self.bType, width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBTypeDisplay.grid(row = 2, column = 1)
        
                #Date

                    #Label
        self.vciBDateLabel = Label(self.vciBFrame, text = "Date", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBDateLabel.grid(row = 3, column = 0)

                    #Display
        self.vciBDateDisplay = Label(self.vciBFrame, text = self.bDate, width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBDateDisplay.grid(row = 3, column = 1)

                #Time

                    #Label
        self.vciBTimeLabel = Label(self.vciBFrame, text = "Time", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBTimeLabel.grid(row = 4, column = 0)

                    #Display
        self.vciBTimeDisplay = Label(self.vciBFrame, text = self.bTime, width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciBTimeDisplay.grid(row = 4, column = 1)



        #####Customer Details (1,0)#####

        #Frame
        self.vciCFrame = LabelFrame(self.vciScreen, padx = 10, pady = 10, background = "#211F34")
        self.vciCFrame.grid(row = 4, column = 13, columnspan = 6)

            #Heading
        self.vciCHeading = Label(self.vciCFrame, text = "Customer", width = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.vciCHeading.grid(row = 0, column = 0, columnspan = 2)

                #Name

                    #Label
        self.vciCForenameLabel = Label(self.vciCFrame, text = "Name", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCForenameLabel.grid(row = 1, column = 0)

                    #Display
        self.vciCForenameDisplay = Label(self.vciCFrame, text = self.cName, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCForenameDisplay.grid(row = 1, column = 1)

                #Phone Number

                    #Label
        self.vciCPhoneNumberLabel = Label(self.vciCFrame, text = "Phone\nNumber", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCPhoneNumberLabel.grid(row = 2, column = 0)

                    #Display
        self.vciCPhoneNumberDisplay = Label(self.vciCFrame, text = self.cPhone_Number, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCPhoneNumberDisplay.grid(row = 2, column = 1)

                #Email

                    #Label
        self.vciCEmailLabel = Label(self.vciCFrame, text = "Email", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCEmailLabel.grid(row = 3, column = 0)

                    #Display
        self.vciCEmailDisplay = Label(self.vciCFrame, text = self.cEmail, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCEmailDisplay.grid(row = 3, column = 1)

                #Address
        
                    #Label
        self.vciCAddressLabel = Label(self.vciCFrame, text = "Address", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCAddressLabel.grid(row = 4, column = 0)

                    #Display
        self.vciCAddressDisplay = Label(self.vciCFrame, text = self.cAddress, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCAddressDisplay.grid(row = 4, column = 1)
        
                #Postcode

                    #Label
        self.vciCPostcodeLabel = Label(self.vciCFrame, text = "Postcode", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCPostcodeLabel.grid(row = 5, column = 0)

                    #Display
        self.vciCPostcodeDisplay = Label(self.vciCFrame, text = self.cPostcode, width = 28, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciCPostcodeDisplay.grid(row = 5, column = 1)



        #####Order Details (1,0)#####

        #Frame
        self.vciOFrame = LabelFrame(self.vciScreen, padx = 10, pady = 10, background = "#211F34")
        self.vciOFrame.grid(row = 6, column = 1, columnspan = 18)

                #Heading
        self.vciOHeading = Label(self.vciOFrame, text = "Order", width = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.vciOHeading.grid(row = 0, column = 0, columnspan = 6)

                #Item Headings
        
                    #Type (0,0)
        self.vciOItemType = Label(self.vciOFrame, text = "Item\nType", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemType.grid(row = 1, column = 0)

                    #Name (1,0)
        self.vciOItemName = Label(self.vciOFrame, text = "Item\nName", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemName.grid(row = 1, column = 1)

                    #Cost (2,0)
        self.vciOItemCost = Label(self.vciOFrame, text = "Item\nCost (£)", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemCost.grid(row = 1, column = 2)

                    #Quantity (2,0)
        self.vciOItemQuantity = Label(self.vciOFrame, text = "Item\nQuantity", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemQuantity.grid(row = 1, column = 3)

                    #Line Cost (3,0)
        self.vciOItemLineCost = Label(self.vciOFrame, text = "Item Line\nCost (£)", width = 8, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemLineCost.grid(row = 1, column = 4)
        
                #Item A (0,1)

                    #Type
        self.vciOItemAType = Label(self.vciOFrame, text = "A", width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemAType.grid(row = 2, column = 0)

                    #Name
        self.vciOItemAName = Label(self.vciOFrame, text = cartItemA, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemAName.grid(row = 2, column = 1)

                    #Cost
        self.vciOItemACost = Label(self.vciOFrame, text = cartItemACost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemACost.grid(row = 2, column = 2)

                    #Quantity
        self.vciOItemAQuantity = Label(self.vciOFrame, text = self.oItemAQuantity, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemAQuantity.grid(row = 2, column = 3)

                    #Line Cost
        self.vciOItemALineCost = Label(self.vciOFrame, text = self.oItemALineCost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemALineCost.grid(row = 2, column = 4)

                #Item B (0,1)

                    #Type
        self.vciOItemBType = Label(self.vciOFrame, text = "B", width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemBType.grid(row = 3, column = 0)

                    #Name
        self.vciOItemBName = Label(self.vciOFrame, text = cartItemB, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemBName.grid(row = 3, column = 1)

                    #Cost
        self.vciOItemBCost = Label(self.vciOFrame, text = cartItemBCost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemBCost.grid(row = 3, column = 2)

                    #Quantity
        self.vciOItemBQuantity = Label(self.vciOFrame, text = self.oItemBQuantity, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemBQuantity.grid(row = 3, column = 3)

                    #Line Cost
        self.vciOItemBLineCost = Label(self.vciOFrame, text = self.oItemBLineCost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemBLineCost.grid(row = 3, column = 4)
        
                #Item C (0,1)

                    #Label
        self.vciOItemCType = Label(self.vciOFrame, text = "C", width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemCType.grid(row = 4, column = 0)

                    #Name
        self.vciOItemCName = Label(self.vciOFrame, text = cartItemC, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemCName.grid(row = 4, column = 1)

                    #Cost
        self.vciOItemCCost = Label(self.vciOFrame, text = cartItemCCost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemCCost.grid(row = 4, column = 2)

                    #Quantity
        self.vciOItemCQuantity = Label(self.vciOFrame, text = self.oItemCQuantity, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemCQuantity.grid(row = 4, column = 3)

                    #Line Cost
        self.vciOItemCLineCost = Label(self.vciOFrame, text = self.oItemCLineCost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemCLineCost.grid(row = 4, column = 4)
        
                #Item D (0,1)

                    #Type
        self.vciOItemDType = Label(self.vciOFrame, text = "D", width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemDType.grid(row = 5, column = 0)

                    #Name
        self.vciOItemDName = Label(self.vciOFrame, text = cartItemD, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemDName.grid(row = 5, column = 1)

                    #Cost
        self.vciOItemDCost = Label(self.vciOFrame, text = cartItemDCost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemDCost.grid(row = 5, column = 2)

                    #Quantity
        self.vciOItemDQuantity = Label(self.vciOFrame, text = self.oItemDQuantity, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemDQuantity.grid(row = 5, column = 3)

                    #Line Cost
        self.vciOItemDLineCost = Label(self.vciOFrame, text = self.oItemDLineCost, width = 16, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOItemDLineCost.grid(row = 5, column = 4)
        
                #Total Cost

                    #Label
        self.vciOTotalCostLabel = Label(self.vciOFrame, text = "Total\nCost (£)", width = 14, padx = 4, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOTotalCostLabel.grid(row = 1, column = 5)

                    #Display
        self.vciOTotalCostDisplay = Label(self.vciOFrame, text = self.oTotalCost, width = 14, padx = 4, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.vciOTotalCostDisplay.grid(row = 2, column = 5)

        #Close Button 
        self.vciCloseButton = Button(self.vciOFrame, text = "Close", padx = 10, font = ("Tahoma", 21), command = self.Close)
        self.vciCloseButton.grid(row = 3, rowspan = 3, column = 5)

    def Close(self):
        self.vciScreen.destroy()
        
#####Create Customer Account Screen####################################################################################################
class CCAWindow:
        
    #Creating screen
    def __init__(self,ccaScreen):
        self.ccaScreen = ccaScreen           
        self.ccaScreen.resizable(False, False)
        self.ccaScreen.configure(background = "#DC7CA1")

    #Title

        #Tab
        self.ccaScreen.title("Create Customer Account") 
        #Screen
        self.ccaTitle = Label(self.ccaScreen, text = "Create Customer Account", width = 30, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.ccaTitle.grid(row = 1, columnspan = 11)
        #Border
        self.ccaTopBorder = LabelFrame(self.ccaScreen, width = 816, height = 15, background = "#211F34")
        self.ccaTopBorder.grid(row = 0, columnspan = 11)
        self.ccaBottomBorder = LabelFrame(self.ccaScreen, width = 816, height = 15, background = "#211F34")
        self.ccaBottomBorder.grid(row = 2, columnspan = 11)

    #Screen Spacing
        self.ccaTopSpace = LabelFrame(self.ccaScreen, width = 816, height = 45, background = "#DC7CA1")
        self.ccaTopSpace.grid(row = 3, columnspan = 11)
        self.ccaBottomSpace = LabelFrame(self.ccaScreen, width = 816, height = 45, background = "#DC7CA1")
        self.ccaBottomSpace.grid(row = 5, columnspan = 11)

    #Customer Details Section

        #Frame
        self.ccaCustomerDetailsFrame = LabelFrame(self.ccaScreen, padx = 10, pady = 10, background = "#211F34")
        self.ccaCustomerDetailsFrame.grid(row = 4, column = 1, columnspan = 4)

            #Title 
        self.ccaCustomerDetailsTitle = Label(self.ccaCustomerDetailsFrame, text = "Customer Details", width = 15, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.ccaCustomerDetailsTitle.grid(row = 0, columnspan = 2)

            #Forname

                #Label
        self.ccaFornameLabel = Label(self.ccaCustomerDetailsFrame, text = "Forename", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaFornameLabel.grid(row = 1, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaFornameEntry = Entry(self.ccaCustomerDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaFornameEntry.grid(row = 1, column = 1, padx = 5, pady = 10)
        
            #Surname

                #Label
        self.ccaSurnameLabel = Label(self.ccaCustomerDetailsFrame, text = "Surname", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaSurnameLabel.grid(row = 2, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaSurnameEntry = Entry(self.ccaCustomerDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaSurnameEntry.grid(row = 2, column = 1, padx = 5, pady = 10)
        
            #Phone Number

                #Label
        self.ccaPhoneNoLabel = Label(self.ccaCustomerDetailsFrame, text = "Phone\nNumber", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaPhoneNoLabel.grid(row = 3, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaPhoneNoEntry = Entry(self.ccaCustomerDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaPhoneNoEntry.grid(row = 3, column = 1, padx = 5, pady = 10)
        
            #Email

                #Label
        self.ccaEmailLabel = Label(self.ccaCustomerDetailsFrame, text = "Email", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaEmailLabel.grid(row = 4, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaEmailEntry = Entry(self.ccaCustomerDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaEmailEntry.grid(row = 4, column = 1, padx = 5, pady = 10)
        
            #Address
        
                #Label
        self.ccaAddressLabel = Label(self.ccaCustomerDetailsFrame, text = "Address", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaAddressLabel.grid(row = 5, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaAddressEntry = Entry(self.ccaCustomerDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaAddressEntry.grid(row = 5, column = 1, padx = 5, pady = 10)
        
            #Postcode

                #Label
        self.ccaPostcodeLabel = Label(self.ccaCustomerDetailsFrame, text = "Postcode", width = 8, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaPostcodeLabel.grid(row = 6, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaPostcodeEntry = Entry(self.ccaCustomerDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaPostcodeEntry.grid(row = 6, column = 1, padx = 5, pady = 10)

    #Login Details Section

        #Frame
        self.ccaLoginDetailsFrame = LabelFrame(self.ccaScreen, padx = 10, pady = 10, background = "#211F34")
        self.ccaLoginDetailsFrame.grid(row = 4, column = 6, columnspan = 4)

            #Title
        self.ccaLoginDetailsTitle = Label(self.ccaLoginDetailsFrame, text = "Login Details", width = 15, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 24))
        self.ccaLoginDetailsTitle.grid(row = 0, columnspan = 2)

            #Username

                #Label
        self.ccaUsernameLabel = Label(self.ccaLoginDetailsFrame, text = "Username", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaUsernameLabel.grid(row = 1, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaUsernameEntry = Entry(self.ccaLoginDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaUsernameEntry.grid(row = 1, column = 1, padx = 5, pady = 10)
        
            #Password

                #Label
        self.ccaPasswordLabel = Label(self.ccaLoginDetailsFrame, text = "Password", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaPasswordLabel.grid(row = 2, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaPasswordEntry = Entry(self.ccaLoginDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaPasswordEntry.grid(row = 2, column = 1, padx = 5, pady = 10)
        
            #Backup Key

                #Label
        self.ccaBackupKeyLabel = Label(self.ccaLoginDetailsFrame, text = "Backup Key", width = 8, pady = 10, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.ccaBackupKeyLabel.grid(row = 4, column = 0, padx = 5, pady = 10)
                #Entry Box
        self.ccaBackupKeyEntry = Entry(self.ccaLoginDetailsFrame, width = 20, borderwidth = 3, font = ("Tahoma", 14))
        self.ccaBackupKeyEntry.grid(row = 4, column = 1, padx = 5, pady = 10)

        #Submit Button 
        self.ccaSubmitButton = Button(self.ccaLoginDetailsFrame, text = "Submit", padx = 80, font = ("Tahoma", 21), command = self.CCA_AddRecord)
        self.ccaSubmitButton.grid(row = 6, columnspan = 2, padx = 10, pady = 10)

    def CCA_AddRecord(self):

        #Passing the input entry boxes through to the CCA_AddRecord function
        self.cForname = self.ccaFornameEntry.get()
        self.cSurname = self.ccaSurnameEntry.get()
        self.cPhoneNo = self.ccaPhoneNoEntry.get()
        self.cEmail = self.ccaEmailEntry.get()
        self.cAddress = self.ccaAddressEntry.get()
        self.cPostcode = self.ccaPostcodeEntry.get()

        self.cUsername = self.ccaUsernameEntry.get()
        self.cPassword = self.ccaPasswordEntry.get()
        self.cBackupKey = self.ccaBackupKeyEntry.get()

        if len(self.cForname) == 0 or len(self.cSurname) == 0 or len(self.cPhoneNo) == 0 or len(self.cEmail) == 0 or len(self.cAddress) == 0 or len(self.cPostcode) == 0 or len(self.cUsername) == 0 or len(self.cPassword) == 0 or len(self.cBackupKey) == 0:
            messagebox.showinfo("Could not add new record", "Could not add new record\nFill in all Login and Customer Details")

        else:

            if len(self.cPhoneNo) != 11:
                messagebox.showinfo("Could not add new record", "Phone number must be 11 characters")
                
            else:

                try:
                    int(self.cPhoneNo)
                    intPhoneNo = True
                    
                except ValueError:
                    messagebox.showinfo("Could not add new record", "Phone number must be an integer")
                    intPhoneNo = False

                if intPhoneNo == True:
                    #Reads all the records in the customer details file for primary key incrementation
                    self.CustomerDetailsFile = open("CustomerDetails.txt","r")

                    self.ccaCountRow = 0

                    for row in self.CustomerDetailsFile:
                        self.ccaCountRow += 1

                    self.CustomerDetailsFile.close()

                    #Adds a record in the customer details file
                    self.CustomerDetailsFile = open("CustomerDetails.txt","a")

                    self.CustomerDetailsFile.write("C#" + str(self.ccaCountRow + 1) + "," + self.cForname + "," + self.cSurname + "," + self.cPhoneNo + "," + self.cEmail + "," + self.cAddress + "," + self.cPostcode + "\n")

                    self.CustomerDetailsFile.close()
                    
                    #Adds a record in the customer account file
                    self.CustomerAccountFile = open("CustomerAccount.txt","a")

                    self.CustomerAccountFile.write("C#" + str(self.ccaCountRow + 1) + "," + self.cUsername + "," + self.cPassword + "," + self.cBackupKey + "\n")

                    self.CustomerAccountFile.close()

                    #Messagebox to indicate to the user that the customer account has been made
                    messagebox.showinfo("Customer Account has been made", "Customer Account: " + self.cUsername + "\nhas been made")

                    self.ccaScreen.destroy()

                else:
                    pass

#####Menu Screen###################################################################################################################
class MenuWindow:

    #Creating Screen
    def __init__(self, menuScreen):
        self.menuScreen = menuScreen     
        self.menuScreen.resizable(False, False)
        self.menuScreen.configure(background = "#BE002B")

        #Title

        #Tab
        self.menuScreen.title("Menu")
        #Screen
        self.menuTitle = Label(self.menuScreen, text = "Menu", width = 20, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.menuTitle.grid(row = 1, columnspan = 6)
        #Border
        self.menuTopBorder = LabelFrame(self.menuScreen, width = 546, height = 15, background = "#211F34")
        self.menuTopBorder.grid(row = 0, columnspan = 6)
        self.menuBottomBorder = LabelFrame(self.menuScreen, width = 546, height = 15, background = "#211F34")
        self.menuBottomBorder.grid(row = 2, columnspan = 6)

        #Screen Spacing
        self.menuTopSpace = LabelFrame(self.menuScreen, width = 546, height = 71, background = "#BE002B")
        self.menuTopSpace.grid(row = 3, columnspan = 6)
        self.menuBottomSpace = LabelFrame(self.menuScreen, width = 546, height = 71, background = "#BE002B")
        self.menuBottomSpace.grid(row = 5, columnspan = 6)

        #Menu Frame
        self.menuFrame = LabelFrame(self.menuScreen, padx = 10, pady = 10, background = "#211F34")
        self.menuFrame.grid(row = 4, columnspan = 6)

        #Buttons

            #Appetisers
        self.menuAppetisersButton = Button(self.menuFrame, text = "Appetisers", width = 22, pady = 5, font = ("Tahoma", 24), command = self.Appetisers)
        self.menuAppetisersButton.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
            #Mains
        self.menuMainsButton = Button(self.menuFrame, text = "Mains", width = 22, pady = 12,  font = ("Tahoma", 24), command = self.Mains)
        self.menuMainsButton.grid(row = 1, columnspan = 2, padx = 10, pady = 10)
            #Desserts
        self.menuDessertsButton = Button(self.menuFrame, text = "Desserts", width = 9, pady = 5, font = ("Tahoma", 24), command = self.Desserts)
        self.menuDessertsButton.grid(row = 2, column = 0, padx = 10, pady = 10)
            #Drinks
        self.menuDrinksButton = Button(self.menuFrame, text = "Drinks", width = 9, pady = 5, font = ("Tahoma", 24), command = self.Drinks)
        self.menuDrinksButton.grid(row = 2, column = 1, padx = 10, pady = 10)

#####Adding Appetisers Screen#####
    def Appetisers(self):
        self.Appetisers = Toplevel(self.menuScreen)
        self.app = AppetisersWindow(self.Appetisers)

#####Adding Create Customer Account Screen#####
    def Mains(self):
        self.Mains = Toplevel(self.menuScreen)
        self.app = MainsWindow(self.Mains)

#####Adding Desserts Screen#####
    def Desserts(self):
        self.Desserts = Toplevel(self.menuScreen)
        self.app = DessertsWindow(self.Desserts)

#####Adding Drinks Screen#####
    def Drinks(self):
        self.Drinks = Toplevel(self.menuScreen)
        self.app = DrinksWindow(self.Drinks)
        
#####Appetisers Screen####################################################################################################
class AppetisersWindow:
        
    #Creating screen
    def __init__(self, appetisersScreen):
        self.appetisersScreen = appetisersScreen           
        self.appetisersScreen.resizable(False, False)
        self.appetisersScreen.configure(background = "#BE002B")

    #Title

        #Tab
        self.appetisersScreen.title("Appetisers") 
        #Screen
        self.appetisersTitle = Label(self.appetisersScreen, text = "Appetisers", width = 25, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.appetisersTitle.grid(row = 1, columnspan = 20)
        #Border
        self.appetisersTopBorder = LabelFrame(self.appetisersScreen, width = 681, height = 15, background = "#211F34")
        self.appetisersTopBorder.grid(row = 0, columnspan = 20)
        self.appetisersBottomBorder = LabelFrame(self.appetisersScreen, width = 681, height = 15, background = "#211F34")
        self.appetisersBottomBorder.grid(row = 2, columnspan = 20)

    #Screen Spacing
        self.appetisersTopSpace = LabelFrame(self.appetisersScreen, width = 681, height = 45, background = "#BE002B")
        self.appetisersTopSpace.grid(row = 3, columnspan = 20)
        self.appetisersBottomSpace = LabelFrame(self.appetisersScreen, width = 681, height = 45, background = "#BE002B")
        self.appetisersBottomSpace.grid(row = 5, columnspan = 20)

        #Frame
        self.appetisersFrame = LabelFrame(self.appetisersScreen, padx = 10, pady = 10, background = "#211F34")
        self.appetisersFrame.grid(row = 4, column = 1, columnspan = 18)

            #Adding a variable for the radio buttons
        self.appetisersRadioButtonVar = StringVar()
        self.appetisersRadioButtonVar.set(None)

            #Item (x,y)
            #Miso Soup (0,0)

                #Name Radio Button
        self.appetisersMisoSoupRadioButton = Radiobutton(self.appetisersFrame, text = "Miso Soup",
                                                         variable = self.appetisersRadioButtonVar, value = "Miso Soup", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersMisoSoupRadioButton.grid(row = 0, column = 0)

                #Cost Label
        self.appetisersMisoSoupCost = Label(self.appetisersFrame, text = "£1.75", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersMisoSoupCost.grid(row = 0, column = 1)
        
                #Image Open
        self.appetisersMisoSoupImage = Image.open("Miso Soup.jpg")
        self.appetisersMisoSoupImage = ImageTk.PhotoImage(self.appetisersMisoSoupImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.appetisersMisoSoupLabel = Label(self.appetisersFrame, image = self.appetisersMisoSoupImage)
        self.appetisersMisoSoupLabel.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Edamame (0,1)

                #Name Radio Button
        self.appetisersEdamameRadioButton = Radiobutton(self.appetisersFrame, text = "Edamame",
                                                        variable = self.appetisersRadioButtonVar, value = "Edamame", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersEdamameRadioButton.grid(row = 0, column = 2)

                #Cost Label
        self.appetisersEdamameCost = Label(self.appetisersFrame, text = "£2.50", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersEdamameCost.grid(row = 0, column = 3)
        
                #Image Open
        self.appetisersEdamameImage = Image.open("Edamame.jpg")
        self.appetisersEdamameImage = ImageTk.PhotoImage(self.appetisersEdamameImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.appetisersEdamameLabel = Label(self.appetisersFrame, image = self.appetisersEdamameImage)
        self.appetisersEdamameLabel.grid(row = 1, column = 2, columnspan = 2, padx = 5, pady = 5)

            #Salmon Teriyaki (0,2)

                #Name Radio Button
        self.appetisersSalmonTeriyakiRadioButton = Radiobutton(self.appetisersFrame, text = "Salmon Teriyaki",
                                                               variable = self.appetisersRadioButtonVar, value = "Salmon Teriyaki", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersSalmonTeriyakiRadioButton.grid(row = 0, column = 4)

                #Cost Label
        self.appetisersSalmonTeriyakiCost = Label(self.appetisersFrame, text = "£3.75", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersSalmonTeriyakiCost.grid(row = 0, column = 5)

                #Image Open
        self.appetisersSalmonTeriyakiImage = Image.open("Salmon Teriyaki.jpg")
        self.appetisersSalmonTeriyakiImage = ImageTk.PhotoImage(self.appetisersSalmonTeriyakiImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.appetisersSalmonTeriyakiLabel = Label(self.appetisersFrame, image = self.appetisersSalmonTeriyakiImage)
        self.appetisersSalmonTeriyakiLabel.grid(row = 1, column = 4, columnspan = 2, padx = 5, pady = 5)

            #Onigiri (0,3)

                #Name Radio Button
        self.appetisersOnigiriRadioButton = Radiobutton(self.appetisersFrame, text = "Onigiri",
                                                        variable = self.appetisersRadioButtonVar, value = "Onigiri", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersOnigiriRadioButton.grid(row = 0, column = 6)

                #Cost Label
        self.appetisersOnigiriCost = Label(self.appetisersFrame, text = "£2.25", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersOnigiriCost.grid(row = 0, column = 7)

                #Image Open
        self.appetisersOnigiriImage = Image.open("Onigiri.jpg")
        self.appetisersOnigiriImage = ImageTk.PhotoImage(self.appetisersOnigiriImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.appetisersOnigiriLabel = Label(self.appetisersFrame, image = self.appetisersOnigiriImage)
        self.appetisersOnigiriLabel.grid(row = 1, column = 6, columnspan = 2, padx = 5, pady = 5)
        
            #Hiyayakko (2,0)

                #Name Radio Button
        self.appetisersHiyayakkoRadioButton = Radiobutton(self.appetisersFrame, text = "Hiyayakko",
                                                          variable = self.appetisersRadioButtonVar, value = "Hiyayakko", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersHiyayakkoRadioButton.grid(row = 2, column = 0)

                #Cost Label
        self.appetisersHiyayakkoCost = Label(self.appetisersFrame, text = "£4.75", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersHiyayakkoCost.grid(row = 2, column = 1)

                #Image Open
        self.appetisersHiyayakkoImage = Image.open("Hiyayakko.jpg")
        self.appetisersHiyayakkoImage = ImageTk.PhotoImage(self.appetisersHiyayakkoImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.appetisersHiyayakkoLabel = Label(self.appetisersFrame, image = self.appetisersHiyayakkoImage)
        self.appetisersHiyayakkoLabel.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Chicken Gyoza (2,1)

                #Name Radio Button
        self.appetisersChickenGyozaRadioButton = Radiobutton(self.appetisersFrame, text = "Chicken Gyoza",
                                                             variable = self.appetisersRadioButtonVar, value = "Chicken Gyoza", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersChickenGyozaRadioButton.grid(row = 2, column = 2)

                #Cost Label
        self.appetisersChickenGyozaCost = Label(self.appetisersFrame, text = "£6.00", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersChickenGyozaCost.grid(row = 2, column = 3)
        
                #Image Open
        self.appetisersChickenGyozaImage = Image.open("Chicken Gyoza.jpg")
        self.appetisersChickenGyozaImage = ImageTk.PhotoImage(self.appetisersChickenGyozaImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.appetisersChickenGyozaLabel = Label(self.appetisersFrame, image = self.appetisersChickenGyozaImage)
        self.appetisersChickenGyozaLabel.grid(row = 3, column = 2, columnspan = 2, padx = 5, pady = 5)

            #Takoyaki (2,2)

                #Name Radio Button
        self.appetisersTakoyakiRadioButton = Radiobutton(self.appetisersFrame, text = "Takoyaki",
                                                         variable = self.appetisersRadioButtonVar, value = "Takoyaki", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersTakoyakiRadioButton.grid(row = 2, column = 4)

                #Cost Label
        self.appetisersTakoyakiCost = Label(self.appetisersFrame, text = "£8.00", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersTakoyakiCost.grid(row = 2, column = 5)

                #Image Open
        self.appetisersTakoyakiImage = Image.open("Takoyaki.jpg")
        self.appetisersTakoyakiImage = ImageTk.PhotoImage(self.appetisersTakoyakiImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.appetisersTakoyakiLabel = Label(self.appetisersFrame, image = self.appetisersTakoyakiImage)
        self.appetisersTakoyakiLabel.grid(row = 3, column = 4, columnspan = 2, padx = 5, pady = 5)

            #Prawn Tempura (2,3)

                #Name Radio Button
        self.appetisersPrawnTempuraRadioButton = Radiobutton(self.appetisersFrame, text = "Prawn Tempura",
                                                             variable = self.appetisersRadioButtonVar, value = "Prawn Tempura", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersPrawnTempuraRadioButton.grid(row = 2, column = 6)

                #Cost Label
        self.appetisersPrawnTempuraCost = Label(self.appetisersFrame, text = "£3.50", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.appetisersPrawnTempuraCost.grid(row = 2, column = 7)

                #Image Open
        self.appetisersPrawnTempuraImage = Image.open("Prawn Tempura.jpg")
        self.appetisersPrawnTempuraImage = ImageTk.PhotoImage(self.appetisersPrawnTempuraImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.appetisersPrawnTempuraLabel = Label(self.appetisersFrame, image = self.appetisersPrawnTempuraImage)
        self.appetisersPrawnTempuraLabel.grid(row = 3, column = 6, columnspan = 2, padx = 5, pady = 5)

        #Submit Button 
        self.appetisersAddButton = Button(self.appetisersFrame, text = "Add", width = 5, font = ("Tahoma", 28), command = self.Appetisers_AddToCart)
        self.appetisersAddButton.grid(row = 4, column = 6, columnspan = 2, padx = 5, pady = 5)
        
    def Appetisers_AddToCart(self):
        global cartItemA
        global cartItemACost
        
        if self.appetisersRadioButtonVar.get() == "Miso Soup":
            cartItemA = "Miso Soup"
            cartItemACost = 1.75
            self.appetisersScreen.destroy()

        elif self.appetisersRadioButtonVar.get() == "Edamame":
            cartItemA = "Edamame"
            cartItemACost = 2.50
            self.appetisersScreen.destroy()

        elif self.appetisersRadioButtonVar.get() == "Salmon Teriyaki":
            cartItemA = "Salmon Teriyaki"
            cartItemACost = 3.75
            self.appetisersScreen.destroy()

        elif self.appetisersRadioButtonVar.get() == "Hiyayakko":
            cartItemA = "Hiyayakko"
            cartItemACost = 4.75
            self.appetisersScreen.destroy()

        elif self.appetisersRadioButtonVar.get() == "Chicken Gyoza":
            cartItemA = "Chicken Gyoza"
            cartItemACost = 6.00
            self.appetisersScreen.destroy()

        elif self.appetisersRadioButtonVar.get() == "Takoyaki":
            cartItemA = "Takoyaki"
            cartItemACost = 8.00
            self.appetisersScreen.destroy()

        elif self.appetisersRadioButtonVar.get() == "Onigiri":
            cartItemA = "Onigiri"
            cartItemACost = 2.25
            self.appetisersScreen.destroy()

        elif self.appetisersRadioButtonVar.get() == "Prawn Tempura":
            cartItemA = "Prawn Tempura"
            cartItemACost = 3.50
            self.appetisersScreen.destroy()

        else:
            print("failed")

#######Mains Screen###################################################################################################################
##class MainsWindow:
##
##    #Creating Screen
##    def __init__(self, mainsScreen):
##        self.mainsScreen = mainsScreen     
##        self.mainsScreen.resizable(False, False)
##        self.mainsScreen.configure(background = "#BE002B")
##
##        #Title
##
##        #Tab
##        self.mainsScreen.title("Menu")
##        #Screen
##        self.mainsTitle = Label(self.mainsScreen, text = "Menu", width = 20, height = 1, background = "#ffffff", font = ("Tahoma", 48))
##        self.mainsTitle.grid(row = 1, columnspan = 6)
##        #Border
##        self.mainsTopBorder = LabelFrame(self.mainsScreen, width = 546, height = 15, background = "#211F34")
##        self.mainsTopBorder.grid(row = 0, columnspan = 6)
##        self.mainsBottomBorder = LabelFrame(self.mainsScreen, width = 546, height = 15, background = "#211F34")
##        self.mainsBottomBorder.grid(row = 2, columnspan = 6)
##
##        #Screen Spacing
##        self.mainsTopSpace = LabelFrame(self.mainsScreen, width = 546, height = 71, background = "#BE002B")
##        self.mainsTopSpace.grid(row = 3, columnspan = 6)
##        self.mainsBottomSpace = LabelFrame(self.mainsScreen, width = 546, height = 71, background = "#BE002B")
##        self.mainsBottomSpace.grid(row = 5, columnspan = 6)
##
##        #Menu Frame
##        self.mainsFrame = LabelFrame(self.mainsScreen, padx = 10, pady = 10, background = "#211F34")
##        self.mainsFrame.grid(row = 4, columnspan = 6)
##
##        #Buttons
##
##            #Noodles
##        self.mainsNoodlesButton = Button(self.mainsFrame, text = "Noodles", width = 8, pady = 20, font = ("Tahoma", 24), )#command = Appetisers)
##        self.mainsNoodlesButton.grid(row = 0, column = 0, padx = 10, pady = 10)
##            #Rice
##        self.mainsRiceButton = Button(self.mainsFrame, text = "Rice", width = 8, pady = 20,  font = ("Tahoma", 24), )#command = Mains)
##        self.mainsRiceButton.grid(row = 0, column = 1, padx = 10, pady = 10)
##            #Other
##        self.mainsOtherButton = Button(self.mainsFrame, text = "Other", width = 22, pady = 5, font = ("Tahoma", 24), )#command = Desserts)
##        self.mainsOtherButton.grid(row = 1, columnspan = 2, padx = 10, pady = 10)

#####Mains Screen####################################################################################################
class MainsWindow:
        
    #Creating screen
    def __init__(self, mainsScreen):
        self.mainsScreen = mainsScreen           
        self.mainsScreen.resizable(False, False)
        self.mainsScreen.configure(background = "#BE002B")

    #Title

        #Tab
        self.mainsScreen.title("Mains") 
        #Screen
        self.mainsTitle = Label(self.mainsScreen, text = "Mains", width = 25, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.mainsTitle.grid(row = 1, columnspan = 10)
        #Border
        self.mainsTopBorder = LabelFrame(self.mainsScreen, width = 681, height = 15, background = "#211F34")
        self.mainsTopBorder.grid(row = 0, columnspan = 10)
        self.mainsBottomBorder = LabelFrame(self.mainsScreen, width = 681, height = 15, background = "#211F34")
        self.mainsBottomBorder.grid(row = 2, columnspan = 10)

    #Screen Spacing
        self.mainsTopSpace = LabelFrame(self.mainsScreen, width = 681, height = 45, background = "#BE002B")
        self.mainsTopSpace.grid(row = 3, columnspan = 10)
        self.mainsBottomSpace = LabelFrame(self.mainsScreen, width = 681, height = 45, background = "#BE002B")
        self.mainsBottomSpace.grid(row = 5, columnspan = 10)

        #Frame
        self.mainsFrame = LabelFrame(self.mainsScreen, padx = 10, pady = 10, background = "#211F34")
        self.mainsFrame.grid(row = 4, column = 1, columnspan = 8)

            #Adding a variable for the radio buttons
        self.mainsRadioButtonVar = StringVar()
        self.mainsRadioButtonVar.set(None)

            #Item (x,y)
            #Chicken Katsu Curry (0,0)

                #Name Radio Button
        self.mainsChickenKatsuCurryRadioButton = Radiobutton(self.mainsFrame, text = "Chicken\nKatsu Curry",
                                                             variable = self.mainsRadioButtonVar, value = "Chicken Katsu Curry", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsChickenKatsuCurryRadioButton.grid(row = 0, column = 0)

                #Cost Label
        self.mainsChickenKatsuCurryCost = Label(self.mainsFrame, text = "£11.50", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsChickenKatsuCurryCost.grid(row = 0, column = 1)
        
                #Image Open
        self.mainsChickenKatsuCurryImage = Image.open("Chicken Katsu Curry.jpg")
        self.mainsChickenKatsuCurryImage = ImageTk.PhotoImage(self.mainsChickenKatsuCurryImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.mainsChickenKatsuCurryLabel = Label(self.mainsFrame, image = self.mainsChickenKatsuCurryImage)
        self.mainsChickenKatsuCurryLabel.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Eel Rice Bowl (0,1)

                #Name Radio Button
        self.mainsEelRiceBowlRadioButton = Radiobutton(self.mainsFrame, text = "Eel Rice\nBowl",
                                                       variable = self.mainsRadioButtonVar, value = "Eel Rice Bowl", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsEelRiceBowlRadioButton.grid(row = 0, column = 2)

                #Cost Label
        self.mainsEelRiceBowlCost = Label(self.mainsFrame, text = "£14.00", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsEelRiceBowlCost.grid(row = 0, column = 3)
        
                #Image Open
        self.mainsEelRiceBowlImage = Image.open("Eel Rice Bowl.jpg")
        self.mainsEelRiceBowlImage = ImageTk.PhotoImage(self.mainsEelRiceBowlImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.mainsEelRiceBowlLabel = Label(self.mainsFrame, image = self.mainsEelRiceBowlImage)
        self.mainsEelRiceBowlLabel.grid(row = 1, column = 2, columnspan = 2, padx = 5, pady = 5)

            #Mushroom Ramen (0,2)

                #Name Radio Button
        self.mainsMushroomRamenRadioButton = Radiobutton(self.mainsFrame, text = "Mushroom\nRamen",
                                                         variable = self.mainsRadioButtonVar, value = "Mushroom Ramen", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsMushroomRamenRadioButton.grid(row = 0, column = 4)

                #Cost Label
        self.mainsMushroomRamenCost = Label(self.mainsFrame, text = "£11.25", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsMushroomRamenCost.grid(row = 0, column = 5)

                #Image Open
        self.mainsMushroomRamenImage = Image.open("Mushroom Ramen.jpg")
        self.mainsMushroomRamenImage = ImageTk.PhotoImage(self.mainsMushroomRamenImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.mainsMushroomRamenLabel = Label(self.mainsFrame, image = self.mainsMushroomRamenImage)
        self.mainsMushroomRamenLabel.grid(row = 1, column = 4, columnspan = 2, padx = 5, pady = 5)

            #Yasai Yaki Udon (2,0)

                #Name Radio Button
        self.mainsYasaiYakiUdonRadioButton = Radiobutton(self.mainsFrame, text = "Yasai Yaki\nUdon",
                                                         variable = self.mainsRadioButtonVar, value = "Yasai Yaki Udon", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsYasaiYakiUdonRadioButton.grid(row = 2, column = 0)

                #Cost Label
        self.mainsYasaiYakiUdonCost = Label(self.mainsFrame, text = "£13.25", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsYasaiYakiUdonCost.grid(row = 2, column = 1)

                #Image Open
        self.mainsYasaiYakiUdonImage = Image.open("Yasai Yaki Udon.jpg")
        self.mainsYasaiYakiUdonImage = ImageTk.PhotoImage(self.mainsYasaiYakiUdonImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.mainsYasaiYakiUdonLabel = Label(self.mainsFrame, image = self.mainsYasaiYakiUdonImage)
        self.mainsYasaiYakiUdonLabel.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Okonomiyaki (2,1)

                #Name Radio Button
        self.mainsOkonomiyakiRadioButton = Radiobutton(self.mainsFrame, text = "Okonomiyaki",
                                                       variable = self.mainsRadioButtonVar, value = "Okonomiyaki", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsOkonomiyakiRadioButton.grid(row = 2, column = 2)

                #Cost Label
        self.mainsOkonomiyakiCost = Label(self.mainsFrame, text = "£12.75", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.mainsOkonomiyakiCost.grid(row = 2, column = 3)
        
                #Image Open
        self.mainsOkonomiyakiImage = Image.open("Okonomiyaki.jpg")
        self.mainsOkonomiyakiImage = ImageTk.PhotoImage(self.mainsOkonomiyakiImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.mainsOkonomiyakiLabel = Label(self.mainsFrame, image = self.mainsOkonomiyakiImage)
        self.mainsOkonomiyakiLabel.grid(row = 3, column = 2, columnspan = 2, padx = 5, pady = 5)

        #Submit Button 
        self.mainsAddButton = Button(self.mainsFrame, text = "Add", width = 5, font = ("Tahoma", 28), command = self.Mains_AddToCart)
        self.mainsAddButton.grid(row = 2, rowspan = 2, column = 4, columnspan = 2, padx = 5, pady = 5)
        
    def Mains_AddToCart(self):
        global cartItemB
        global cartItemBCost
        
        if self.mainsRadioButtonVar.get() == "Chicken Katsu Curry":
            cartItemB = "Chicken Katsu Curry"
            cartItemBCost = 11.50
            self.mainsScreen.destroy()

        elif self.mainsRadioButtonVar.get() == "Eel Rice Bowl":
            cartItemB = "Eel Rice Bowl"
            cartItemBCost = 14.00
            self.mainsScreen.destroy()

        elif self.mainsRadioButtonVar.get() == "Mushroom Ramen":
            cartItemB = "Mushroom Ramen"
            cartItemBCost = 11.25
            self.mainsScreen.destroy()

        elif self.mainsRadioButtonVar.get() == "Yasai Yaki Udon":
            cartItemB = "Yasai Yaki Udon"
            cartItemBCost = 13.25
            self.mainsScreen.destroy()

        elif self.mainsRadioButtonVar.get() ==  "Okonomiyaki":
            cartItemB = "Okonomiyaki"
            cartItemBCost = 12.75
            self.mainsScreen.destroy()

        else:
            print("failed")

#####Desserts Screen####################################################################################################
class DessertsWindow:
        
    #Creating screen
    def __init__(self, dessertsScreen):
        self.dessertsScreen = dessertsScreen           
        self.dessertsScreen.resizable(False, False)
        self.dessertsScreen.configure(background = "#BE002B")

    #Title

        #Tab
        self.dessertsScreen.title("Desserts") 
        #Screen
        self.dessertsTitle = Label(self.dessertsScreen, text = "Desserts", width = 25, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.dessertsTitle.grid(row = 1, columnspan = 10)
        #Border
        self.dessertsTopBorder = LabelFrame(self.dessertsScreen, width = 681, height = 15, background = "#211F34")
        self.dessertsTopBorder.grid(row = 0, columnspan = 10)
        self.dessertsBottomBorder = LabelFrame(self.dessertsScreen, width = 681, height = 15, background = "#211F34")
        self.dessertsBottomBorder.grid(row = 2, columnspan = 10)

    #Screen Spacing
        self.dessertsTopSpace = LabelFrame(self.dessertsScreen, width = 681, height = 45, background = "#BE002B")
        self.dessertsTopSpace.grid(row = 3, columnspan = 10)
        self.dessertsBottomSpace = LabelFrame(self.dessertsScreen, width = 681, height = 45, background = "#BE002B")
        self.dessertsBottomSpace.grid(row = 5, columnspan = 10)

        #Frame
        self.dessertsFrame = LabelFrame(self.dessertsScreen, padx = 10, pady = 10, background = "#211F34")
        self.dessertsFrame.grid(row = 4, column = 1, columnspan = 8)

            #Adding a variable for the radio buttons
        self.dessertsRadioButtonVar = StringVar()
        self.dessertsRadioButtonVar.set(None)

            #Item (x,y)
            #Red Bean Soup (0,0)

                #Name Radio Button
        self.dessertsRedBeanSoupRadioButton = Radiobutton(self.dessertsFrame, text = "Red Bean\nSoup",
                                                          variable = self.dessertsRadioButtonVar, value = "Red Bean Soup", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsRedBeanSoupRadioButton.grid(row = 0, column = 0)

                #Cost Label
        self.dessertsRedBeanSoupCost = Label(self.dessertsFrame, text = "£1.75", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsRedBeanSoupCost.grid(row = 0, column = 1)
        
                #Image Open
        self.dessertsRedBeanSoupImage = Image.open("Red Bean Soup.jpg")
        self.dessertsRedBeanSoupImage = ImageTk.PhotoImage(self.dessertsRedBeanSoupImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.dessertsRedBeanSoupLabel = Label(self.dessertsFrame, image = self.dessertsRedBeanSoupImage)
        self.dessertsRedBeanSoupLabel.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Matcha Ice Cream (0,1)

                #Name Radio Button
        self.dessertsMatchaIceCreamRadioButton = Radiobutton(self.dessertsFrame, text = "Matcha\nIce Cream",
                                                             variable = self.dessertsRadioButtonVar, value = "Matcha Ice Cream", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsMatchaIceCreamRadioButton.grid(row = 0, column = 2)

                #Cost Label
        self.dessertsMatchaIceCreamCost = Label(self.dessertsFrame, text = "£2.50", width = 5, pady = 6, foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsMatchaIceCreamCost.grid(row = 0, column = 3)
        
                #Image Open
        self.dessertsMatchaIceCreamImage = Image.open("Matcha Ice Cream.jpg")
        self.dessertsMatchaIceCreamImage = ImageTk.PhotoImage(self.dessertsMatchaIceCreamImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.dessertsMatchaIceCreamLabel = Label(self.dessertsFrame, image = self.dessertsMatchaIceCreamImage)
        self.dessertsMatchaIceCreamLabel.grid(row = 1, column = 2, columnspan = 2, padx = 5, pady = 5)

            #Anmitsu (0,2)

                #Name Radio Button
        self.dessertsAnmitsuRadioButton = Radiobutton(self.dessertsFrame, text = "Anmitsu",
                                                      variable = self.dessertsRadioButtonVar, value = "Anmitsu", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsAnmitsuRadioButton.grid(row = 0, column = 4)

                #Cost Label
        self.dessertsAnmitsuCost = Label(self.dessertsFrame, text = "£4.25", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsAnmitsuCost.grid(row = 0, column = 5)

                #Image Open
        self.dessertsAnmitsuImage = Image.open("Anmitsu.jpg")
        self.dessertsAnmitsuImage = ImageTk.PhotoImage(self.dessertsAnmitsuImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.dessertsAnmitsuLabel = Label(self.dessertsFrame, image = self.dessertsAnmitsuImage)
        self.dessertsAnmitsuLabel.grid(row = 1, column = 4, columnspan = 2, padx = 5, pady = 5)

            #Hanami Dango (2,0)

                #Name Radio Button
        self.dessertsHanamiDangoRadioButton = Radiobutton(self.dessertsFrame, text = "Hanami\nDango",
                                                          variable = self.dessertsRadioButtonVar, value = "Hanami Dango", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsHanamiDangoRadioButton.grid(row = 2, column = 0)

                #Cost Label
        self.dessertsHanamiDangoCost = Label(self.dessertsFrame, text = "£2.75", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsHanamiDangoCost.grid(row = 2, column = 1)

                #Image Open
        self.dessertsHanamiDangoImage = Image.open("Hanami Dango.jpg")
        self.dessertsHanamiDangoImage = ImageTk.PhotoImage(self.dessertsHanamiDangoImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.dessertsHanamiDangoLabel = Label(self.dessertsFrame, image = self.dessertsHanamiDangoImage)
        self.dessertsHanamiDangoLabel.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Mango Mochi (2,1)

                #Name Radio Button
        self.dessertsMangoMochiRadioButton = Radiobutton(self.dessertsFrame, text = "Mango\nMochi",
                                                         variable = self.dessertsRadioButtonVar, value = "Mango Mochi", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsMangoMochiRadioButton.grid(row = 2, column = 2)

                #Cost Label
        self.dessertsMangoMochiCost = Label(self.dessertsFrame, text = "£2.25", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.dessertsMangoMochiCost.grid(row = 2, column = 3)
        
                #Image Open
        self.dessertsMangoMochiImage = Image.open("Mango Mochi.jpg")
        self.dessertsMangoMochiImage = ImageTk.PhotoImage(self.dessertsMangoMochiImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.dessertsMangoMochiLabel = Label(self.dessertsFrame, image = self.dessertsMangoMochiImage)
        self.dessertsMangoMochiLabel.grid(row = 3, column = 2, columnspan = 2, padx = 5, pady = 5)

        #Submit Button 
        self.dessertsAddButton = Button(self.dessertsFrame, text = "Add", width = 5, font = ("Tahoma", 28), command = self.Desserts_AddToCart)
        self.dessertsAddButton.grid(row = 2, rowspan = 2, column = 4, columnspan = 2, padx = 5, pady = 5)
        
    def Desserts_AddToCart(self):
        global cartItemC
        global cartItemCCost
        
        if self.dessertsRadioButtonVar.get() == "Red Bean Soup":
            cartItemC = "Red Bean Soup"
            cartItemCCost = 1.75
            self.dessertsScreen.destroy()

        elif self.dessertsRadioButtonVar.get() == "Matcha Ice Cream":
            cartItemC = "Matcha Ice Cream"
            cartItemCCost = 2.50
            self.dessertsScreen.destroy()

        elif self.dessertsRadioButtonVar.get() == "Anmitsu":
            cartItemC = "Anmitsu"
            cartItemCCost = 4.25
            self.dessertsScreen.destroy()

        elif self.dessertsRadioButtonVar.get() == "Hanami Dango":
            cartItemC = "Hanami Dango"
            cartItemCCost = 2.75
            self.dessertsScreen.destroy()

        elif self.dessertsRadioButtonVar.get() ==  "Mango Mochi":
            cartItemC = "Mango Mochi"
            cartItemCCost = 2.25
            self.dessertsScreen.destroy()

        else:
            print("failed")

#####Drinks Screen####################################################################################################
class DrinksWindow:
        
    #Creating screen
    def __init__(self, drinksScreen):
        self.drinksScreen = drinksScreen           
        self.drinksScreen.resizable(False, False)
        self.drinksScreen.configure(background = "#BE002B")

    #Title

        #Tab
        self.drinksScreen.title("Drinks") 
        #Screen
        self.drinksTitle = Label(self.drinksScreen, text = "Drinks", width = 25, height = 1, background = "#ffffff", font = ("Tahoma", 48))
        self.drinksTitle.grid(row = 1, columnspan = 10)
        #Border
        self.drinksTopBorder = LabelFrame(self.drinksScreen, width = 681, height = 15, background = "#211F34")
        self.drinksTopBorder.grid(row = 0, columnspan = 10)
        self.drinksBottomBorder = LabelFrame(self.drinksScreen, width = 681, height = 15, background = "#211F34")
        self.drinksBottomBorder.grid(row = 2, columnspan = 10)

    #Screen Spacing
        self.drinksTopSpace = LabelFrame(self.drinksScreen, width = 681, height = 45, background = "#BE002B")
        self.drinksTopSpace.grid(row = 3, columnspan = 10)
        self.drinksBottomSpace = LabelFrame(self.drinksScreen, width = 681, height = 45, background = "#BE002B")
        self.drinksBottomSpace.grid(row = 5, columnspan = 10)

        #Frame
        self.drinksFrame = LabelFrame(self.drinksScreen, padx = 10, pady = 10, background = "#211F34")
        self.drinksFrame.grid(row = 4, column = 1, columnspan = 8)

            #Adding a variable for the radio buttons
        self.drinksRadioButtonVar = StringVar()
        self.drinksRadioButtonVar.set(None)

            #Item (x,y)
            #Green Tea (0,0)

                #Name Radio Button
        self.drinksGreenTeaRadioButton = Radiobutton(self.drinksFrame, text = "Green Tea",
                                                     variable = self.drinksRadioButtonVar, value = "Green Tea", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksGreenTeaRadioButton.grid(row = 0, column = 0)

                #Cost Label
        self.drinksGreenTeaCost = Label(self.drinksFrame, text = "£1.50", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksGreenTeaCost.grid(row = 0, column = 1)
        
                #Image Open
        self.drinksGreenTeaImage = Image.open("Green Tea.jpg")
        self.drinksGreenTeaImage = ImageTk.PhotoImage(self.drinksGreenTeaImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.drinksGreenTeaLabel = Label(self.drinksFrame, image = self.drinksGreenTeaImage)
        self.drinksGreenTeaLabel.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Sake (0,1)

                #Name Radio Button
        self.drinksSakeRadioButton = Radiobutton(self.drinksFrame, text = "Sake",
                                                 variable = self.drinksRadioButtonVar, value = "Sake", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksSakeRadioButton.grid(row = 0, column = 2)

                #Cost Label
        self.drinksSakeCost = Label(self.drinksFrame, text = "£3.50", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksSakeCost.grid(row = 0, column = 3)
        
                #Image Open
        self.drinksSakeImage = Image.open("Sake.jpg")
        self.drinksSakeImage = ImageTk.PhotoImage(self.drinksSakeImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.drinksSakeLabel = Label(self.drinksFrame, image = self.drinksSakeImage)
        self.drinksSakeLabel.grid(row = 1, column = 2, columnspan = 2, padx = 5, pady = 5)

            #Water (0,2)

                #Name Radio Button
        self.drinksWaterRadioButton = Radiobutton(self.drinksFrame, text = "Water",
                                                  variable = self.drinksRadioButtonVar, value = "Water", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksWaterRadioButton.grid(row = 0, column = 4)

                #Cost Label
        self.drinksWaterCost = Label(self.drinksFrame, text = "£1.00", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksWaterCost.grid(row = 0, column = 5)

                #Image Open
        self.drinksWaterImage = Image.open("Water.jpg")
        self.drinksWaterImage = ImageTk.PhotoImage(self.drinksWaterImage.resize((78, 60), Image.ANTIALIAS))
        
                #Image Label
        self.drinksWaterLabel = Label(self.drinksFrame, image = self.drinksWaterImage)
        self.drinksWaterLabel.grid(row = 1, column = 4, columnspan = 2, padx = 5, pady = 5)

            #Ramune (2,0)

                #Name Radio Button
        self.drinksRamuneRadioButton = Radiobutton(self.drinksFrame, text = "Ramune",
                                                   variable = self.drinksRadioButtonVar, value = "Ramune", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksRamuneRadioButton.grid(row = 2, column = 0)

                #Cost Label
        self.drinksRamuneCost = Label(self.drinksFrame, text = "£2.25", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksRamuneCost.grid(row = 2, column = 1)

                #Image Open
        self.drinksRamuneImage = Image.open("Ramune.jpg")
        self.drinksRamuneImage = ImageTk.PhotoImage(self.drinksRamuneImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.drinksRamuneLabel = Label(self.drinksFrame, image = self.drinksRamuneImage)
        self.drinksRamuneLabel.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

            #Bubble Tea (2,1)

                #Name Radio Button
        self.drinksBubbleTeaRadioButton = Radiobutton(self.drinksFrame, text = "Bubble Tea",
                                                      variable = self.drinksRadioButtonVar, value = "Bubble Tea", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksBubbleTeaRadioButton.grid(row = 2, column = 2)

                #Cost Label
        self.drinksBubbleTeaCost = Label(self.drinksFrame, text = "£4.50", foreground = "#ffffff", background = "#211F34", font = ("Tahoma", 14))
        self.drinksBubbleTeaCost.grid(row = 2, column = 3)
        
                #Image Open
        self.drinksBubbleTeaImage = Image.open("Bubble Tea.jpg")
        self.drinksBubbleTeaImage = ImageTk.PhotoImage(self.drinksBubbleTeaImage.resize((78, 60), Image.ANTIALIAS))

                #Image Label
        self.drinksBubbleTeaLabel = Label(self.drinksFrame, image = self.drinksBubbleTeaImage)
        self.drinksBubbleTeaLabel.grid(row = 3, column = 2, columnspan = 2, padx = 5, pady = 5)

        #Submit Button 
        self.drinksAddButton = Button(self.drinksFrame, text = "Add", width = 5, font = ("Tahoma", 28), command = self.Drinks_AddToCart)
        self.drinksAddButton.grid(row = 2, rowspan = 2, column = 4, columnspan = 2, padx = 5, pady = 5)
        
    def Drinks_AddToCart(self):
        global cartItemD
        global cartItemDCost
        
        if self.drinksRadioButtonVar.get() == "Green Tea":
            cartItemD = "Green Tea"
            cartItemDCost = 1.50
            self.drinksScreen.destroy()

        elif self.drinksRadioButtonVar.get() == "Sake":
            cartItemD = "Sake"
            cartItemDCost = 3.50
            self.drinksScreen.destroy()

        elif self.drinksRadioButtonVar.get() == "Water":
            cartItemD = "Water"
            cartItemDCost = 1.00
            self.drinksScreen.destroy()

        elif self.drinksRadioButtonVar.get() == "Ramune":
            cartItemD = "Ramune"
            cartItemDCost = 2.25
            self.drinksScreen.destroy()

        elif self.drinksRadioButtonVar.get() ==  "Bubble Tea":
            cartItemD = "Bubble Tea"
            cartItemDCost = 4.50
            self.drinksScreen.destroy()

        else:
            print("failed")

Start()
