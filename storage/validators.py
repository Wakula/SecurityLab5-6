from django.core.exceptions import ValidationError


class RepeatingCharactersSequenceValidator:
    def __init__(self, max_length=2):
        self.max_length = max_length

    def validate(self, password, user=None):
        characters = set(password)
        for c in characters:
            if password.count(c) <= self.max_length:
                continue
            if c * (self.max_length+1) in password:
                raise ValidationError({'Password contains sequence of repeating characters'})

    def get_help_text(self):
        return f'Password can not contain sequence of repeating characters with length more than {self.max_length}'
