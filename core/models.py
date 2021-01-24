from django.db import models


class Produto(models.Model):
    nome = models.CharField ('Nome', max_length=100)
    preco = models.DecimalField ('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField ('Quantidade')

    def __str__(self):
        return {self.nome}, {self.estoque}


class Cliente(models.Model):
    nome = models.CharField ('Nome', max_length=100)
    sobrenome = models.CharField ('Sobrenme', max_length=100)
    email = models.EmailField ('E-mail', max_length=100)

    def __str__(self):
        return {self.nome}, {self.sobrenome}, {self.email}



