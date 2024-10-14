from django import forms
from .models import Encryption,Decryption

class EncryptionForm(forms.ModelForm):
    class Meta:
        model = Encryption
        field = '__all__'

class DecryptionForm(forms.ModelForm):
    class Meta:
        model = Decryption
        field = '__all__'