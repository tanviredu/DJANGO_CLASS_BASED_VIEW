from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import School
from .models import Student
from django.urls import reverse_lazy


class IndexView(TemplateView):
	"""docstring for IndexView"""
	template_name = "basic_app/index.html"

	## injecting data in class based view
	## sending data with dictionary
	## in the class based view
	## **kwargs will take all the value will 
	## pass no matter what you pass
	def get_context_data(self,**kwargs):

		## you dont have to understand the line
		## its basically call the base constructor
		## and override the get_context_data() method
		context = super().get_context_data(**kwargs)
		context['injectMe'] = "this is a basic injection"
		return context
                



class SchoolListView(ListView):
	model = School


class StudentListView(ListView):
	model = Student

class SchoolDetailView(DetailView):
	context_object_name = "school_detail"
	model = School
	template_name = "basic_app/school_detail.html"





class StudentDetailView(DetailView):
	context_object_name = "student_detail"
	model = Student
	template_name = "basic_app/student_detail.html"


### create a school and the create a student

class CreateSchoolView(CreateView):
	fields = ('name','printciple','location')
	model = School

class CreateStudentView(CreateView):
	fields = ('name','age','school')
	model = Student

class StudentUpdateView(UpdateView):
	fields = ('name','age','school')
	model = Student

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('basic_app:studentList')




