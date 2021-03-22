from django.urls import path,include

from youtubeapp import views

app_name = 'ytproject'

urlpatterns = [
    path('',views.index,name='index'),
    path('download/', views.download, name='download'),
    path('download/<resolution>/', views.yt_download_done, name='download_done'),

]
