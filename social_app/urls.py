
from django.urls import path
from . import views as api_view

urlpatterns = [
    path('register/', api_view.RegisterUserAPIView.as_view(), name='register-user'), 
    path('login/', api_view.UserLoginAPIView.as_view(), name='user_login'), 
    path('send-friend-request/', api_view.FriendRequestSendAPIView.as_view(), name='send_friend_request'),
    path('accept-or-reject-request/<int:pk>', api_view.FriendRequestAcceptRejectAPIView.as_view(), name='accept_or_reject_friend_request'),
    path('friends/', api_view.ListFriendsAPIView.as_view(), name='friends_list'), 
    path('search-users/', api_view.UserSearchAPIView.as_view(), name='search_users'),
    path('pending-requests/', api_view.PendingFriendRequestsAPIView.as_view(), name='pending_requests') 




]
