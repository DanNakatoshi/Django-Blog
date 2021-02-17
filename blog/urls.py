from django.urls import path
from .views import IndexView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<pk>/post', PostDetailView.as_view(), name='post-detail'),
]

