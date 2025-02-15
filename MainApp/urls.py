from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('upload_files/',views.upload_files, name='upload_files'),
    path('dashboard/', views.user_dashboard, name='dashboard'),

]



