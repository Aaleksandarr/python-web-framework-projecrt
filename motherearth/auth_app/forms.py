from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from motherearth.auth_app.models import Profile, MotherearthUser
from motherearth.common.helpers import BootstrapFormMixin

UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    region = forms.ChoiceField(choices=[
        ("Западно Северняшко", "Западно Северняшко"),
        ("Лудогорие", "Лудогорие"),
        ("Добруджа", "Добруджа"),
        ("Шоплук", "Шоплук"),
        ("Тракия", "Тракия"),
        ("Македония", "Македония"),
        ("Родопа", "Родопа"),
        ("Странджа", "Странджа"),
    ]
    )
    email = forms.EmailField()

    description = forms.CharField(
        widget=forms.Textarea,
    )
    photo = forms.FileField()
    place = forms.CharField(
        max_length=20,
    )
    phone_number = forms.IntegerField(

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            region=self.cleaned_data['region'],
            photo=self.cleaned_data['photo'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
            place=self.cleaned_data['place'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'photo', 'first_name', 'last_name', 'region', 'description')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Първо име',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Фамилия',
                }
            ),
            'place': forms.TextInput(
                attrs={
                    'placeholder': 'Enter place',
                }
            ),
            'phone_number': forms.IntegerField(

            ),

        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'photo': forms.FileField(

            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                },
            ),

            'region': forms.ChoiceField(choices=[
                ("Западно Северняшко", "Западно Северняшко"),
                ("Лудогорие", "Лудогорие"),
                ("Добруджа", "Добруджа"),
                ("Шоплук", "Шоплук"),
                ("Тракия", "Тракия"),
                ("Македония", "Македония"),
                ("Родопа", "Родопа"),
                ("Странджа", "Странджа"),
            ]
            ),
            'place': forms.TextInput(
                attrs={
                    'placeholder': 'Enter place',
                }
            ),
            'phone_number': forms.IntegerField(

            ),
        }


class DeleteUserForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.posts.all().delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = MotherearthUser
        fields = ()
