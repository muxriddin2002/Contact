from main.models import Contact
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from api.serializers.contact_serializers import ContactSerializer
from api.permissions import IsAuthorPermission
from rest_framework.permissions import IsAuthenticated


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthorPermission]
    queryset = Contact.objects.all()


class ContactListAPIView(ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
