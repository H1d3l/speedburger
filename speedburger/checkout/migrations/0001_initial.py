# Generated by Django 3.1.1 on 2020-10-17 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0013_auto_20201017_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_key', models.CharField(db_index=True, max_length=40, verbose_name='Chave_carrinho')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preco')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do carrinho',
                'verbose_name_plural': 'Item do carrinhos',
            },
        ),
    ]
