from django.shortcuts import render, redirect
from .models import المريض, الاشتراك, الدفع
from .forms import تسجيل_الدخول, إضافة_مريض, إضافة_اشتراك, إضافة_دفع

def الرئيسية(request):
    return render(request, 'الرئيسية.html')

def تسجيل_الدخول(request):
    إذا request.method == 'POST':
        شكل = تسجيل_الدخول(request.POST)
        إذا شكل.is_valid():
            اسم = شكل.cleaned_data['اسم']
            كلمة_المرور = شكل.cleaned_data['كلمة_المرور']
            مريض = المريض.objects.get(اسم=اسم, كلمة_المرور=كلمة_المرور)
            إذا مريض:
                return redirect('الرئيسية')
    شكل = تسجيل_الدخول()
    return render(request, 'تسجيل_الدخول.html', {'شكل': شكل})

def إضافة_مريض(request):
    إذا request.method == 'POST':
        شكل = إضافة_مريض(request.POST)
        إذا شكل.is_valid():
            شكل.save()
            return redirect('الرئيسية')
    شكل = إضافة_مريض()
    return render(request, 'إضافة_مريض.html', {'شكل': شكل})

def إضافة_اشتراك(request):
    إذا request.method == 'POST':
        شكل = إضافة_اشتراك(request.POST)
        إذا شكل.is_valid():
            شكل.save()
            return redirect('الرئيسية')
    شكل = إضافة_اشتراك()
    return render(request, 'إضافة_اشتراك.html', {'شكل': شكل})

def إضافة_دفع(request):
    إذا request.method == 'POST':
        شكل = إضافة_دفع(request.POST)
        إذا شكل.is_valid():
            شكل.save()
            return redirect('الرئيسية')
    شكل = إضافة_دفع()
    return render(request, 'إضافة_دفع.html', {'شكل': شكل})
