# Generated by Django 3.1.1 on 2020-10-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200926_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='udemuimages/hamburguer'),
        ),
    ]
