# Generated by Django 4.1.5 on 2023-01-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_demanddata_geodata'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docs', models.FileField(upload_to='files/', verbose_name='Файл Навыков xlsx')),
            ],
            options={
                'verbose_name': 'Навыки',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.AlterModelOptions(
            name='demanddata',
            options={'verbose_name': 'Востребованность', 'verbose_name_plural': 'Востребованность'},
        ),
        migrations.AlterField(
            model_name='demanddata',
            name='image',
            field=models.ImageField(upload_to='files/', verbose_name='Графика востребованности'),
        ),
        migrations.AlterField(
            model_name='geodata',
            name='docs',
            field=models.FileField(upload_to='files/', verbose_name='Файл Географии xlsx'),
        ),
    ]
