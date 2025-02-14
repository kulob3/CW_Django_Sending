from django.db import models


class Message(models.Model):
    topic = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Содержание письма')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец', related_name='messaging', editable=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
