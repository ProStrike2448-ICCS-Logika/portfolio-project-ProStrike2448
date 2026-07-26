from django.contrib.auth.forms import UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'phone_number',
            'first_name',
            'last_name',
        )
