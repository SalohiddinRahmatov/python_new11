import datetime

from django.shortcuts import render
from myfiles.models import Maxsulotlar
from myfiles.models import Project,Project1
from myfiles.models import *
# Create your views here.
def index(malumot):
    maxs=Maxsulotlar.objects.all()
    pro=Project.objects.all()
    if malumot.method == 'POST':
        mail = malumot.POST.get('gmail')
        Gmail(gmail=mail).save()
    return render(malumot, 'index.html',{'pro':pro,'maxs':maxs})


def about(malumot):
    ab=About.objects.all()
    if malumot.method =='POST':
      mail=malumot.POST.get('gmail')
      Gmail(gmail=mail).save()
    return render(malumot,'about.html',{'ab':ab})


def blog(malumot):
    bl=Blog.objects.all()

    if malumot.method =='POST':
        mail=malumot.POST.get('gmail')
        Gmail(gmail=mail).save()
    return render(malumot,'blog.html',{'bl':bl})



def contact(malumot):

    if 'matn' in malumot.POST:
        name=malumot.POST.get('ism')
        fam = malumot.POST.get('familya')
        gmail = malumot.POST.get('mail')
        text = malumot.POST.get('matn')
       # mail1=malumot.POST.get('gmail')
        vaqt=datetime.datetime.now()
        Murojat(ism=name,fam=fam,mail=gmail,text=text,vaqt=vaqt).save()
    elif 'gmail' in malumot.POST:
            mail = malumot.POST.get('gmail')
            Gmail(gmail=mail).save()
    return render(malumot,'contact.html')



def main(malumot):
    return render(malumot,'main.html')


def project(malumot):
    pro1 = Project1.objects.all()
    if malumot.method =='POST':
        mail=malumot.POST.get('gmail')
        Gmail(gmail=mail).save()
    return render(malumot,'project.html',{'pro1':pro1})


def services(malumot):
    ser=Services.objects.all()
    if malumot.method =='POST':
        mail=malumot.POST.get('gmail')
        Gmail(gmail=mail).save()
    return render(malumot,'services.html',{'ser':ser})

def single(malumot):
    return render(malumot,'single.html')

#def projects(malumot):
 #   return render(malumot,'project.html')