INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'موقع_المرضى',  # اسم التطبيق
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'موقع_المرضى',  # اسم قاعدة البيانات
        'USER': 'مستخدم',  # اسم المستخدم
        'PASSWORD': 'كلمة_المرور',  # كلمة المرور
        'HOST': 'localhost',  # عنوان الخادم
        'PORT': '3306',  # منفذ الخادم
    }
}
