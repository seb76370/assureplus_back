from rest_framework import serializers
from .models import Users

class UsersListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username']
        read_only_fields = ['id','username']



class UsersReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username','email','first_name','last_name','phone_number','contract_number','street','zipcode','city','is_admin']
        read_only_fields = ['username','email','first_name','last_name','phone_number','contract_number','contract_number','street','zipcode','city','is_admin']

class UsersResetPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['password']
        read_only_fields = ['password']

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username','first_name','last_name','email','password','is_admin','street','zipcode','city','phone_number','contract_number']
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
    
