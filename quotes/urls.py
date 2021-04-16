from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
#efe279573f74b7ef827f9f52f696376a account no.
#pk_578314fa031149afabb112f6e4e3e7e2  api token
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about,name="about"),
    path('tickerDB.html', views.tickerDB, name="tickerDB"),
    path('register.html', views.register,name="register"),
    #path('login.html', views.login,name="login"),
    path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #path('delete_db/<str:ticker_id>',views.delete_db,name="delete_db"),
   

]
urlpatterns += staticfiles_urlpatterns()