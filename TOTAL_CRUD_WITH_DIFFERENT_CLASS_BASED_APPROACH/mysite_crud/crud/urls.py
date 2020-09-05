from django.urls import path
from . import views

app_name = "data"

urlpatterns = [
    path("",views.ShowList.as_view(),name="all"),
    path("create/",views.Create.as_view(),name="create"),
    path("update/<int:pk>/",views.MakeUpdate.as_view(),name="update"),
    path("delete/<int:pk>/",views.Delete.as_view(),name="delete")

]