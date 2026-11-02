from django.urls import path
from users.views.administrator import AdministratorView
from users.views.moderator import ModeratorView, ModeratorDetail
from core.views.accept_invitation import AcceptInvitationView
from core.views.login import LoginView
from core.views.logout import LogoutView
from core.views.profile import ProfileView, ProfileDetail
from core.views.reset_password import ResetPasswordView
from core.views.update_password import UpdatePasswordView
from core.views.user import UserView, UserDetail
from fuelcredit.views.invitation import InvitationView
from fuelcredit.views.transfer import TransferView
from fuelcredit.views.wallet import WalletDetail

urlpatterns = [
    # Administrators
    path('administrators', AdministratorView.as_view()),

    # Moderators
    path('moderators', ModeratorView.as_view()),
    path('moderators/<int:pk>', ModeratorDetail.as_view()),

    # Accept invitation
    path('accept_invitation/', AcceptInvitationView.as_view()),

    # Login / logout
    path('login', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    # Password management
    path('reset_password/', ResetPasswordView.as_view()),
    path('update_password/', UpdatePasswordView.as_view()),

    # Profiles
    path('profiles/', ProfileView.as_view()),
    path('profiles/<int:pk>', ProfileDetail.as_view()),

    # Users
    path('users/', UserView.as_view()),
    path('users', UserView.as_view()),
    path('users/<int:user_id>/', UserDetail.as_view()),
    path('users/<int:user_id>', UserDetail.as_view()),

    # Invitations
    path('invitations', InvitationView.as_view()),

    # Transfers
    path('transfers', TransferView.as_view()),

    # Wallets
    path('wallets/<int:pk>', WalletDetail.as_view()),
]
