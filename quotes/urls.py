from django.urls import path
from . import views
#efe279573f74b7ef827f9f52f696376a account no.
#pk_578314fa031149afabb112f6e4e3e7e2  api token
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about,name="about"),
    path('tickerDB.html', views.tickerDB, name="tickerDB"),
    path('delete.html', views.delete, name="delete"),
    path('deleteDB/<ticker_id>', views.deleteDB, name="deleteDB"),
    #path('delete_db/<str:ticker_id>',views.delete_db,name="delete_db"),
   

]