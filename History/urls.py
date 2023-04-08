from django.urls import path
from History import views

urlpatterns = [
    path("createHistory/<int:id_user>",views.create_history,name="create"),
    path("getlistHistory/<int:id_user>",views.getHistory,name="listHistory"),
    path("removeHistory/<int:id>",views.removeHistory,name="deleteHistory"),
]
