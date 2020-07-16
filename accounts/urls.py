from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('loginPage/', views.loginPage,name='login'),
    path('register/', views.register,name='register'),
    path('logoutUser/', views.logoutUser,name='logout'),
    path('addProject/', views.addProject,name='addProject'),
    path('projectReport/', views.projectReport,name='projectReport'),
    path('updateProject/<str:pk>/', views.updateProject,name='updateProject'),
    path('deleteProject/<str:pk>/', views.deleteProject,name='deleteProject'),
    path('addBug/<str:pk>/', views.addBug,name='addBug'),
    path('bugReport/<str:pk>/', views.bugReport,name='bugReport'),
    path('updateBug/<str:pk>/', views.updateBug,name='updateBug'),
    path('deleteBug/<str:pk>/', views.deleteBug,name='deleteBug'),
    path('user/', views.userPage,name='userPage'),

] 
 