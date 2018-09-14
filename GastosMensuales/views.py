# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render

# Create your views here.

def index(request):
    gastos = Gasto.objects.all()
    return render(request, "index.html",  {'todos_los_gastos':gastos})


def gastomonth(request):
    gastos = Gasto.objects.all()
    gastos.objects.filter(date__month='', date__year='')
    return render(request, "gastomonth.html", {'mes_gastos':gastos})