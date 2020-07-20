from django.urls import path
from . import views


app_name = "basic_app"

urlpatterns = [
    
    path('',views.IndexView.as_view(),name="index"),
    path('listschool',views.SchoolListView.as_view(),name="schoolList"),
    path('liststudent',views.StudentListView.as_view(),name="studentList"),
    path("schoolDetail/<int:pk>",views.SchoolDetailView.as_view(),name="schoolDetail"),
    path("studentDetail/<int:pk>",views.StudentDetailView.as_view(),name="studentDetail"),
    path("new",views.CreateSchoolView.as_view(),name="create"),
    path("student/new",views.CreateStudentView.as_view(),name="create_student"),
    path("student/update/<int:pk>",views.StudentUpdateView.as_view(),name="update_student"),
    path("student/delete/<int:pk>",views.StudentDeleteView.as_view(),name="delete_student"),

]