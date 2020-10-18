from django.db import models
from core.models import *

# Create your models here.


class CartItem(models.Model):
    cart_key = models.CharField('Chave_carrinho', max_length=40, db_index=True)
    product = models.ForeignKey(Product, verbose_name='Produto',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade',default = 1)
    price = models.DecimalField('Preco', max_digits=8, decimal_places=2)


    class Meta:
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Item do carrinhos'
    
    def __str__(self):
        return '{} [{}]'.format(self.product,self.quantity)

