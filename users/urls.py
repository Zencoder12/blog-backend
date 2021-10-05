from django.urls import path
from .views import CustomerUserCreate, BlacklistTokenView

app_name = 'users'

urlpatterns = [
    path('register/', CustomerUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name="blacklist")
]
