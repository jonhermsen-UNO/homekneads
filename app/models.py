from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=50)
    weight_uom = models.CharField(max_length=3)

    def get_icon(self):
        """This method attempts to match a species name with a Font Awesome icon.
        If a match is found, it is returned, otherwise a default icon is returned.
        """
        icon_options = {
            'bird': 'dove',
            'cat': 'cat',
            'dog': 'dog',
            'fish': 'fish',
            'frog': 'frog',
            'horse': 'horse',
        }
        return icon_options.get(self.name.lower(), 'paw')
    icon = property(get_icon)

    def __str__(self):
        return "%s (%s)" % (self.name, self.weight_uom)


class Animal(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    adoption_fee = models.DecimalField(max_digits=5, decimal_places=2)
    is_male = models.BooleanField()
    image = models.ImageField(upload_to='animals')

    def __str__(self):
        return "%s the %s" % (self.name, self.species.name)
