from django.db import models

class BdWords(models.Model):
    word = models.TextField(null=False, default='APPLE')
    trl_word = models.TextField(null=False, default='ЯБЛОКО')
