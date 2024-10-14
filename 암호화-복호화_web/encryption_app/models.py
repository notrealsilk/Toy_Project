from django.db import models

class Encryption(models.Model):
    content = models.CharField(max_length=255, label='암호화할 텍스트')
    key = models.CharField(max_length=4, label='암호화 키 (4자리 숫자)')

class Decryption(models.Model):
    content = models.CharField(max_length=255, label='복호화할 텍스트')
    key = models.CharField(max_length=4, label='복호화 키 (4자리 숫자)')
    
