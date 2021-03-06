"""scholarshipPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scholarships/',include('scholarships.urls')),
    path('chat/',include('talking_bot.urls'))
    path('accounts/',include('accounts.urls'))
]
<<<<<<< HEAD
urlpatterns += staticfiles_urlpatterns()
=======

urlpatterns += staticfiles_urlpatterns()
# urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
>>>>>>> b8a24efaf4c9bf1402e62f528cffc4e75a7388fc
