# Generated by Django 3.2.16 on 2023-05-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20230516_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'Топпинг', 'verbose_name_plural': 'Топпинги'},
        ),
        migrations.AlterField(
            model_name='icecream',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.Topping', verbose_name='Топпинги'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='Слаг'),
        ),
    ]