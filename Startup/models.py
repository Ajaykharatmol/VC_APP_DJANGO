from django.db import models

class Company(models.Model):
    Company_name = models.CharField(max_length = 200) 
    Company_location = models.CharField(max_length = 20)  
    Sector = models.IntegerField() 

    def __str__(self):
        return self.Company_name

class Live_Investors(models.Model):  
    Investor = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)
    Class_of_Share  = models.CharField(max_length=20)
    No_of_shares = models.IntegerField()
    Percentage = models.IntegerField()
    Price_per_Share = models.IntegerField()
    Investment = models.IntegerField()
    Total = models.IntegerField()

    def __str__(self): 
        return self.Investor

class Founder_Details(models.Model):  
    Number_of_founders = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    Role_in_startup  = models.CharField(max_length=20)
    Email_address = models.EmailField()
    Contact_no = models.IntegerField()
    LinkedIn_profile = models.EmailField()
    

    def __str__(self): 
        return self.Number_of_founders

class Startup_Details(models.Model):  
    Legal_Name_of_company = models.CharField(max_length=20)
    Startup_Name = models.CharField(max_length=20)
    Founding_month_and_year  = models.IntegerField()
    Location = models.CharField(max_length=20)
    Sector  = models.IntegerField()
    Stage = models.IntegerField()
    Upload_GST_certificate_or_License_for_verification = models.IntegerField()
    Product_Summary = models.TextField()
    Team_Summary = models.TextField()
    Why_are_you_better_than_your_competitors_or_What_differentiates_you = models.TextField()
    Upload_Pitch_deck = models.IntegerField()
    
    

    def __str__(self): 
        return self.Legal_Name_of_company


class Company_Financials(models.Model):  
    How_much_money_have_you_raised_till_date_in_Lakhs  = models.IntegerField()
    How_much_debt_does_your_company_have_in_Lakhs = models.IntegerField()
    Upload_company_financial_report_preferably_audited   = models.CharField(max_length=20)

    def __str__(self): 
        return self.How_much_money_have_you_raised_till_date_in_Lakhs

class Funding_Requirements (models.Model):  
    Minimum_Company_valuation = models.IntegerField()
    Minimum_Cost_per_share = models.IntegerField()
    Minimum_total_amount_for_investor_to_invest  = models.IntegerField()
    Other_requirements = models.CharField(max_length=20)
    
    def __str__(self): 
        return self.Minimum_Company_valuation


class Pending(models.Model):  
    Type_of_Investor  = models.CharField(max_length=20)
    Name_of_investor = models.CharField(max_length=20)
    Total_amount_bid  = models.IntegerField()
    Percentage  = models.IntegerField()
    No_of_shares = models.IntegerField()
    Price_per_share = models.IntegerField()
    money_valuation = models.IntegerField()
    

    def __str__(self): 
        return self.Type_of_Investor

class Company_Bids(models.Model):  
    Total_amount_invested  = models.IntegerField()
    Percentage_of_company  = models.IntegerField()
    No_of_shares = models.IntegerField()
    Price_per_share = models.IntegerField()
    pre_or_post_money_valuation = models.IntegerField()
    

    def __str__(self): 
        return self.Total_amount_invested

 
class Investor_Details (models.Model):  
    Full_Name  = models.CharField(max_length=20)
    Date_of_birth  = models.IntegerField()
    Email_address = models.EmailField()
    Contact_Number = models.IntegerField()
    
    def __str__(self): 
        return self.Full_Name

class Profile(models.Model):  
    profile_picture = models.ImageField(upload_to='profile_images/',blank=True)
    Full_Name  = models.CharField(max_length=20)
    Email_address = models.EmailField()
    change_password = models.IntegerField()
    
    def __str__(self): 
        return self.Full_Name


class Startup_Details1(models.Model):
    Legal_Name_of_company = models.CharField(max_length=20)
    Startup_Name = models.CharField(max_length=20)
    Founding_month_and_year  = models.IntegerField()
    Location = models.CharField(max_length=20)
    Sector  = models.IntegerField()
    GST_or_License_Number = models.IntegerField()
    Website_Link  = models.CharField(max_length=20)
    Startup_description = models.TextField()
    
    def __str__(self): 
        return self.Legal_Name_of_company

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

