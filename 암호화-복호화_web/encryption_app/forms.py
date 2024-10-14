from django import forms

class EncryptionForm(forms.Form):
    text = forms.CharField(max_length=255, label='암호화할 텍스트')
    key = forms.CharField(max_length=4, label='암호화 키 (4자리 숫자)')

class DecryptionForm(forms.Form):
    text = forms.CharField(max_length=255, label='복호화할 텍스트')
    key = forms.CharField(max_length=4, label='복호화 키 (4자리 숫자)')