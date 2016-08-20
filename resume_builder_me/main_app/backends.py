import imaplib
from django.contrib.auth.models import User

class MyBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            temp = imaplib.IMAP4("webmail.nitt.edu")
            temp.login(username, password)
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                user = User(username = username, password = 'nope')
                user.save()
            return user
        except Exception as e:
            print(e)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
