from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from Investor import views as user_view 
from django.contrib.auth import views as auth 

urlpatterns = [
    
    path('hello',views.hello,name="hello"),
    path('', views.index, name ='index'),
    path('register/', user_view.register, name ='register'),
    path('login/', user_view.Login, name ='login'), 
    path('new', views.new, name ='new'),
    


    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'), 
    path('SignUpJoin/', user_view.SignUpJoin, name ='SignUpJoin'),
    path('For_Investers',views.For_Investers,name="For_Investers"),
    path('For_Investers1',views.For_Investers1,name="For_Investers1"),
    path('For_Investers2',views.For_Investers2,name="For_Investers2"),
     path('For_Investers3',views.For_Investers3,name="For_Investers3"),
    path('For_Investers4',views.For_Investers4,name="For_Investers4"),
    path('Dashboard',views.Dashboard,name="Dashboard"),
    path('View_Startup',views.View_Startup,name="View_Startup"),
    path('Monthly_Reports',views.Monthly_Reports,name="Monthly_Reports"),
    path('Invest',views.Invest,name="Invest"),
    path('Invest1',views.Invest1,name="Invest1"),
    path('Invest2',views.Invest2,name="Invest2"),
    path('addInvestment',views.addInvestment,name="addInvestment"),
    path('addInvestor',views.addInvestor,name="addInvestor"),
    path('addbank',views.addbank,name="addbank"),
    path('Pending_deals',views.Pending_deals,name="Pending_deals"),
    path('Pending',views.Pending,name="Pending"),
    path('addpending',views.addpending,name="addpending"),
    path('Notifications',views.Notifications,name="Notifications"),
    path('Profile',views.Profile,name="Profile"),
    path('My_Profile',views.My_Profile,name="My_Profile"),
    path('addCat',views.addCat,name="addCat"),
    path('Company_Profile',views.Company_Profile,name="Company_Profile"),
    path('Administator1',views.Administator1,name="Administator1"),
    path('Employees1',views.Employees1,name="Employees1"),
    path('addCompany_Profile',views.addCompany_Profile,name="addCompany_Profile"),
    path('Subscription',views.Subscription,name="Subscription"),
    path('billing_details',views.billing_details,name="billing_details"),
    path('payment',views.payment,name="payment"),
    path('action_page',views.action_page,name="action_page"),
    path('UPI_page',views.UPI_page,name="UPI_page"),
    path('WALLET_page',views.WALLET_page,name="WALLET_page"),
    path('FAQs',views.FAQs,name="FAQs"),
    path('Signout',views.Signout,name="Signout"),
    path('display',views.display,name="display"),

]