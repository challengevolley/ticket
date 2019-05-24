import random

from . import models


def factory_user(**kwargs):
    d = {
        'username': ''.join(random.choice('abcdef') for _ in range(10)),
        'first_name': '名',
        'last_name': '姓',
        'email': 'test@example.com',
        'address1': '住所1',
        'address2': '住所2',

    }
    password = kwargs.pop('password', None)
    d.update(kwargs)
    user = models.User(**d)
    if password:
        user.set_password(password)
    user.save()
    return user