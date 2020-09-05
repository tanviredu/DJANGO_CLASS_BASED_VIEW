from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from .models import Auto,Make
from .forms import MakeForm



class MainView(LoginRequiredMixin, View):
    ## list view process the get request
    ## this will use the View and the Login Required Mixin
    ## this is the list view so only get
    def get(self,request):
        ## collec the data from the model
        mc = Make.objects.all().count()
        al = Auto.objects.all()
        context = {'make_count':mc,'auto_list':al}
        return render(request,'autos/auto_list.html',context)

class MakeView(LoginRequiredMixin, View):
    ## this is also a List View for the main
    ## so there is loginrequired mixin for login
    ## and the View and no post
    def get(self,request):
        ml = Make.objects.all()
        ctx = {'make_list':ml}
        return render(request,'autos/make_list.html',ctx)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class MakeCreate(LoginRequiredMixin, View):
    ## this is a create view 
    ## so need both get and the post
    ## we need a form and success url too
    template = "autos/make_form.html"
    #3 redirect to home page named 'all'
    success_url = reverse_lazy('autos:all')
    
    ## this is the get request
    def get(self,request):
        form = MakeForm()
        ctx = {'form':form}
        return render(request,self.template,ctx)

    ## this is the post request
    def post(self,request):
        ## means user actually hit post
        form = MakeForm(request.POST)
        if not form.is_valid():
            ## return again
            ctx = {'form':form}
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class MakeUpdate(LoginRequiredMixin, View):
    ### this is update
    ## we need get post both with form 
    ## and we need Model too
    ## we need the form and the model


    model = Make
    success_url = reverse_lazy('autos:all')
    template  = "autos/make_form"  ## same form for creating make

    def get(self,request,pk):
        ## get the make object
        ## from the model
        ## so we can know which instance we need to update
        make = get_object_or_404(self.model,pk)
        form = MakeForm(instance=make)
        ctx = {'form':form}
        return render(request,self.template,ctx)

    def post(self,request,pk):
        ## again fetch the model
        ## when post is hit
        ## why we did it again in the post
        ## because if the form not valid we need
        ## to send a form get here too
        ## you have to write a complete get request inside a post 
        ## too

        make = get_object_or_404(Make,pk=pk)
        ## you need to show which model instance you need to edit
        ## with the edit information
        form = MakeForm(request.POST,instance=make)
        if not form.is_valid():
            ctx = {'form':form}
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.success_url)




class MakeDelete(LoginRequiredMixin, View):
    ## delte is also a both get and post request
    ## the model and the model instalce
    ## model is needed because you need specfy
    ## which object you need to delete
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_confirm_delete.html'


    def get(self,request,pk):
        make = get_object_or_404(self.model,pk=pk)
        ## send the model to the template
        ## for watching which model is deleted
        ctx = {'make':make}
        return render(request,self.template,ctx)


    def post(self,request,pk):
        make = get_object_or_404(self.model,pk=pk)
        make.delete()
        return redirect(self.success_url)







### doing the same thing with the generic view




class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto 
    fields = '__all__'
    success_url = reverse_lazy('autos:all')



class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto 
    fields = "__all__"
    success_url = reverse_lazy('autos:all')



# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview