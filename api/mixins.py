
from rest_framework import permissions,authentication
from .permissions import IsStaffEditorPermission
from .authentication import TokenAuthentication 

class StaffEditorMixin():
    permission_classes = [
        IsStaffEditorPermission,
        permissions.IsAuthenticatedOrReadOnly
    ]
    authentication_classes = [
        TokenAuthentication
    ]

class UserQuerySetMixin():

    user_field = 'user'

    def get_queryset(self,*args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs= super().get_queryset(*args, **kwargs)
        return  qs.filter(**lookup_data)