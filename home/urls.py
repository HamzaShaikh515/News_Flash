from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("register/",views.register, name = "register"),
    path("login/",views.login_page, name = "login"),
    path("everything/",views.everything_news, name = "everything"),
    path("top-headlines/",views.top_headlines, name = "top-headlines"),
    path("profile/", views.user_profile, name = "profile"),
    path("logout/", views.logout_view, name = "logout"),
    path("add_article/", views.add_article_view, name = "add_article"),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('user_articles/',views.user_articles,name='user_articles'),
    path('article_view/',views.article_view,name='article_view'),
]
#apikey = 'c384de4445624993bef7fac28f71a494'