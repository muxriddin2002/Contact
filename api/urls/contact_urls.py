from django.urls import path
from api.views import contact_views as views

urlpatterns = [
    path("", views.ContactListAPIView.as_view(), name="user-contacts"),
    path("create", views.ContactCreateAPIView.as_view(), name="contact-create"),
    path("<int:pk>", views.ContactDetailAPIView.as_view()),
]