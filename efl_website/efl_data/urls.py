from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('data/', views.data, name='data'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('signuppage/', views.signuppage, name='signuppage'),
    path('signuppage/verifypage', views.verifypage, name='verifypage'),
    path('verifypage/', views.verifypage, name='verifypage'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('loginpage/forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('loginpage/signuppage', views.signuppage, name='signuppage'),
    path('loginpage/passchange-page.html', views.passchangepage, name='passchangepage'),
]
