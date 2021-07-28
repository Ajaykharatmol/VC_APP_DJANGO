from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm,InvestmentForm,InvestorForm,Account_DetailsForm,Company_DetailsForm,ProfileForm,billing_detailsForm, Pay_nowForm,UPIForm,UPIwalletForm,CheckBox,CheckBox1,CheckBox2,CheckBox4,VC_with_VCXForm,VC_without_VCXForm
from .models import Dashboard1,Profile,Investment,Administator,Employees,Subscription1,Monthly_Reports1
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
from django.shortcuts import render,HttpResponse,redirect




def hello(request):
    return HttpResponse("Hello World")

def index(request): 
    return render(request, 'index.html', {'title':'index'})

def register(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            email = form.cleaned_data.get('email') 
             
            htmly = get_template('Email.html') 
            d = { 'username': username } 
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email 
            html_content = htmly.render(d) 
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            msg.attach_alternative(html_content, "text / html") 
            msg.send() 
             
            messages.success(request, f'Your account has been created ! You are now able to log in') 
            return redirect('login') 
    else: 
        form = UserRegisterForm() 
    return render(request, 'register.html', {'form': form, 'title':'reqister here'})

def Login(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            form = login(request, user) 
            messages.success(request, f' welcome {username} !!') 
            return redirect('For_Investers') 
        else: 
            messages.info(request, f'account done not exit plz sign in') 
    form = AuthenticationForm() 
    return render(request, 'login.html', {'form':form, 'title':'log in'})

def new(request): 
    return render(request, 'login5.html')



def SignUpJoin(request): 
    return render(request, 'SignUpJoin.html', {'title':'SignUpJoin'})

def For_Investers(request):
    return render(request, 'For_Investers.html')
    
def For_Investers1(request):
    context ={} 
    form =  CheckBox(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'For_Investers1.html',context)


def For_Investers2(request):
    context ={} 
    form =  CheckBox4(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'For_Investers2.html',context)

def For_Investers3(request):
    context ={} 
    form =  VC_with_VCXForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'For_Investers3.html',context)

def For_Investers4(request):
    context ={} 
    form =  VC_without_VCXForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'For_Investers4.html',context)


def display(request):
    emp = Profile.objects.all()
    return render(request, 'display.html',{'emp':emp})
    

def Dashboard(request):
    depts = Investment.objects.all()
    return render(request, 'Dashboard.html',{'depts':depts})

def View_Startup(request):
    return render(request, 'View_Startup.html')

def Monthly_Reports(request):
    depts = Monthly_Reports1.objects.all()
    return render(request, 'Monthly_Reports.html',{'depts':depts})

def Invest(request):
    return render(request, 'Invest.html')

def Invest1(request):
    return render(request, 'Invest1.html')

def Invest2(request):
    if request.method == 'POST':
        context ={} 
        Investment_Form = InvestmentForm(request.POST or None, request.FILES or None) 
        Investor_Form = InvestorForm(request.POST or None, request.FILES or None) 
        Account_Details_Form = Account_DetailsForm(request.POST or None, request.FILES or None) 
        if Investment_Form.is_valid() or  Investor_Form.is_valid() or Account_Details_Form.is_valid():
            Investment_Form.save() 
            Investor_Form.save()
            Account_Details_Form.save()
            return render(request, "Invest2.html", context)

    else:
        context ={} 
        context['Investment_Form']= InvestmentForm()
        context['Investor_Form']= InvestorForm()
        context['Account_Details_Form']= Account_DetailsForm()
    return render(request, "Invest2.html", context)

def addInvestment(request):
    if (request.method=="GET"):
        form  =  InvestmentForm()
        return render(request,'Invest2.html',{"form":form})
    else:
        #save code
        form =  InvestmentForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Invest2)

def addInvestor(request):
    if (request.method=="GET"):
        form  =  InvestorForm()
        return render(request,'Invest2.html',{"form":form})
    else:
        #save code
        form =  InvestorForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Invest2)
            

def addbank(request):
    if (request.method=="GET"):
        form  =  Account_DetailsForm()
        return render(request,'Invest2.html',{"form":form})
    else:
        #save code
        form =  Account_DetailsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Invest2)



def Pending_deals(request):
    depts = Dashboard1.objects.all()
    return render(request, "Pending_deals.html",{'depts':depts})

    
def Pending(request):
    context ={} 
    form =  InvestmentForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'Pending.html',context)

def addpending(request):
    if (request.method=="GET"):
        form  =  InvestmentForm()
        return render(request,'Pending.html',{"form":form})
    else:
        #save code
        form =  InvestmentForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Pending)

    


        

def Notifications(request):
    return render(request, 'Notification.html')

def Profile(request):
    return render(request, 'Profile.html')

def My_Profile(request):
    context ={} 
    form =  ProfileForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'My_profile.html',context)

def addCat(request):
    if (request.method=="GET"):
        form  =  ProfileForm()
        return render(request,'My_Profile.html',{"form":form})
    else:
        #save code
        form =  ProfileForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(My_Profile)



def Company_Profile(request):
    context ={} 
    form =  Company_DetailsForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'Company_Profile.html',context)

def addCompany_Profile(request):
    if (request.method=="GET"):
        form  =  Company_DetailsForm()
        return render(request,'Company_Profile.html',{"form":form})
    else:
        #save code
        form =  Company_DetailsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(Company_Profile)

def Administator1(request):
    admn = Administator.objects.all()
    return render(request,'Company_Profile.html',{'admn':admn})

def Employees1(request):
    emp1 = Employees.objects.all()
    return render(request,'Company_Profile.html',{'emp1':emp1})
    

def Subscription(request):
    sub = Subscription1.objects.all()
    return render(request, 'Subscription.html',{'sub':sub})

def billing_details(request):
    context ={} 
    form =  billing_detailsForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'billing_details.html',context)   

def payment(request):
    if request.method == 'POST':
        context ={} 
        Pay_now_Form = Pay_nowForm(request.POST or None, request.FILES or None) 
        UPI_Form = UPIForm(request.POST or None, request.FILES or None) 
        UPIwallet_Form = UPIwalletForm(request.POST or None, request.FILES or None) 
        if Pay_now_Form.is_valid() or  UPI_Form.is_valid() or UPIwallet_Form.is_valid():
            Pay_now_Form.save() 
            UPI_Form.save()
            UPIwallet_Form.save()
            return render(request, "payment.html", context)

    else:
        context ={} 
        context['Pay_now_Form']= Pay_nowForm()
        context['UPI_Form']= UPIForm()
        context['UPIwallet_Form']= UPIwalletForm()
    return render(request, "payment.html", context)
   

def action_page(request):
    if (request.method=="GET"):
        form  =  Pay_nowForm()
        return render(request,'payment.html',{"form":form})
    else:
        #save code
        form =  Pay_nowForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return HttpResponse("Payment Received")

def UPI_page(request):
    if (request.method=="GET"):
        form  =  UPIForm()
        return render(request,'payment.html',{"form":form})
    else:
        #save code
        form =  UPIForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return HttpResponse("Payment Received")

def WALLET_page(request):
    if (request.method=="GET"):
        form  =  UPIwalletFormm()
        return render(request,'payment.html',{"form":form})
    else:
        #save code
        form =  UPIwalletForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return HttpResponse("Payment Received")

def FAQs(request):
    return render(request, 'FAQs.html')

def Signout(request):
    if(request.method=="POST"):
            udata = request.POST.get("username")
            request.session["username"]=udata
            session.pop['username', None]
    return redirect(Login)
