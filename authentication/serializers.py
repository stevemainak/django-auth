from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128,min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self,validate_data):
        password = validate_data.pop("password",None)
        instance = self.Meta.model(**validate_data)
        print(instance)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    
    
class LoginSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length =255, min_length =3)
    password = serializers.CharField(max_length=128,min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password','token')

        read_only_fields = ['token']

    