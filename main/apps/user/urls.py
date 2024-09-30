from django.urls import path, include
# from .views import GoogleLoginView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # path('oauth/google/', GoogleLoginView.as_view(), name='google_login'),
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
]
