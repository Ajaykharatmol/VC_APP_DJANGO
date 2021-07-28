from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Startup.models import Company,Live_Investors,Founder_Details,Startup_Details,Company_Financials,Funding_Requirements,Pending,Company_Bids,Investor_Details,Startup_Details1,Profile,bill,Pay_now,UPI,UPIwallet
 
  
  
class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() 
    phone_no = forms.CharField(max_length = 20) 
    first_name = forms.CharField(max_length = 20) 
    last_name = forms.CharField(max_length = 20) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class CompanyForm(forms.ModelForm): 
     class Meta: 
        model = Company 
        fields = ('Company_name','Company_location','Sector')

        widgets = {
            'Company_name' : forms.TextInput(attrs={'class':'form-control'}),
            'Company_location' : forms.TextInput(attrs={'class':'form-control'}),
            'Sector' : forms.NumberInput(attrs={'class':'form-control'}),
            

        }    

class Live_InvestorsForm(forms.ModelForm):  
    class Meta:  
        model = Live_Investors 
        fields = "__all__" 

class Founder_DetailsForm(forms.ModelForm):  
    class Meta:  
        model = Founder_Details 
        fields = ('Number_of_founders','Name','Role_in_startup','Email_address','Contact_no','LinkedIn_profile')        
        widgets = {
            'Number_of_founders' : forms.TextInput(attrs={'class':'form-control'}),
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Role_in_startup' : forms.TextInput(attrs={'class':'form-control'}),
            'Email_address' : forms.EmailInput(attrs={'class':'form-control'}),
            'Contact_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'LinkedIn_profile' : forms.EmailInput(attrs={'class':'form-control'}),
            
        }   
         

class Startup_DetailsForm(forms.ModelForm):  
    class Meta:  
        model = Startup_Details
        fields = ('Legal_Name_of_company','Startup_Name','Founding_month_and_year','Location','Sector','Stage','Upload_GST_certificate_or_License_for_verification','Product_Summary','Team_Summary','Why_are_you_better_than_your_competitors_or_What_differentiates_you','Upload_Pitch_deck')
        
        widgets = {
            'Legal_Name_of_company' : forms.TextInput(attrs={'class':'form-control'}),
            'Startup_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Founding_month_and_year' : forms.NumberInput(attrs={'class':'form-control'}),
            'Location' : forms.TextInput(attrs={'class':'form-control'}),
            'Sector' : forms.NumberInput(attrs={'class':'form-control'}),
            'Stage' : forms.NumberInput(attrs={'class':'form-control'}),
            'Upload_GST_certificate_or_License_for_verification' : forms.NumberInput(attrs={'class':'form-control'}),
            'Product_Summary' : forms.Textarea(attrs={'class':'form-control'}),
            'Team_Summary' : forms.Textarea(attrs={'class':'form-control'}),
            'Why_are_you_better_than_your_competitors_or_What_differentiates_you' : forms.Textarea(attrs={'class':'form-control'}),
            'Upload_Pitch_deck' : forms.NumberInput(attrs={'class':'form-control'})


        }    
         

class Company_FinancialsForm(forms.ModelForm):  
    class Meta:  
        model = Company_Financials
        fields = ('How_much_money_have_you_raised_till_date_in_Lakhs','How_much_debt_does_your_company_have_in_Lakhs','Upload_company_financial_report_preferably_audited')
        
        widgets = {
            'How_much_money_have_you_raised_till_date_in_Lakhs' : forms.NumberInput(attrs={'class':'form-control'}),
            'How_much_debt_does_your_company_have_in_Lakhs' : forms.NumberInput(attrs={'class':'form-control'}),
            'Upload_company_financial_report_preferably_audited' : forms.TextInput(attrs={'class':'form-control'}),
            
        }   
        

class Funding_RequirementsForm(forms.ModelForm):  
    class Meta:  
        model = Funding_Requirements
        fields = ('Minimum_Company_valuation','Minimum_Cost_per_share','Minimum_total_amount_for_investor_to_invest','Other_requirements')
        
        widgets = {
            'Minimum_Company_valuation' : forms.NumberInput(attrs={'class':'form-control'}),
            'Minimum_Cost_per_share' : forms.NumberInput(attrs={'class':'form-control'}),
            'Minimum_total_amount_for_investor_to_invest' : forms.NumberInput(attrs={'class':'form-control'}),
            'Other_requirements' : forms.TextInput(attrs={'class':'form-control'}),
            }    
        

class PendingForm(forms.ModelForm):  
    class Meta:  
        model = Pending
        fields = "__all__" 

class BidsForm(forms.ModelForm):  
    class Meta:  
        model = Company_Bids 
        fields = ('Total_amount_invested','Percentage_of_company','No_of_shares','Price_per_share','pre_or_post_money_valuation')

        widgets = {
            'Total_amount_invested' : forms.NumberInput(attrs={'class':'form-control'}),
            'Percentage_of_company' : forms.NumberInput(attrs={'class':'form-control'}),
            'No_of_shares' : forms.NumberInput(attrs={'class':'form-control'}),
            'Price_per_share' : forms.NumberInput(attrs={'class':'form-control'}),
            'pre_or_post_money_valuation' : forms.NumberInput(attrs={'class':'form-control'})

        }    

class Investor_DetailsForm(forms.ModelForm):  
    class Meta:  
        model = Investor_Details
        fields = ('Full_Name','Date_of_birth','Email_address','Contact_Number')

        widgets = {
            'Full_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Date_of_birth' : forms.NumberInput(attrs={'class':'form-control'}),
            'Email_address' : forms.EmailInput(attrs={'class':'form-control'}),
            'Contact_Number' : forms.NumberInput(attrs={'class':'form-control'})

        }    


#  
class ProfileForm(forms.ModelForm):  
    class Meta:  
        model = Profile 
        fields = ('profile_picture','Full_Name','Email_address','change_password')

        widgets = {
            'profile_picture' : forms.FileInput(attrs={'class':'form-control'}),
            'Full_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Email_address' : forms.EmailInput(attrs={'class':'form-control'}),
            'change_password' : forms.NumberInput(attrs={'class':'form-control'})

        }    

class Startup_Details1Form(forms.ModelForm):  
    class Meta:  
        model = Startup_Details1
 
        fields = ('Legal_Name_of_company','Startup_Name','Founding_month_and_year','Location','Sector','GST_or_License_Number','Website_Link','Startup_description')
        
        widgets = {
            'Legal_Name_of_company' : forms.TextInput(attrs={'class':'form-control'}),
            'Startup_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Founding_month_and_year' : forms.NumberInput(attrs={'class':'form-control'}),
            'Location' : forms.TextInput(attrs={'class':'form-control'}),
            'Sector' : forms.NumberInput(attrs={'class':'form-control'}),
            'GST_or_License_Number' : forms.NumberInput(attrs={'class':'form-control'}),
            'Website_Link' : forms.TextInput(attrs={'class':'form-control'}),
            'Startup_description' : forms.Textarea(attrs={'class':'form-control'})

        }   
# #


class billing_detailsForm(forms.ModelForm):  
    class Meta:  
        model = bill 
        fields = ('Type_of_membership','Cost','Duration')

        widgets = {
            'Type_of_membership' : forms.TextInput(attrs={'class':'form-control'}),
            'Cost' : forms.TextInput(attrs={'class':'form-control'}),
            'Duration' : forms.Select(attrs={'class':'form-control'})
            }

class Pay_nowForm(forms.ModelForm):  
    class Meta:  
        model = Pay_now 
        fields = ('Name_on_Card','Credit_card_number','Exp_Month','CVV','Exp_Year')

        widgets = {
            'Name_on_Card' : forms.TextInput(attrs={'class':'form-control'}),
            'Credit_card_number' : forms.NumberInput(attrs={'class':'form-control'}),
            'Exp_Month' : forms.TextInput(attrs={'class':'form-control'}),
            'CVV' : forms.NumberInput(attrs={'class':'form-control'}),
            'Exp_Year' : forms.NumberInput(attrs={'class':'form-control'})
            } 

class UPIForm(forms.ModelForm):  
    class Meta:  
        model = UPI 
        fields = ('Mobile_or_Payment_Address',)

        widgets = {
        
            'Mobile_or_Payment_Address' : forms.NumberInput(attrs={'class':'form-control'})
            }

class UPIwalletForm(forms.ModelForm):  
    class Meta:  
        model = UPIwallet 
        fields = ('Choose_your_wallet',)

        widgets = {
            
            'Choose_your_wallet' : forms.Select(attrs={'class':'form-control'}),
            }  
