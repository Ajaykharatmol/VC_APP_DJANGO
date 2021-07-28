from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from Startup import views as user_view 
from django.contrib.auth import views as auth 

urlpatterns = [
    
    path('hello',views.hello,name="hello"),
    path('register1/', user_view.register1, name ='register1'),
    path('login1/', user_view.Login1, name ='login1'), 
    path('Company_register',views.Company_register,name ='Company_register'),
    path('addCompany_register', views.addCompany_register, name ='addCompany_register'), 
    path('logout1/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout1'), 
    path('For_Startups',views.For_Startups,name="For_Startups"),
    path('Current_Investors',views.Current_Investors,name="Current_Investors"),
    path('Apply_for_Funding',views.Apply_for_Funding,name="Apply_for_Funding"),
    path('Startup_Profile',views.Startup_Profile,name="Startup_Profile"),
    path('addFounder_Details',views.addFounder_Details,name="addFounder_Details"),
    path('addStartup_Details',views.addStartup_Details,name="addStartup_Details"),
    path('addCompany_Financials',views.addCompany_Financials,name="addCompany_Financials"),
    path('addFunding_Requirements',views.addFunding_Requirements,name="addFunding_Requirements"),
    path('Pending_deals1',views.Pending_deals1,name="Pending_deals1"),
    path('bids',views.bids,name="bids"),
    path('addbids',views.addbids,name="addbids"),
    path('Investor_Details',views.Investor_Details,name="Investor_Details"),
    path('Notifications1',views.Notifications1,name="Notifications1"),
    path('Profile1',views.Profile1,name="Profile1"),
    path('My_Profile1',views.My_Profile1,name="My_Profile1"),
    path('addCat',views.addCat,name="addCat"),
    path('Startup_Company_Profile',views.Startup_Company_Profile,name="Startup_Company_Profile"),
    path('addStartup_Company_Profile',views.addStartup_Company_Profile,name="addStartup_Company_Profile"),
    path('Administator2',views.Administator2,name="Administator2"),
    path('Employees2',views.Employees2,name="Employees2"),
    path('Subscription2',views.Subscription2,name="Subscription2"),
    path('billing_details1',views.billing_details1,name="billing_details1"),
    path('payment1',views.payment1,name="payment1"),
    path('action_page1',views.action_page1,name="action_page1"),
    path('UPI_page1',views.UPI_page1,name="UPI_page1"),
    path('WALLET_page1',views.WALLET_page1,name="WALLET_page1"),
    path('FAQs1',views.FAQs1,name="FAQs1"),
    path('Signout',views.Signout,name="Signout"),

]