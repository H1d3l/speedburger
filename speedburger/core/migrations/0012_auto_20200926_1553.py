# Generated by Django 3.1.1 on 2020-09-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200926_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='images/hamburguer'),
        ),
    ]
