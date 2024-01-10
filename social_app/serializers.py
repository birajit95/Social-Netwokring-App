from rest_framework import serializers
from .models import FriendStatus, User
from rest_framework.exceptions import ValidationError


class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=50, required=True, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

        extra_kwargs = {
            'first_name':{'required': True},
            'last_name':{'required': True},
            'email':{'required': True}
            }

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError('User already exists with this email id')
        return email
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('password does not match')
        
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        instance = User.objects.create_user(**validated_data)
        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    

class FriendRequestSendSerializer(serializers.Serializer):
    requested_user_id = serializers.IntegerField()

    def validate_user(self, user_id):
        user = User.objects.filter(id=user_id).first()
        if not user:
            raise ValidationError('Invalid user id passed')
        return user.id


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class FriendRequestAcceptRejectSerializer(serializers.ModelSerializer):
    source_user = UserSerializer()
    class Meta:
        model = FriendStatus
        fields = ['id', 'status', 'source_user']

        extra_kwargs = {
            'source_user': {'read_only': True}
        }

    def validate_status(self, status):
        if status not in ['accepted', 'rejected']:
            raise ValidationError('status must be either accepted or rejected')
        return status
    


class PendinFriendRequestSerializer(FriendRequestAcceptRejectSerializer):
    pass
