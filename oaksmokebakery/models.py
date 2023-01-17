from django.conf import settings
from django.db import models

CATEGORIES = [
    ('Bread', 'Bread'),
    ('Cake', 'Cake'),
    ('Pastries', 'Pastries'),
    ('Specialty Bread', 'Specialty Bread'),
    ('Ocassion Cake', 'Ocassion Cake'),
]


class Item(models.Model):
    """ A model for structure of items """
    title = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORIES, max_length=25, null=True)


    def __str__(self):
        """ To present the title of item """
        return self.title
    


class OrderItem(models.Model):
    """ Structure for the items order """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.title, self.price
    

class OrderCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    


