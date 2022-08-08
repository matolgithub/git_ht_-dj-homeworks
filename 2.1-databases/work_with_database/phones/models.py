from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return f"id:{self.id}; name:{self.name}; price (RUR):{self.price}; image:{self.image}; " \
               f"release_date:{self.release_date}; lte_exists{self.lte_exists}; slug:{self.slug}"
