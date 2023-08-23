from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from . forms import MovieForm


# Create your views here.
def index(request):
    movie_list = movie.objects.all()
    context = {
        'list': movie_list
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movieid=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'cine':movieid})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        adding=movie(name=name,desc=desc,year=year,img=img)
        adding.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    Movie=movie.objects.get(id=id)
    form=MovieForm(request.POST or None ,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':Movie})

def delete(request,id):
    if request.method=='POST':
        dele=movie.objects.get(id=id)
        dele.delete()
        return redirect('/')
    return render(request,'delete.html')