from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.create,name="create"),
    path('list/',views.list,name="list"),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='delete'),
    path('login/',views.login,name='login'),
    path('signup/',views.user,name='signup'),
    path('logout/',views.logout,name='logout'),
]