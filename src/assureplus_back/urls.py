"""assureplus_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import delete_sinistre, get_user_sinitre, index, modify_sinistre
from .views import save_user, save_comment, modify_user, delete_user, not_connected
from .views import upload_file,save_sinistre

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', index, name ='index'),
    path('upload_file/', upload_file, name ='upload_file'),
    path('save_sinistre/', save_sinistre, name ='save_sinitre'),
    path('delete_sinistre/<int:id>',delete_sinistre, name='delete_sinistre'),
    path('modify_sinistre/<int:id>',modify_sinistre, name='modify_sinistre'),
    path('save_user/', save_user, name ='save_user'),
    path('save_comment/', save_comment, name ='save_comment'),
    path('get_user_sinitre/<int:id>', get_user_sinitre, name ='get_user_sinitre'),
    path('modify_user/<int:id>', modify_user, name ='modify_user'),
    path('delete_user/<int:id>', delete_user, name ='modify_user'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('not_connected/',not_connected, name='not_connected'),
    path('admin/', admin.site.urls),
]
