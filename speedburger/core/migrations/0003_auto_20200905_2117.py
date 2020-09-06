# Generated by Django 3.1.1 on 2020-09-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_hamburguer_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hamburguer',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='hamburguer',
            name='value',
        ),
        migrations.AddField(
            model_name='hamburguer',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='hamburguer',
            name='image',
            field=models.ImageField(default='uploads/hamburguer_defalt.png', upload_to='uploads/'),
        ),
    ]
