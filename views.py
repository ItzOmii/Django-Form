from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms

def form(request):
    new_form=forms.user_form()
    diction={'text_form': new_form,'heading_1':'Information Form '}

    if request.method=='POST':
        new_form=forms.user_form(request.POST)
        diction.update({'text_form':new_form })

    return render(request,'first_app/form.html',context=diction)
