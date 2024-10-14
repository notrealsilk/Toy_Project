from django.shortcuts import render, redirect
from .models import Encryption, Decryption
from .forms import EncryptionForm, DecryptionForm

# 메인 페이지
def index(request):
    return render(request, 'encryption_app/index.html')

# 암호화 기능
def encrypt(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            # 폼의 클린 데이터 딕셔너리로 저장
            data = {
                'content': form.cleaned_data['content'],
                'key': form.cleaned_data['key'],
            }
            shift = int(data['key'])
            encrypted = "".join([chr(ord(char) + shift) for char in data['content']])
            return render(request, 'encryption_app/result.html', {'result': encrypted, 'operation': 'Encryption'})
    else:
        form = EncryptionForm()
    return render(request, 'encryption_app/encrypt.html', {'form': form})

# 복호화 기능
def decrypt(request):
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            # 폼의 클린 데이터 딕셔너리로 저장
            data = {
                'content': form.cleaned_data['content'],
                'key': form.cleaned_data['key'],
            }
            shift = int(data['key'])
            decrypted = "".join([chr(ord(char) - shift) for char in data['content']])
            return render(request, 'encryption_app/result.html', {'result': decrypted, 'operation': 'Decryption'})
    else:
        form = DecryptionForm()
    return render(request, 'encryption_app/decrypt.html', {'form': form})
