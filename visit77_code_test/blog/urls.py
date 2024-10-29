from django.urls import path, include
from . import views
# from . import consumers

urlpatterns = [
    path('', views.index, name='home'),
    # path('ws/upload/', consumers.ImageUploadConsumer.as_asgi()),
]