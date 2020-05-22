from django.urls import path
from django.contrib.auth import views as auth_views
from .views import accountSettings,userPage,logoutUser,registerPage,loginPage, home,products,updateOrder,customer,createOrder,deleteOrder

urlpatterns = [
    path('',home, name='home'),
    path('user/',userPage , name='user-page'),
    path("login/",loginPage,name='login'),
    path('account/' , accountSettings , name = 'account'),
    path("logout/",logoutUser,name='logout'),
    path("register/",registerPage,name='register'),
    path("products/",products,name='products'),
    path("customers/<str:pk_test>/",customer,name='customers'),
    path("create_order/<str:pk>/",createOrder , name="create_order"),
    path("update_order/<str:pk>/",updateOrder , name="update_order"),
    path("delete_order/<str:pk>/",deleteOrder , name="delete_order"),
    path('reset_password/', auth_views.PasswordResetView.as_view(),name = 'reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name = 'password_reset_confirm'),
    path('reset_password_completed/', auth_views.PasswordResetCompleteView.as_view(),name = 'password_reset_complete'),
]

