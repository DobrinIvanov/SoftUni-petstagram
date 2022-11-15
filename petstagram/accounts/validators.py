from django.core.exceptions import ValidationError


def ValidateOnlyLetters(string):
    for ch in string:
        if not ch.isalpha():
            raise ValidationError('First and Last names should only contain alphabetical letters!')