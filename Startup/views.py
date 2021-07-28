from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm,CompanyForm,Live_InvestorsForm,Founder_DetailsForm,Startup_DetailsForm,Company_FinancialsForm,Funding_RequirementsForm,PendingForm,BidsForm,Investor_DetailsForm,ProfileForm,Startup_Details1Form,billing_detailsForm,Pay_nowForm,UPIForm,UPIwalletForm
from .models import Live_Investors,Founder_Details,Startup_Details,Company_Financials,Funding_Requirements,Pending,Investor_Details,Company_Bids,Startup_Details1,Profile,Subscription1
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
from django.shortcuts import render,HttpResponse,redirect

def hello(request):
    return HttpResponse("Hello World")

def register1(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            email = form.cleaned_data.get('email') 
             
            htmly = get_template('Email1.html') 
            d = { 'username': username } 
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email 
            html_content = htmly.render(d) 
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            msg.attach_alternative(html_content, "text / html") 
            msg.send() 
             
            messages.success(request, f'Your account has been created ! You are now able to log in') 
            return redirect('login1') 
    else: 
        form = UserRegisterForm() 
    return render(request, 'register1.html', {'form': form, 'title':'reqister here'})

def Login1(request): 
    if request.method == 'POST': 
   
      
   
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            form = login(request, user) 
            messages.success(request, f' welcome {username} !!') 
            return redirect('For_Startups') 
        else: 
            messages.info(request, f'account done not exit plz sign in') 
    form = AuthenticationForm() 
    return render(request, 'login1.html', {'form':form, 'title':'log in'})

def Company_register(request): 
    context ={} 
    form =  CompanyForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'Company_register.html',context)

def addCompany_register(request):
    if (request.method=="GET"):
        form  =  CompanyForm()
        return render(request,'Company_register.html',{"form":form})
    else:
        #save code
        form =  CompanyForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Company_register)

def For_Startups(request): 
    return render(request, 'For_Startups.html', {'title':'For_Startups'})

def Current_Investors(request):
    depts = Live_Investors.objects.all()
    return render(request, 'Current_Investors.html',{'depts':depts})

def Apply_for_Funding(request):
    if request.method == 'POST':
        context ={} 
        Founder_Details_Form = Founder_DetailsForm(request.POST or None, request.FILES or None) 
        Startup_Details_Form = Startup_DetailsForm(request.POST or None, request.FILES or None) 
        Company_Financials_Form = Company_FinancialsForm(request.POST or None, request.FILES or None)
        Funding_Requirements_Form = Funding_RequirementsForm(request.POST or None, request.FILES or None)  
        if Founder_Details_Form.is_valid() or  Startup_Details_Form.is_valid() or Company_Financials_Form.is_valid():
            Founder_Details_Form.save() 
            Startup_Details_Form.save()
            Company_Financials_Form.save()
            Funding_Requirements_Form.save()
            return render(request, "Apply_for_Funding.html", context)

    else:
        context ={} 
        context['Founder_Details_Form']= Founder_DetailsForm()
        context['Startup_Details_Form']= Startup_DetailsForm()
        context['Company_Financials_Form']= Company_FinancialsForm()
        context['Funding_Requirements_Form']= Funding_RequirementsForm()
    return render(request, "Apply_for_Funding.html", context)


def addFounder_Details(request):
    if (request.method=="GET"):
        form  =  Founder_DetailsForm()
        return render(request,'Apply_for_Funding.html',{"form":form})
    else:
        #save code
        form =  Founder_DetailsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Apply_for_Funding) 

def addStartup_Details(request):
    if (request.method=="GET"):
        form  =  Startup_DetailsForm()
        return render(request,'Apply_for_Funding.html',{"form":form})
    else:
        #save code
        form =  Startup_DetailsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Apply_for_Funding)

def addCompany_Financials(request):
    if (request.method=="GET"):
        form  =  Company_FinancialsForm
        return render(request,'Apply_for_Funding.html',{"form":form})
    else:
        #save code
        form =  Company_FinancialsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Apply_for_Funding)


def addFunding_Requirements(request):
    if (request.method=="GET"):
        form  =  Funding_RequirementsForm()
        return render(request,'Apply_for_Funding.html',{"form":form})
    else:
        #save code
        form =  Funding_RequirementsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Apply_for_Funding)

def Pending_deals1(request):
    depts = Pending.objects.all()
    return render(request, 'Pending_deals1.html',{'depts':depts})

def bids(request):
    if request.method == 'POST':
        context ={} 
        Bids_Form = BidsForm(request.POST or None, request.FILES or None) 
        Investor_Details_Form = Investor_DetailsForm(request.POST or None, request.FILES or None) 
        
        if Bids_Form.is_valid() or  Investor_Details_Form.is_valid() :
            Bids_Form.save() 
            Investor_Details_Form.save()
            
            return render(request, "bids.html", context)

    else:
        context ={} 
        context['Bids_Form']= BidsForm()
        context['Investor_Details_Form']= Investor_DetailsForm()
    
    return render(request, "bids.html", context)

def addbids(request):
    if (request.method=="GET"):
        form  =  BidsForm()
        return render(request,'bids.html',{"form":form})
    else:
        #save code
        form =  BidsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(bids)
     

def Investor_Details(request):
    if (request.method=="GET"):
        form  =  Investor_DetailsForm()
        return render(request,'bids.html',{"form":form})
    else:
        #save code
        form =  Investor_DetailsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(bids) 
   
def Startup_Profile(request):
    return render(request, 'Startup_Profile.html')

def Notifications1(request):
    return render(request, 'Notifications1.html')

def Profile1(request):
    return render(request, 'Profile1.html')

def My_Profile1(request):
    context ={} 
    form =  ProfileForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'My_profile1.html',context)

def addCat(request):
    if (request.method=="GET"):
        form  =  ProfileForm()
        return render(request,'My_Profile1.html',{"form":form})
    else:
        #save code
        form =  ProfileForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(My_Profile)

def Startup_Company_Profile(request):
    context ={} 
    form =  Startup_Details1Form(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'Startup_Company_Profile.html',context)

def addStartup_Company_Profile(request):
    if (request.method=="GET"):
        form  =  Startup_Details1Form()
        return render(request,'Startup_Company_Profile.html',{"form":form})
    else:
        #save code
        form =  Startup_Details1Form(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(addStartup_Company_Profile)

def Administator2(request):
    admn = Administator.objects.all()
    return render(request,'Company_Profile.html',{'admn':admn})

def Employees2(request):
    emp1 = Employees.objects.all()
    return render(request,'Company_Profile.html',{'emp1':emp1})
    

def Subscription2(request):
    sub = Subscription1.objects.all()
    return render(request, 'Subscription1.html',{'sub':sub})

def billing_details1(request):
    context ={} 
    form =  billing_detailsForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'billing_details1.html',context)   

def payment1(request):
    if request.method == 'POST':
        context ={} 
        Pay_now_Form = Pay_nowForm(request.POST or None, request.FILES or None) 
        UPI_Form = UPIForm(request.POST or None, request.FILES or None) 
        UPIwallet_Form = UPIwalletForm(request.POST or None, request.FILES or None) 
        if Pay_now_Form.is_valid() or  UPI_Form.is_valid() or UPIwallet_Form.is_valid():
            Pay_now_Form.save() 
            UPI_Form.save()
            UPIwallet_Form.save()
            return render(request, "payment1.html", context)

    else:
        context ={} 
        context['Pay_now_Form']= Pay_nowForm()
        context['UPI_Form']= UPIForm()
        context['UPIwallet_Form']= UPIwalletForm()
    return render(request, "payment1.html", context)
   
def action_page1(request):
    if (request.method=="GET"):
        form  =  Pay_nowForm()
        return render(request,'payment1.html',{"form":form})
    else:
        #save code
        form =  Pay_nowForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return HttpResponse("Payment Received")

def UPI_page1(request):
    if (request.method=="GET"):
        form  =  UPIForm()
        return render(request,'payment1.html',{"form":form})
    else:
        #save code
        form =  UPIForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return HttpResponse("Payment Received")

def WALLET_page1(request):
    if (request.method=="GET"):
        form  =  UPIwalletFormm()
        return render(request,'payment1.html',{"form":form})
    else:
        #save code
        form =  UPIwalletForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return HttpResponse("Payment Received")
   
def FAQs1(request):
    return render(request, 'FAQs1.html')

def Signout(request):
    if(request.method=="POST"):
            udata = request.POST.get("username")
            request.session["username"]=udata
            session.pop['username', None]
    return redirect(Login1)
