
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from social_app.serializers import FriendRequestAcceptRejectSerializer, FriendRequestSendSerializer, PendinFriendRequestSerializer, RegisterUserSerializer, UserLoginSerializer, UserSerializer
from social_app.paginations import StandardListPagination
from .models import FriendStatus, User
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.utils import timezone
from rest_framework.response import Response
from django.db.models import Q, Subquery

class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects.filter(email=email).first()

        if not user:
            raise ValidationError('user not found with this email')
        
        if user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)

        response = {
            'user_id': user.id,
            'token': str(token),
            'generated_at': str(timezone.now())
        }

        return Response(response, status=200)

    

class FriendRequestSendAPIView(APIView):
    serializer_class = FriendRequestSendSerializer
    throttle_scope = 'friend_request_throttle'

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = FriendRequestSendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        requested_user_id = serializer.validated_data['requested_user_id']

        FriendStatus.objects.create(
            status='requested',
            source_user=user,
            target_user_id=requested_user_id
        )
    
    

        response = {
            "status": 'requested',
            "message": "Friend request sent successfully"
        }
        return Response(response, 200)



class FriendRequestAcceptRejectAPIView(UpdateAPIView):
    serializer_class = FriendRequestAcceptRejectSerializer
    
    def get_queryset(self):
        user = self.request.user
        qs = FriendStatus.objects.filter(status='requested', target_user=user)
        return qs
    


class ListFriendsAPIView(ListAPIView):
    serializer_class = UserSerializer
    pagination_class = StandardListPagination

    def get_queryset(self):
        user = self.request.user

        qs = User.objects.filter(
            Q(
                id__in=Subquery(
                    FriendStatus.objects.filter(source_user=user, status='accepted').values_list('target_user_id', flat=True)
                    )
            ) 
            |
            Q (  id__in=Subquery(
                FriendStatus.objects.filter(target_user=user, status='accepted').values_list('source_user_id', flat=True)
            )
            )
        )
        return qs
    


class UserSearchAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = StandardListPagination


    def get_queryset(self):
        request = self.request
        search = request.query_params.get('search')

        qs = self.queryset

        if search:
            if '@' in search:
                qs = qs.filter(email=search)
            else:
                qs = qs.filter(Q(first_name__icontains=search)| Q(last_name__icontains=search))
            
        return qs
    


class PendingFriendRequestsAPIView(ListAPIView):
    serializer_class = PendinFriendRequestSerializer
    pagination_class = StandardListPagination

    def get_queryset(self):
        user = self.request.user
        qs = FriendStatus.objects.filter(
            status='requested',
            target_user = user
            )
        return qs

    






        

    
