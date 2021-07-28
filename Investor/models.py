from django.db import models
from django import forms 

class User(models.Model):
    email = models.EmailField() 
    phone_no = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20) 
    last_name = models.CharField(max_length = 20)  
    
    def __str__(self):
        return self.email

CheckBox_CHOICES= [
    ('1', 'Yes'),
    ('2', 'No'),
]

class CheckBox(models.Model):
    Select = models.CharField(max_length=200,choices=CheckBox_CHOICES)
   


    def __str__(self):
        return self.Select 

class CheckBox2(models.Model):
   Select = models.CharField(max_length=200,choices=CheckBox_CHOICES)
   
   def __str__(self):
        return self.Select 

class CheckBox3(models.Model):
    Brief_Description = forms.CharField(max_length=100)
    


    def __str__(self):
        return self.Brief_Description

class VC_with_VCX(models.Model):  
    Name_of_VC  = models.CharField(max_length=20)
    Email_ID  = models.EmailField() 
    Your_Name   = models.CharField(max_length=20)
    Your_email   = models.EmailField() 
    Your_Designation  = models.CharField(max_length=20)
    Undertaking_that_the_person_is_actually_the_part_of_the_VC_and_will_be_granted_access_only_if_the_admin_will_accept_your_request  = models.BooleanField(default=True)
    
    def __str__(self): 
        return self.Name_of_VC

class VC_without_VCX(models.Model):  
    Name_of_your_firm = models.CharField(max_length=20)
    Location_of_your_firm  = models.CharField(max_length=20)
    GST_or_License_number   = models.IntegerField()
    Your_Name   = models.CharField(max_length=20)
    Your_email   = models.EmailField() 
    Your_Designation  = models.CharField(max_length=20)
    Upload_GST_certificate   = models.CharField(max_length=20)
    Brief_Description_of_VC   = models.TextField(max_length=20)
    Website_Link = models.CharField(max_length=20)
    
    
    def __str__(self): 
        return self.Name_of_your_firm 


class Dashboard1(models.Model):  
    #Name_of_Company = models.CharField(max_length=20)
    Amount_invested = models.IntegerField()
    Percentage_of_company  = models.IntegerField()
    Type_of_shares  = models.CharField(max_length=20)
    No_of_shares = models.IntegerField()
    Current_value = models.IntegerField()
    Profit_or_loss_on_investment = models.IntegerField()
    Amount_invested = models.IntegerField()
    
    def __str__(self): 
        return self.Name_of_Company 


class Monthly_Reports1(models.Model):  
    Name_of_Document = models.CharField(max_length=20)
    File_Type = models.CharField(max_length=20)
    Download_Link = models.URLField(max_length=200)
    
    def __str__(self): 
        return self.Name_of_Document

class Investment(models.Model):
    Name_of_Company =  models.CharField(max_length=20)
    Total_amount_to_invest  = models.IntegerField()
    Percentage_of_company  = models.IntegerField()
    Type_of_shares =  models.CharField(max_length=20)
    No_of_shares = models.IntegerField()
    Price_per_share  = models.IntegerField()
    Pre_money_valuation  = models.IntegerField()
    
    def __str__(self): 
        return self.Total_amount_to_invest

class Investor(models.Model):  
    Full_Name  = models.CharField(max_length=20)
    Date_of_birth  = models.IntegerField()
    Email_address = models.EmailField() 
    Contact_Number  = models.IntegerField()
    
    def __str__(self): 
        return self.Full_Name

class Account_Details(models.Model):  
    Account_Type  = models.CharField(max_length=20)
    Payment_Method   = models.CharField(max_length=20)
    Bank_Account_Number = models.IntegerField()
    IFSC_code  = models.IntegerField()
    
    def __str__(self): 
        return self.Account_Type

class Profile(models.Model): 
    profile_picture = models.ImageField(upload_to='profile_images/',blank=True)
    Full_Name  = models.CharField(max_length=20)
    Email_address = models.EmailField()
    change_password = models.IntegerField()
    
    def __str__(self): 
        return self.Image

class Company_Details(models.Model):  
    Name_of_your_Ventrue_Capital_firm  = models.CharField(max_length=20)
    Location_of_your_Firm   = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_images/',blank=True)
    GST_or_Licencse_Number = models.IntegerField()
    Your_website_Link  = models.URLField()
    Briefly_Describe_your_firms_Investments_and_expectations   = models.TextField(max_length=20)
    
    
    def __str__(self): 
        return self.Name_of_your_Ventrue_Capital_firm 


class Administator(models.Model): 
    Name  = models.CharField(max_length=20)
    Email = models.EmailField()
    Designation = models.CharField(max_length=20)
    
    def __str__(self): 
        return self.Name

class Employees(models.Model):
    Name  = models.CharField(max_length=20)
    Email = models.EmailField()
    Designation = models.CharField(max_length=20)
    
    def __str__(self): 
        return self.Name

class Subscription1(models.Model):
    Type  = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
    Description = models.TextField(max_length=100)
    
    def __str__(self): 
        return self.Type

CHOICES =( 
    ("1", "monthly"), 
    ("2", "Quarterly"), 
    ("3", "Annual"), 
    
) 

class bill(models.Model):
    Type_of_membership = models.CharField(max_length=20)
    Cost = models.CharField(max_length=20)
    Duration = models.CharField(max_length=1,choices = CHOICES) 
    
    def __str__(self): 
        return self.Type_of_membership

class Pay_now(models.Model):
    Name_on_Card = models.CharField(max_length=20)
    Credit_card_number = models.IntegerField()
    Exp_Month = models.CharField(max_length=20) 
    CVV = models.IntegerField()
    Exp_Year = models.IntegerField()
    
    def __str__(self): 
        return self.Name_on_Card 

class UPI(models.Model):
    Mobile_or_Payment_Address = models.IntegerField()
    
    def __str__(self): 
        return self.Mobile_or_Payment_Address

WALLETCHOICES =( 
    ("1", "PayTM"), 
    ("2", "BHIM Axis Pay"), 
    ("3", "PhonePe"),
    ("4", "Mobikwik"), 
    ("5", "Amazon Pay"),  
    
) 

class UPIwallet(models.Model):
    Choose_your_wallet = models.CharField(max_length=1,choices = WALLETCHOICES) 
    
    def __str__(self): 
        return self.Choose_your_wallet



    





    

    


