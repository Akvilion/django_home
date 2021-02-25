from django.db import models

# Create your models here.

class Bb(models.Model):
    title = models.TextField(max_length=250, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name="Опис")
    price = models.FloatField(null=True, blank=True, verbose_name="Ціна") 
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.TextField(max_length=20, db_index=True, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']

    def __str__(self):
        return self.name