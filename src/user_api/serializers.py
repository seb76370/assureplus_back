from rest_framework import serializers
from .models import Users


class UsersReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username','email','first_name','last_name','contract_number','street','zipcode','city']
        read_only_fields = ['username','email','first_name','last_name','contract_number','contract_number','street','zipcode','city']

class UsersResetPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['password']
        read_only_fields = ['password']

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username','email','password','is_admin']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        is_admin = validated_data.pop('is_admin', False)

        instance = self.Meta.model(**validated_data)
        if (password is not None):
            instance.set_password(password)
        instance.save()
        if is_admin:
            instance.is_staff = True
            instance.is_superuser = True
            instance.save()
        return instance
    
