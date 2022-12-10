import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_number(string):
    regex = '^[7]'
    valid = re.compile(regex)
    if valid.search(string) is None:
        raise ValidationError(
            _(f'{string} should start with 7')
        )
    if len(string) < 11:
        raise ValidationError(
            _(f'Number length must be 11 digits, your length is {len(string)}')
        )
