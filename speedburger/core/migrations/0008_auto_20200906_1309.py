# Generated by Django 3.1.1 on 2020-09-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200905_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguer',
            name='image',
            field=models.ImageField(blank=True, default='defalt.png', upload_to=''),
        ),
    ]
