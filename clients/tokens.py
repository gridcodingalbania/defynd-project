from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, contact, timestamp):
        """
            Use user pass token generator to generate a token for client data confirmation
        """
        return (
            six.text_type(contact.pk) + six.text_type(timestamp) +
            six.text_type(contact.is_active)
        )


# contact data confirmation 
contact_activation_token = TokenGenerator()
