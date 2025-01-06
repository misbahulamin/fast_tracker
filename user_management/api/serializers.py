from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Employee, Department, Designation

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Ensure passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        # Ensure email is unique
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': "Email already exists"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = [
            'user','name', 'company', 'department', 'mobile', 'designation',
            'employee_id', 'date_of_joining', 'assigned_line', 'assigned_block'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
