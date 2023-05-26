from django.urls import path

from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView, UserIdFromEmailView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:id>/', UserProfileView.as_view(), name='profile-detail'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('profile/email-to-id/', UserIdFromEmailView.as_view(), name='email-to-id'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    # path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]