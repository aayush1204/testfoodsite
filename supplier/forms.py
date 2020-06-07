<<<<<<< HEAD
#from django.forms import ModelForm
#from shop.models import Product


#class ProductForm(ModelForm):
#    class Meta:

#        model = Product
#        fields = '__all__'
=======
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:

        model = Product
        fields = '__all__'
>>>>>>> origin/b2
