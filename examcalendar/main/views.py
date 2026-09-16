from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Exam

# Remember to implement login required!

@login_required
def index(req):
    ctx = {"examJSON": serializers.serialize("json", Exam.objects.all())}
    return render(req, "index.html", ctx)

@login_required
def altmonth(req, month):
    if month==0: return index(req)
    ctx = {"examJSON": serializers.serialize("json", Exam.objects.all()),
      "month": month}
    return render(req, "altmonth.html", ctx)