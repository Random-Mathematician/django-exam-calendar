from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Exam, SpecialDate
from datetime import date

TODAY = date.today()

# Remember to implement login!

@login_required
def index(req):
    theseExams = Exam.objects.filter(date__year=TODAY.year,
        date__month=TODAY.month)
    theseSDs =  SpecialDate.objects.filter(date__year=TODAY.year,
        date__month=TODAY.month)
    ctx = {
        "exams": [x.jsify() for x in theseExams],
        "specialdates": [sd.jsify() for sd in theseSDs]
    }
    return render(req, "index.html", ctx)

@login_required
def altmonth(req, month):
    if month==0: return index(req)
    # Normalize month and year because month counts past 12
    normalmonth = TODAY.month+month
    normalyear = TODAY.year+(normalmonth-1)//12
    normalmonth = (normalmonth-1)%12+1
    theseExams = Exam.objects.filter(date__year=normalyear,
        date__month=normalmonth)
    theseSDs =  SpecialDate.objects.filter(date__year=normalyear,
        date__month=normalmonth)
    ctx = {
        "exams": [x.jsify() for x in theseExams],
        "specialdates": [sd.jsify() for sd in theseSDs],
        "month": month
    }
    return render(req, "altmonth.html", ctx)

@login_required
def newExam(req):
    ctx = {
        "subjects": Exam.Subject,
        "periods": Exam.Periods,
    }
    return render(req, "newexam.html", ctx)

@login_required
def newSD(req):
    return render(req, "newsd.html", ctx)

def submit(req):
    if req.POST["content"] == "exam":
        new = Exam(
            subject=int(req.POST["subject"]),
            name=req.POST["name"],
            date=date.strptime(req.POST["date"], "%Y-%m-%d"),
            period=int(req.POST["period"]),
            isConfirmed=("isConfirmed" in req.POST)
        )
    else: raise ValueError("Invalid Submit Request Parameters")
    new.save()
    return HttpResponseRedirect("/")