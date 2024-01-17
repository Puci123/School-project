from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", views.auth_logout, name='auth_logout'),
    path("mysite/", views.account_site, name="account site"),
    path("mysite/mylists/", views.game_lists_site, name="game lists"),
    path("mysite/mylists/addlist/", views.list_form, name="add list"),
    path("mysite/mylists/<slug:gl_slug>/", views.game_list, name="game list"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/mysite/change_password/', views.change_password, name='change_password')
]