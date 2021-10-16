from django.db import models

class ProductManager():
    def create_user(self, name, precio, stock, imagen1, talla, color):
        """
        Creates and saves a product
        """
        product = self.model(name=name)
        product.set_precio(precio)
        product.set_stock(stock)
        product.set_imagen1(imagen1)
        product.set_talla(talla)
        product.set_color(color)

        product.save(using=self._db)
        
        return product


        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length = 30)
    precio = models.IntegerField('Precio', default=0)
    stock = models.IntegerField('Stock', default=0) 
    imagen1 = models.ImageField('imagen1', upload_to='producto',blank=True, null=True)
    talla = models.CharField('Talla', max_length = 30)
    color = models.CharField('Color', max_length = 30)

    def save(self, **kwargs):
        super().save(**kwargs)

    