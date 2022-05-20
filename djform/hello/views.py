from django.shortcuts import redirect, render
from .forms import StudentRegistration
# Create your views here.

from .models import User


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']

            em = fm.cleaned_data['email']
            rn = fm.cleaned_data['roll_no']
            pn = fm.cleaned_data['phone_number']
            dp = fm.cleaned_data['departments']
            webd = fm.cleaned_data['is_webd']
            gd = fm.cleaned_data['is_gd']
            ma = fm.cleaned_data['is_ma']
            ui = fm.cleaned_data['is_ui']
            ve = fm.cleaned_data['is_ve']

            com = fm.cleaned_data['comments']

            reg = User(name=nm, email=em, roll_no=rn,
                       phone_number=pn, departments=dp, is_webd=webd, comments=com, is_gd=gd, is_ma=ma, is_ui=ui, is_ve=ve)

            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    return render(request, 'hello/userregistration.html', {'form': fm})
