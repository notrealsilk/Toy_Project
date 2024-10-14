from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'encryption_app/index.html')

def encrypt(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        shift = int(request.POST.get('shift', 0))
        encrypted = "".join([chr(ord(char) + shift) for char in word])
        return render(request, 'encryption_app/result.html', {'result': encrypted, 'operation': 'Encryption'})
    return render(request, 'encryption_app/encrypt.html')

def decrypt(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        shift = int(request.POST.get('shift', 0))
        decrypted = "".join([chr(ord(char) - shift) for char in word])
        return render(request, 'encryption_app/result.html', {'result': decrypted, 'operation': 'Decryption'})
    return render(request, 'encryption_app/decrypt.html')