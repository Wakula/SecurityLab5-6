from sensitive_data.storage_manager import decrypt, encrypt


class SensitiveDataMixin:
    """
    Requires additional field in Model
        class Sensitive:
            sensitive_fields = (...)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for sensitive_field in self.Sensitive.sensitive_fields:
            sensitive_data = getattr(self, sensitive_field)
            if sensitive_data:
                setattr(self, sensitive_field, decrypt(sensitive_data))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        for sensitive_field in self.Sensitive.sensitive_fields:
            sensitive_data = getattr(self, sensitive_field, '')
            setattr(self, sensitive_field, encrypt(sensitive_data))
        super().save(force_insert, force_update, using, update_fields)
