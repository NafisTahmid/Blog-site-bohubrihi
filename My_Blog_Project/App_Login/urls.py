from django.urls import path
from App_Login import views


app_name = "App_Login"
urlpatterns = [
    path('signup/', views.sign_up, name="sign_up")  ,
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('password/', views.password_change, name='pass_change'),
    path('add-dp/', views.dp_upload, name='add_dp'),
    path('change-dp/', views.change_dp, name='change_dp')
]

