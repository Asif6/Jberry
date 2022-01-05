from django.urls import path
from home.views.index import Index
from home.views.signup import Signup
from home.views.login import Login, Logout

from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', Signup.as_view(), name='signup'),
    path("login/", Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    path('password_reset/', auth_view.PasswordResetView.as_view(), name="password_reset"),

    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
