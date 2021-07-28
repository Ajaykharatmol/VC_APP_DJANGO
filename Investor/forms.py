from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from Investor.models import Dashboard1,Investment,Investor,Account_Details,Company_Details,Profile,bill,Pay_now,UPI,UPIwallet,VC_with_VCX,VC_without_VCX, CheckBox,CheckBox2,CheckBox3
from django import forms 
  
  
class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() 
    phone_no = forms.CharField(max_length = 20) 
    first_name = forms.CharField(max_length = 20) 
    last_name = forms.CharField(max_length = 20) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

CheckBox_CHOICES= [
    ('1', 'Yes'),
    ('2', 'No'),
]
class CheckBox(forms.Form):
    Select = forms.CharField(max_length=1,widget=forms.RadioSelect(choices=CheckBox_CHOICES))
    Brief_Description_of_your_investments = forms.CharField(max_length=200)

class CheckBox1(forms.Form):
    Select1 = forms.CharField(widget=forms.RadioSelect(choices=CheckBox_CHOICES))
    
class CheckBox4(forms.Form):
    Select = forms.CharField(widget=forms.RadioSelect(choices=CheckBox_CHOICES)) 

class VC_with_VCXForm(forms.ModelForm):  
    class Meta:  
        model = VC_with_VCX 
    
        fields = ('Name_of_VC','Email_ID','Your_Name','Your_email','Your_Designation','Undertaking_that_the_person_is_actually_the_part_of_the_VC_and_will_be_granted_access_only_if_the_admin_will_accept_your_request')

        widgets = {
            'Name_of_VC' : forms.TextInput(attrs={'class':'form-control'}),
            'Email_ID' : forms.EmailInput(attrs={'class':'form-control'}),
            'Your_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Your_email' : forms.EmailInput(attrs={'class':'form-control'}),
            'Your_Designation' : forms.TextInput(attrs={'class':'form-control'}),
            #'Undertaking_that_the_person_is_actually_the_part_of_the_VC_and_will_be_granted_access_only_if_the_admin_will_accept_your_request' : forms.BooleanInput(attrs={'class':'form-control'})

        }       

        #Undertaking_that_the_person_is_actually_the_part_of_the_VC_and_will_be_granted_access_only_if_the_admin_will_accept_your_request = forms.BooleanField() 
    
class VC_without_VCXForm(forms.ModelForm):  
    class Meta:  
        model =  VC_without_VCX  
        
        fields = ('Name_of_your_firm','Location_of_your_firm','GST_or_License_number','Your_Name','Your_email','Your_Designation','Upload_GST_certificate','Brief_Description_of_VC','Website_Link')

        widgets = {
            'Name_of_your_firm' : forms.TextInput(attrs={'class':'form-control'}),
            'Location_of_your_firm' : forms.TextInput(attrs={'class':'form-control'}),
            'GST_or_License_number' : forms.NumberInput(attrs={'class':'form-control'}),
            'Your_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Your_email' : forms.EmailInput(attrs={'class':'form-control'}),
            'Your_Designation' : forms.TextInput(attrs={'class':'form-control'}),
            'Upload_GST_certificate' : forms.TextInput(attrs={'class':'form-control'}),
            'Brief_Description_of_VC' : forms.Textarea(attrs={'class':'form-control'}),
            'Website_Link' : forms.TextInput(attrs={'class':'form-control'})
            

        }       

class Form(forms.ModelForm):  
    class Meta:  
        model = Dashboard1  
        fields = "__all__" 

class InvestmentForm(forms.ModelForm):  
    class Meta:  
        model = Investment  
        
        fields = ('Name_of_Company','Total_amount_to_invest','Percentage_of_company','Type_of_shares','No_of_shares','Price_per_share','Pre_money_valuation')
        
        widgets = {
            'Name_of_Company' : forms.TextInput(attrs={'class':'form-control'}),
            'Total_amount_to_invest' : forms.NumberInput(attrs={'class':'form-control'}),
            'Percentage_of_company' : forms.NumberInput(attrs={'class':'form-control'}),
            'Type_of_shares' : forms.TextInput(attrs={'class':'form-control'}),
            'No_of_shares' : forms.NumberInput(attrs={'class':'form-control'}),
            'Price_per_share' : forms.NumberInput(attrs={'class':'form-control'}),
            'Pre_money_valuation' : forms.NumberInput(attrs={'class':'form-control'})
            
        }      


class InvestorForm(forms.ModelForm):  
    class Meta:  
        model = Investor 
        
        fields = ('Full_Name','Date_of_birth','Email_address','Contact_Number')
        
        widgets = {
            'Full_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Date_of_birth' : forms.NumberInput(attrs={'class':'form-control'}),
            'Email_address' : forms.EmailInput(attrs={'class':'form-control'}),
            'Contact_Number' : forms.NumberInput(attrs={'class':'form-control'}),
            
        }      

class Account_DetailsForm(forms.ModelForm):  
    class Meta:  
        model = Account_Details 
        
        fields = ('Account_Type','Payment_Method','Bank_Account_Number','IFSC_code')
        
        widgets = {
            'Account_Type' : forms.TextInput(attrs={'class':'form-control'}),
            'Payment_Method' : forms.TextInput(attrs={'class':'form-control'}),
            'Bank_Account_Number' : forms.NumberInput(attrs={'class':'form-control'}),
            'IFSC_code' : forms.NumberInput(attrs={'class':'form-control'}),
            
        }      

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

class Company_DetailsForm(forms.ModelForm):  
    class Meta:  
        model = Company_Details 
        fields = ('Name_of_your_Ventrue_Capital_firm','Location_of_your_Firm','profile_picture','GST_or_Licencse_Number','Your_website_Link','Briefly_Describe_your_firms_Investments_and_expectations')
        
        widgets = {
            'Name_of_your_Ventrue_Capital_firm' : forms.TextInput(attrs={'class':'form-control'}),
            'Location_of_your_Firm' : forms.TextInput(attrs={'class':'form-control'}),
            'profile_picture' : forms.FileInput(attrs={'class':'form-control'}),
            'GST_or_Licencse_Number' : forms.NumberInput(attrs={'class':'form-control'}),
            'Your_website_Link' : forms.URLInput(attrs={'class':'form-control'}),
            'Briefly_Describe_your_firms_Investments_and_expectations' : forms.Textarea(attrs={'class':'form-control'})

        }      


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
