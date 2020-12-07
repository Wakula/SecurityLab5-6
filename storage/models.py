from django.contrib.auth.models import AbstractUser
from hashlib import sha512


def pre_hash(raw_password):
    return sha512(raw_password.encode('utf-8')).hexdigest()


class SecureUser(AbstractUser):
    def set_password(self, raw_password):
        super().set_password(pre_hash(raw_password))

    def check_password(self, raw_password):
        return super().check_password(pre_hash(raw_password))
