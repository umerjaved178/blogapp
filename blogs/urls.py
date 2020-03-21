from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
   
    path("",views.index,name='home'),
    path("<str:id>",views.detail,name="detailView"),
    path("new/",views.newForm,name="newForm"),
    path("delete/<str:id>",views.delete,name='delete'),
    path("edit/<str:id>",views.edit,name='edit'),
    path('login/',LoginView.as_view(),name='login_url'),
    path('logout/',LogoutView.as_view(next_page='login_url'),name='logout_url'),
	path('register/',views.registerView,name='register'),

]
