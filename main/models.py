from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class DemandData(models.Model):
    image = models.ImageField('Графика востребованности', upload_to='img/', blank=False)

    def __str__(self):
        return 'Востребованность ' + self.image.name

    class Meta:
        verbose_name = 'Востребованность'
        verbose_name_plural = 'Востребованность'


class GeoData(models.Model):
    docs = models.FileField('Файл Географии xlsx', upload_to='files/', blank=False)

    def __str__(self):
        return 'География ' + self.docs.name

    class Meta:
        verbose_name = 'География'
        verbose_name_plural = 'География'


class SkillsData(models.Model):
    docs = models.FileField('Файл Навыков xlsx', upload_to='files/', blank=False)

    def __str__(self):
        return 'Навыки ' + self.docs.name

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'


@receiver(pre_delete, sender=SkillsData)
def SkillsFileDelete(sender, instance, **kwargs):
    instance.docs.delete(False)


@receiver(pre_delete, sender=GeoData)
def SkillsFileDelete(sender, instance, **kwargs):
    instance.docs.delete(False)


@receiver(pre_delete, sender=DemandData)
def SkillsFileDelete(sender, instance, **kwargs):
    instance.image.delete(False)
