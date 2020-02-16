from.models import Login
    from rest_framework import serializers, viewsets


class LoginSerializer(serializers.ModelSerializer):

class Meta:
model = Login
fields = '__all__'



class LoginViewSet(viewsets.ModelViewSet):
queryset = Login.objects.all()
serializer_class = LoginSerializer
