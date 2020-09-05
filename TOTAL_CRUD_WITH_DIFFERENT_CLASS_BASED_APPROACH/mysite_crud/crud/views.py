from django.shortcuts import render
from .models import GeekModel
from .forms import  GeekForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse,reverse_lazy



# makng list of all the Geek
# with login required mixins

class ShowList(View):
    ## its only get request
    def get(self,request):
        data = GeekModel.objects.all()
        ctx  = {"data_list":data}
        return render(request,'data/list.html',ctx)


### creating a createview
class Create(View):
    template   = "data/create.html"
    succes_url = reverse_lazy("data:all") 

    def get(self,request):
        form = GeekForm()
        ctx = {'form':form}
        return render(request,self.template,ctx)

    def post(self,request):
        form = GeekForm(request.POST)
        if not form.is_valid():
            ## if not valid send the form again
            ctx = {'form':form}
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.succes_url)



class MakeUpdate(View):

    model = GeekModel
    success_url = reverse_lazy("data:all")
    template = "data/create.html"

    def get(self,request,pk):
        ## you cant just put pk you have ti put pk=pk
        obj  = get_object_or_404(self.model,pk=pk)
        form = GeekForm(instance=obj)
        ctx  = {'form':form}
        return render(request,self.template,ctx); 

    def post(self,request,pk):
        obj = get_object_or_404(self.model,pk=pk)
        form = GeekForm(request.POST,instance=obj)
        if not form.is_valid():
            ctx = {'form':form}
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.success_url)

class Delete(View):
    model = GeekModel
    success_url = reverse_lazy("data:all")
    template = "data/confirm_delete.html"

    def get(self,request,pk):
        obj = get_object_or_404(self.model,pk=pk)
        ctx = {'obj':obj}
        return render(request,self.template,ctx)
         

    def post(self,request,pk):
        obj = get_object_or_404(self.model,pk=pk)
        obj.delete()
        return redirect(self.success_url)
        
