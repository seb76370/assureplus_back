from django.urls import include, path

from .views import loginView, registerView, userView, logoutView

urlpatterns = [
    path('register/', registerView.as_view()),
    path('login/', loginView.as_view()),
    path('logout/', logoutView.as_view()),
    path('user/', userView.as_view()),
]

