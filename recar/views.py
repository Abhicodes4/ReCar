from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cars,Category
from django.db.models import Q
from .forms import Carform
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer,CarSerializer

def carlist(request):
    c=Cars.objects.all()
    a=Category.objects.all()
    return render(request,'recar.html',{'cars':c,'category':a})


def carview(request,c_id):
    c=Cars.objects.get(id=c_id)
    return render(request,'carview.html',{'car':c})

def carcat(request,p_id):

    c=Cars.objects.filter(category=p_id)
    a=Category.objects.all()
    print(c)
    return render(request,'Recar.html',{'cars':c,'category':a})

def create(request):
    return render(request,'create.html')


def regfn(request):
    n=request.POST['name']
    ln=request.POST['ln']
    e=request.POST['email']
    u=request.POST['usern']
    pa=request.POST['pass']
    pa2=request.POST['pass2']


    if pa==pa2 :
      
      if User.objects.filter(username=u).exists():
              
             messages.error(request,"Username taken")
             return redirect('/create')
      
      elif User.objects.filter(email=e).exists():
              
              messages.error(request,"Email already in use")
              return redirect('/create')
      
       
      else:
          User.objects.create_user(username=u,email=e,first_name=n,password=pa,last_name=ln)
          messages.success(request,"Account created succesfully")
          return redirect('/login')
      
        
    else :
        messages.error(request,"Password not matching")
        return redirect('/create')
      
    

def loginfn(request):
        
        if request.method == 'POST':
            u=request.POST['a']
            pa=request.POST['b']

            a=auth.authenticate(username=u,password=pa)

            if a:
                auth.login(request,a)

                return redirect('/recar/')
               
            
            else:
                messages.error(request,"Invalid Username or Password...please try again")
                return redirect('/login')
    
        else:   
         return render(request,'login.html')
    

def logoutfn(request):
        auth.logout(request)

        return redirect('/recar')

def searchfn(request):
    
    item=request.GET['s']
    
    cars1=Cars.objects.filter(Q(name__icontains=item) | Q(year__icontains=item)| Q(transmission__icontains=item))

    return render(request,'recar.html',{'cars':cars1})



@login_required(login_url='/login')
def sellcarfn(request):

    if request.method=="POST":
         c=Carform(request.POST,request.FILES)
         if c.is_valid():
            abc=c.save(commit=False)
            abc.us=request.user
            abc.save()

            return redirect('/recar')

    else:     
        c=Carform()
        return render(request,'sellcar.html',{'cf':c})
    

def editcarfn(request,pro_id): 
    if request.method=="POST":
         a=Cars.objects.get(id=pro_id) 

         if a.us==request.user:    

            c=Carform(request.POST,request.FILES,instance=a)
            if c.is_valid():
                c.save()  

                return redirect('/recar')
         else:
              return HttpResponse("<h1>sorry</h1>")   

    else:
        a=Cars.objects.get(id=pro_id)     
        c=Carform(instance=a)
        return render(request,'editcar.html',{'cf':c})
    


def dltcarfn(request,pro_id): 
     a=Cars.objects.get(id=pro_id) 
     a.delete()
     return redirect('/recar')

# @login_required(login_url='/login')
class SellcarfnNew(View): 

        def get(self,request):   
           c=Carform()
           return render(request,'sellcar.html',{'cf':c})
           

        def post(self,request):
                c=Carform(request.POST,request.FILES)
                if c.is_valid():
                    abc=c.save(commit=False)
                    abc.us=request.user
                    abc.save()
                return redirect('/recar')
 
class Carall(ListView):

        model=Cars 

        



class Carview(DetailView):
      
      model=Cars   


class Catadd(CreateView):
     model=Category
     fields='__all__'
     success_url='/recar'   


class Caradd(CreateView):
    model=Cars
    form_class=Carform  

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.us = self.request.user
        obj.save()
        return redirect('/recar')

class Updatecars(UpdateView):
     model=Cars
     form_class=Carform
     success_url='/recar'

class Deletecars(DeleteView):
     model=Cars
     success_url='/recar'      




def gallery(request):
    return render(request,'apitest.html')

def fake(request):
    return render(request,'fake.html')
     
def fakeview(request,pid):
    return render(request,'fakeview.html',{'id':pid})     


@api_view(['GET'])
def categoryapifn(request):
    a=Category.objects.all()
    b=CategorySerializer(a,many=True)
    return Response(b.data)


@api_view(['GET'])
def carsviewfn(request):
    a=Cars.objects.all()
    b=CarSerializer(a,many=True)
    return Response(b.data)



@api_view(['GET'])
def singlecarsviewfn(request,cid):
    a=Cars.objects.get(id=cid)
    b=CarSerializer(a,many=False)
    return Response(b.data)


@api_view(['POST'])
def addcategoryapifn(request):
    d=CategorySerializer(data=request.data)
    if d.is_valid():
       d.save() 
       return Response(d.data)


@api_view(['PUT'])
def editcategoryapifn(request,p_id):
    p=Category.objects.get(id=p_id)
    d=CategorySerializer(data=request.data,instance=p)
    if d.is_valid():
       d.save() 
       return Response(d.data)       
    

def apicall(request):
    return render(request,'apicall.html')