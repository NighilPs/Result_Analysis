from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def add(request):
    data = Result.objects.all
    return render(request, 'add.html' , { 'd' : data })

def result(request):
    return render(request, 'result.html')

def new(request):
    return render(request, 'new.html')

def mark(request):
    name = request.POST['name']
    rno = request.POST['rno']
    dob = request.POST['dob']
    mark = int(request.POST['mark'])
    if mark>90:
        grade = "A"
    elif mark>80:
        grade = "B"
    elif mark>70:
        grade = "C"
    elif mark>60:
        grade = "D"
    elif mark>54:
        grade = "E"
    else:
        grade = "F"

    data = Result(name=name, rno=rno, dob=dob, mark=mark, grade=grade)
    data.save()
    return render(request, 'new.html', {'d' : "Added Successfully"})

def changeMark(request):
    ida = request.POST['ida']
    mark = int(request.POST['newmark'])
    if mark>90:
        grade = "A"
    elif mark>80:
        grade = "B"
    elif mark>70:
        grade = "C"
    elif mark>60:
        grade = "D"
    elif mark>54:
        grade = "E"
    else:
        grade = "F"
    data = Result.objects.filter(id=ida).update(mark=mark,grade=grade)
    data2 = Result.objects.all
    return render(request, 'add.html', {'d': data2})

def result(request):
    total = Result.objects.all().count()
    a = Result.objects.filter(grade="A").count()
    b = Result.objects.filter(grade="B").count()
    c = Result.objects.filter(grade="C").count()
    d = Result.objects.filter(grade="D").count()
    e = Result.objects.filter(grade="E").count()
    f = Result.objects.filter(grade="F").count()
    dis = (a/total)*100
    first = ((b+c)/total)*100
    pas = ((total - f)/total)*100
    return render(request, 'result.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'t':total,'dis':dis,
                                          'first':first,'pas':pas})
