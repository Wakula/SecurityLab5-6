from django.db import migrations
from sensitive_data.storage_manager import encrypt


def encrypt_empty_addresses(apps, schema_editor):
    SecureUser = apps.get_model('storage', 'SecureUser')
    for user in SecureUser.objects.filter(address=''):
        SecureUser.objects.filter(id=user.id).update(address=encrypt(''))


class Migration(migrations.Migration):
    dependencies = [
        ('storage', '0002_secureuser_address'),
    ]

    operations = [
        migrations.RunPython(encrypt_empty_addresses, migrations.RunPython.noop),
    ]
