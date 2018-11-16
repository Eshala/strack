from django.contrib import auth
from django.db import models


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)