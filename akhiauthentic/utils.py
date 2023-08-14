from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestampt):
        return (six.text_type(user.pk)+six.text_type(timestampt)+six.text_type(user.is_active))
generate_token=TokenGenerator()
