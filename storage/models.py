from django.contrib.auth.models import AbstractUser
from django.db import models
from sensitive_data.mixins import SensitiveDataMixin
from hashlib import sha512


def pre_hash(raw_password):
    return sha512(raw_password.encode('utf-8')).hexdigest()


class SecureUser(SensitiveDataMixin, AbstractUser):
    address = models.CharField(default='', max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_password(self, raw_password):
        super().set_password(pre_hash(raw_password))

    def check_password(self, raw_password):
        return super().check_password(pre_hash(raw_password))

    class Sensitive:
        sensitive_fields = ['address']
