from .models import Register
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    