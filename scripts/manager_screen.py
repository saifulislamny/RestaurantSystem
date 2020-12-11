''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen
from manager_operations import accept_customer_registrations, decline_customer_registrations, view_customer_registrations, view_account_deregistrations,view_customer_complaints_by_customers, view_chef_complaints_and_compliments, view_delivery_complaints_and_compliments, raise_employee_pay, cut_employee_pay, delete_account_as_manager, delete_account_as_manager, give_warning, view_taboo_words


def main() :
   root = tk.Tk()
   app = ManagerScreen(root,"BrotherChicken")

#class to show what appears on the main screen of "Manager"
class ManagerScreen:
    def __init__(self,master,user):
        self.root=master
        self.user=user
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        titleLabel = tk.Label(frame, text="Manager", bg='white', font=('Times New Roman', 30))
        titleLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        privilegesFrame = tk.Frame(frame, bg='#cccccc')
        privilegesFrame.place(relx=0.05, rely=0.25, relwidth=0.3, relheight=0.7)

        privilegesLabel = tk.Label(privilegesFrame, text="Manager Privileges", bg="white", font=('Times New Roman', 12, 'bold'))
        privilegesLabel.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor="center")

        reviewButton = tk.Button(privilegesFrame, text="Check\nComplaints/Compliments", bg="white", font=('Times New Roman', 12), command=self.check_reviews_window)
        reviewButton.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)

        registerButton = tk.Button(privilegesFrame, text="View Registrations", bg="white", font=('Times New Roman', 12), command=self.register_surfer_window)
        registerButton.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.1)

        manageCustButton = tk.Button(privilegesFrame, text="Manage Customers", bg="white", font=('Times New Roman', 12), command=self.manage_cust_window)
        manageCustButton.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)

        manageStaffButton = tk.Button(privilegesFrame, text="Manage Staffs", bg="white", font=('Times New Roman', 12), command=self.manage_staff_window)
        manageStaffButton.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)

        tabooListFrame = tk.Frame(frame, bg='#cccccc')
        tabooListFrame.place(relx=0.4, rely=0.25, relwidth=0.3, relheight=0.1)

        tabooListButton = tk.Button(tabooListFrame, text="View Taboo List", bg="white", font=('Times New Roman', 14), command=self.taboo_list_window)
        tabooListButton.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.7)


        self.root.mainloop()

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
# function to open check reviews window
    def check_reviews_window(self):
        self.app = CheckReviewsWindow(self.root,self.user)
# function to open register surfer window
    def register_surfer_window(self):
        self.app = RegisterSurferWindow(self.root,self.user)
# function to open manage customer window
    def manage_cust_window(self):
        self.app = ManageCustWindow(self.root,self.user)
# function to open manage staff window
    def manage_staff_window(self):
        self.app = ManageStaffWindow(self.root,self.user)
# function to open taboo list window
    def taboo_list_window(self):
        self.app = TabooListWindow(self.root,self.user)
     
# function to accept customer 
    def accept_cust_window (self):
        self.app = AcceptCustWindow(self.root,self.user)
# function to decline customer
    def decline_cust_window(self):
        self.app = DeclineCustWindow (self.root, self.user)
# function to view customer registered 
    def view_cust_Registration_window(self):
        self.app = ViewCustRegistrations(self.root, self.user)

    def view_cust_Deregistration_window(self):
        self.app = ViewCustDeregistrations(self.root, self.user)

    def custCompaincustWindow(self):
        self.app = CustComplainCust(self.root, self.user)
    
    def chefComplainComplimentWindow(self):
        self.app = CustComplainCust(self.root, self.user)

    def deliveryComplainComplimentWindow(self):
        self.app = DeliveryComplainCompliment(self.root, self.user)

                

#class to show what appears after "Check Complaints/Compliments" button pressed
class CheckReviewsWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()
        self.root.geometry("700x700")

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        checkReviewsLabel = tk.Label(frame, text="Compliments/Complaints", font=('Times New Roman', 16), bg="#e6e6e6")
        checkReviewsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
        custTocustComplain = tk.Button(frame, text="Customer Complain on Customer", bg="#b2bff7", font=('Times New Roman', 12),  borderwidth=2, command= self.custCompaincustWindow) 
        custTocustComplain.place (relx = 0.25, rely = .25, relwidth=0.5, relheight=0.1)

        chefComplimentComplaint = tk.Button (frame, text="Chef Complain and Compliment", bg="#b2bff7", font=('Times New Roman', 12),  borderwidth=2, command= self.chefComplainComplimentWindow)
        chefComplimentComplaint.place (relx = 0.25, rely =.35, relwidth=0.5, relheight=0.1)
        
        deliveryComplimentComplaint = tk.Button (frame, text="Delivery Complain and Compliment", bg="#b2bff7", font=('Times New Roman', 12),  borderwidth=2, command =self.deliveryComplainComplimentWindow  )
        deliveryComplimentComplaint.place(relx = 0.25, rely = .45, relwidth=0.5, relheight=0.1)
      
      
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
      
    def custCompaincustWindow(self):
        self.app = CustComplainCust(self.root, self.user)

    def chefComplainComplimentWindow(self):
        self.app = ChefComplainCompliment(self.root, self.user)

    def deliveryComplainComplimentWindow(self):
        self.app = DeliveryComplainCompliment(self.root, self.user)
         
         
class CustComplainCust:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")
        
        custComplinLabel = tk.Label (frame, text="Customer Complaints", bg='#e6e6e6', font=('Times New Roman', 18), borderwidth=2)
        custComplinLabel.place(relx = .3, rely = .1)

        custComplainString = tk. Label (frame, text = str(view_customer_complaints_by_customers()),  font=('Times New Roman', 12), bg="#e6e6e6")
        custComplainString.place (relx =0.2, rely= 0.25) 
         
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
         
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)


class ChefComplainCompliment:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        cheffComplainComplimentLabel = tk.Label(frame, text = "Cheff Complaints and Compliment", bg ='#e6e6e6',font=('Times New Roman', 18), borderwidth=2)
        cheffComplainComplimentLabel.place(relx = .2, rely = .1)

        cheffComplainComplimentString = tk. Label (frame, text = str(view_chef_complaints_and_compliments()), font=('Times New Roman', 12), bg="#e6e6e6") 
        cheffComplainComplimentString.place(relx = 0.0 , rely = 0.25)
      
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
   
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)


class DeliveryComplainCompliment:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        deliveryComplainComplimentLabel = tk.Label(frame, text = "Delivery Complaints and Compliment", bg ='#e6e6e6',font=('Times New Roman', 18), borderwidth=2)
        deliveryComplainComplimentLabel.place(relx = .2, rely = .1)

        deliveryComplainComplimentString = tk. Label (frame, text = str(view_delivery_complaints_and_compliments()), font=('Times New Roman', 12), bg="#e6e6e6") 
        deliveryComplainComplimentString.place(relx = 0.0 , rely = 0.25)
      
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
        
      
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)


class RegisterSurferWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        registerSurferLabel = tk.Label(frame, text="Registrations", font=('Times New Roman', 19), bg="#e6e6e6")
        registerSurferLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)
        
        
        acceptCustomerRegistrations = tk.Button(frame, text="Accept Customer Registration", bg='#999999', font=('Times New Roman', 12), borderwidth=2, command= self.accept_cust_window )
        acceptCustomerRegistrations.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.05)

        declineCustomerRegistrations = tk.Button(frame, text="Decline Customer Registration", bg='#999999', font=('Times New Roman', 12), borderwidth=2, command = self.decline_cust_window)
        declineCustomerRegistrations.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.05)

        viewCustomerRegistrations = tk.Button(frame, text="View Customer Registration", bg='#999999', font=('Times New Roman', 12), borderwidth=2, command = self.view_cust_Registration_window)
        viewCustomerRegistrations.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.05)

        viewAccountDeregistrations = tk.Button(frame, text="View Customer Deregistration", bg='#999999', font=('Times New Roman', 12), borderwidth=2, command = self.view_cust_Deregistration_window)
        viewAccountDeregistrations.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
         
         
    def accept_cust_window (self):
        self.app = AcceptCustWindow(self.root,self.user)

    def decline_cust_window(self):
        self.app = DeclineCustWindow (self.root, self.user)

    def view_cust_Registration_window(self):
        self.app = ViewCustRegistrations(self.root, self.user)
    
    def view_cust_Deregistration_window(self):
        self.app = ViewCustDeregistrations(self.root, self.user)
         
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
      
   

#class to show what appears after "Manage Customers" button pressed
class ManageCustWindow:
    def closeCustaccount(self, username, frame):
        if delete_account_as_manager(self.user) == True:
            closesuccess = tk.Label(frame, text="Successful", font=('Times New Roman', 16), bg="#e6e6e6")
            closesuccess.place(relx=0.3, rely=0.7)
        else:
            closeunsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            closeunsuccessful.place(relx=0.3, rely=0.7)

    def warningCheck(self, username, frame):
        if give_warning(self.user) == True:
            warningSucess = tk.Label(frame, text="Successfully given warning", font=('Times New Roman', 16), bg="#e6e6e6")
            warningSucess.place(relx=0.3, rely=0.7)
        else:
            warningunsuccessful = tk.Label(frame, text="Unsuccessful to give warning", font=('Times New Roman', 16), bg="#e6e6e6")
            warningunsuccessful.place(relx=0.3, rely=0.7)
   
   
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        manageCustLabel = tk.Label(frame, text="Manage Customer", font=('Times New Roman', 14), bg="#e6e6e6")
        manageCustLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.07)
        
        customerName = tk.Label(frame, text="Enter Customer Name", font=('Times New Roman', 11), bg="#e6e6e6")
        customerName.place(relx=0.1, rely=0.2)
        EntercustomerName = tk.Entry (frame, font = 20)
        EntercustomerName.place (relx=0.1, rely=0.25, relwidth=0.45, relheight=0.05 )

        getCustomerNameButton = tk.Button(frame, text="Close Account", bg='#999999', font=('Times New Roman', 10), borderwidth=2, command = lambda:self.closeCustaccount(EntercustomerName.get(),frame))
        getCustomerNameButton.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.05)

        checkWarningButton= tk.Button (frame, text= "Give Warning",bg='#999999', font=('Times New Roman', 10), borderwidth=2, command= lambda:self.warningCheck(EntercustomerName.get(),frame) )
        checkWarningButton.place (relx =0.1, rely =.5, relwidth=0.3, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
         
      
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
        # TODO: Dante, fulfill this window by using close_customer_accounts() from manager_operations.py (if it's already implemented)
         
         
#class to show what appears after "Manage Staffs" button pressed
class ManageStaffWindow:
    def payDecrease(self, username, decrement,frame):
        if cut_employee_pay(self.user,decrement) == True:
            cutsuccess = tk.Label(frame, text="Successful", font=('Times New Roman', 16), bg="#e6e6e6")
            cutsuccess.place(relx=0.3, rely=0.7)
        else:
            cutunsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            cutunsuccessful.place(relx=0.3, rely=0.7)

    def payRaise(self, username, increment,frame):
        if raise_employee_pay(self.user,increment) == True:
            raisesuccess = tk.Label(frame, text="Successful", font=('Times New Roman', 16), bg="#e6e6e6")
            raisesuccess.place(relx=0.3, rely=0.7)
        else:
            raiseunsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            raiseunsuccessful.place(relx=0.3, rely=0.7)

    def closeAccount(self, username, frame):
        if delete_account_as_manager(self.user) == True:
            closeSuccess = tk.Label(frame, text="Successful Deleted", font=('Times New Roman', 16), bg="#e6e6e6")
            closeSuccess.place(relx=0.3, rely=0.7)
        else:
            closeunsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            closeunsuccessful.place(relx=0.3, rely=0.7)

    def giveWarning(self,username,frame):
        if give_warning(self.user) == True:
            givewarningSuccess=  tk.Label(frame, text="Successful warning given", font=('Times New Roman', 16), bg="#e6e6e6")
            givewarningSuccess.place(relx=0.3, rely=0.7)
        else:
            givewarningunsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            givewarningunsuccessful.place(relx=0.3, rely=0.7)
   
      
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        manageStaffLabel = tk.Label(frame, text="You chose to manage staffs!", font=('Times New Roman', 14), bg="#e6e6e6")
        manageStaffLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)
        
        staffName = tk.Label(frame, text="Enter Staff Name", font=('Times New Roman', 11), bg="#e6e6e6")
        staffName.place(relx=0.1, rely=0.2)
        enterStaffName = tk.Entry (frame, font = 20)
        enterStaffName.place (relx=0.1, rely=0.25, relwidth=0.45, relheight=0.05 )
      
        staffPayCut = tk.Label(frame, text="Enter Amount to Cut Pay", font=('Times New Roman', 11), bg="#e6e6e6")
        staffPayCut.place(relx=0.1, rely=0.4)
        enterPayCut = tk.Entry (frame, font = 20)
        enterPayCut.place (relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05 )

        cutPayButton = tk.Button(frame, text="Cut Pay", bg='#999999', font=('Times New Roman', 10), borderwidth=2, command = lambda: self.payDecrease(enterStaffName.get(),enterPayCut.get(),frame) )
        cutPayButton.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05)
        dollarSign = tk.Label (frame, text = '$', font= ('Times New Roman', 12 ), bg="#e6e6e6")
        dollarSign.place(relx=0.0, rely= .45, relwidth=0.1, relheight=0.05 )

        staffPayRaiseField = tk.Label(frame, text="Enter Amount to Raise Pay", font=('Times New Roman', 11), bg="#e6e6e6")
        staffPayRaiseField.place(relx=0.1, rely=0.55)
        enterPayRaiseField = tk.Entry (frame, font = 10)
        enterPayRaiseField.place (relx=0.1, rely=0.6, relwidth=0.3, relheight=0.05 )

        raisePayButton = tk.Button(frame, text="Raise Pay", bg='#999999', font=('Times New Roman', 10), borderwidth=2, command=lambda: self.payRaise( enterStaffName.get(),enterPayRaiseField.get(), frame))
        raisePayButton.place(relx=0.5, rely=0.6, relwidth=0.1, relheight=0.05)
        dollarSign = tk.Label (frame, text = '$', font= ('Times New Roman', 12 ), bg="#e6e6e6")
        dollarSign.place(relx=0.0, rely=.6, relwidth=0.1, relheight=0.05 )

        closeStaffAccountButton= tk.Button(frame, text = "Close Staff Account" ,bg='#999999',font=('Times New Roman', 13), command = lambda:self.closeAccount(enterStaffName.get(),frame))
        closeStaffAccountButton.place(relx=0.5, rely=0.8, relwidth=0.35, relheight=0.05)

        givewarningButton = tk.Button(frame, text = "Give Warning", bg='#999999',font=('Times New Roman', 13), command = lambda:self.giveWarning (enterStaffName.get(),frame ) )
        givewarningButton.place(relx=0.1, rely=0.8, relwidth=0.25, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
         
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

         
         
  #class to show what appears after "View Taboo List" button pressed
class TabooListWindow:
    def __init__(self, master,user):
        self.root = master
        self.user=user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        tabooListLabel = tk.Label(frame, text="Taboo List", font=('Times New Roman', 14), bg="#e6e6e6")
        tabooListLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
        tabooframe = tk.Frame(frame, bg="#ffb993", text = str (view_taboo_words()) )
        tabooframe.place(relx = 0.15, rely =0.2, relwidth = 0.65, relheight = .6 )
      
      
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
      
      
class AcceptCustWindow:
    def CheckCustomer(self, username, frame):
        if accept_customer_registrations(self.user) == True:
            success = tk.Label(frame, text="Successful", font=('Times New Roman', 12), bg="#e6e6e6")
            success.place(relx=0.3, rely=0.4)
        else:
            unsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 12), bg="#e6e6e6")
            unsuccessful.place(relx=0.3, rely=0.4)

    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()
        self.root.geometry("700x700")

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        acceptCustLabel = tk.Label(frame, text="Accept Customer", font=('Times New Roman', 20), bg="#e6e6e6")
        acceptCustLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        customerName = tk.Label(frame, text="Enter Customer Name", font=('Times New Roman', 11), bg="#e6e6e6")
        customerName.place(relx=0.1, rely=0.2)

        entercustomerName = tk.Entry (frame, font = 20)
        entercustomerName.place (relx=0.1, rely=0.25, relwidth=0.45, relheight=0.05 )
        entercustomerName.focus_set()

        tapButton = tk.Button(frame, text="Enter",borderwidth=2, command = lambda: self.CheckCustomer(entercustomerName.get() ,frame),  bg='#999999', font=('Times New Roman', 10) )
        tapButton.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.05)


        isCustRegistered = tk.Label(frame, text="Is Customer Registered ?", font=('Times New Roman', 11), bg="#e6e6e6")
        isCustRegistered.place(relx=0.1, rely=0.35)
        isCustRegistered = tk.Frame (frame, bg='#d6e5f2')
        isCustRegistered.place(relx=0.3, rely=0.4, relwidth=0.25, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)
      
      
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
        
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)
    

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
         
class DeclineCustWindow:
    def removeCust(self, username, frame):
        if decline_customer_registrations(username) == True:
            thissuccess = tk.Label(frame, text="Successful", font=('Times New Roman', 12), bg="#e6e6e6")
            thissuccess.place(relx=0.3, rely=0.4)
        else:
            thisunsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 12), bg="#e6e6e6")
            thisunsuccessful.place(relx=0.3, rely=0.4)


    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()
        self.root.geometry("700x700")

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        declineCustLabel = tk.Label(frame, text=self.user, font=('Times New Roman', 20), bg="#e6e6e6")
        declineCustLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        customerName = tk.Label(frame, text="Enter Customer Name", font=('Times New Roman', 11), bg="#e6e6e6")
        customerName.place(relx=0.1, rely=0.2)

        customerNameEntry = tk.Entry (frame, font = 20)
        customerNameEntry.place (relx=0.1, rely=0.25, relwidth=0.45, relheight=0.05 )

        enterButton = tk.Button(frame, text="Enter", bg='#999999', font=('Times New Roman', 10), borderwidth=2)
        enterButton.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.05)

        deleteButton = tk.Button(frame, text =" Delete", bg='#999999', font=('Times New Roman', 10), borderwidth=2, command = lambda: self.removeCust(customerNameEntry.get() ,frame))
        deleteButton.place(relx=0.25, rely=0.45, relwidth=0.2, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)
         
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
        
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)
   
    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
         
         
class ViewCustRegistrations:

    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()
        self.root.geometry("700x700")

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        viewRegistration = tk.Label (frame, text = "View Customer Registration",font=('Times New Roman', 18),  bg="#e6e6e6")
        viewRegistration.place(relx=.20, rely=.05, relwidth=0.5, relheight=0.05)

        username = tk.Label (frame, text = "Username", font=('Times New Roman', 10), bg="#e6e6e6")
        username.place(relx=0.1, rely=0.20, relwidth=0.3, relheight=0.05)

        depositInfo= tk.Label (frame, text = "Deposit Information", font=('Times New Roman', 10), bg="#e6e6e6") 
        depositInfo.place(relx=0.3, rely=0.20, relwidth=0.4, relheight=0.05)

        usernamelist = tk.Frame (frame, bg='#e6e6e6', )
        usernamelist.place(relx=0.17, rely=0.25, relwidth=0.25, relheight=0.5)

        depositList = tk.Frame (frame, bg='#e6e6e6')
        depositList.place(relx=0.58, rely=0.25, relwidth=0.25, relheight=0.5)

        custReg_label = tk.Label (frame,  text = str(view_customer_registrations()) , font=('Times New Roman', 12), bg="#e6e6e6")
        custReg_label.place(relx =0.2, rely= 0.3)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)
      
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
        
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)
    
    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)         

         
class ViewCustDeregistrations:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()
        self.root.geometry("700x700")

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        viewDeregistration = tk.Label (frame, text = "View Customer Deregistration",font=('Times New Roman', 16),  bg="#e6e6e6")
        viewDeregistration.place(relx=.20, rely=.05, relwidth=0.5, relheight=0.05)

        usernameEnter = tk.Label (frame, text = "Username", font=('Times New Roman', 12), bg="#e6e6e6")
        usernameEnter.place(relx=0.1, rely=0.20, relwidth=0.25, relheight=0.05)

        ReasontoLeave = tk.Label (frame, text = "Reason To Leave", font=('Times New Roman', 12), bg="#e6e6e6")
        ReasontoLeave.place(relx=0.30, rely=0.20, relwidth=0.3, relheight=0.05)

        usernameCount = tk.Frame (frame, bg='#e6e6e6')
        usernameCount.place(relx=0.17, rely=0.25, relwidth=0.25, relheight=0.5)

        ReasonLeft = tk.Frame (frame, bg='#e6e6e6')
        ReasonLeft.place(relx=0.58, rely=0.25, relwidth=0.25, relheight=0.5)

        custdeReg_label = tk.Label (frame,  text = str(view_account_deregistrations()) , font=('Times New Roman', 12), bg="#e6e6e6")
        custdeReg_label.place(relx =0.2, rely= 0.3)
      
      
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
      
      
        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)
       
    
    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)  
      
        
    # function to return to home screen
    def home_window(self):
        self.app = ManagerScreen(self.root,self.user)
      

      
# you can run the Manager screen by running $ python3 manager_screen.py

main()
