from django.db import models

class المريض(models.Model):
    اسم = models.CharField(max_length=255)
    تاريخ_الميلاد = models.DateField()
    عنوان = models.TextField()
    رقم_الهاتف = models.CharField(max_length=20)
    البريد_الإلكتروني = models.EmailField(unique=True)
    كلمة_المرور = models.CharField(max_length=255)

class الاشتراك(models.Model):
    نوع_الاشتراك = models.CharField(max_length=255)
    تاريخ_البدء = models.DateField()
    تاريخ_الانتهاء = models.DateField()
    مبلغ_الاشتراك = models.DecimalField(max_digits=10, decimal_places=2)
    مريض = models.ForeignKey(المريض, on_delete=models.CASCADE)

class الدفع(models.Model):
    تاريخ_الدفع = models.DateField()
    مبلغ_الدفع = models.DecimalField(max_digits=10, decimal_places=2)
    طريقة_الدفع = models.CharField(max_length=255)
    حالة_الدفع = models.CharField(max_length=255)
    اشتراك = models.ForeignKey(الاشتراك, on_delete=models.CASCADE)
