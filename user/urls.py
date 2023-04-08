from django.urls import path
from user import views

urlpatterns = [
    path("register/",views.register_user,name="register"),
    path("login/",views.login,name="login"),
    path("getuserbyid/<int:id>",views.get_user_by_id,name="getuserbyid"),
    path("updateuser/<int:id_user>",views.set_user,name="updateuser"),
]
