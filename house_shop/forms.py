from django import forms

from house_shop.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'buyer_name',
            'buyer_firstname',
            'comment',
            'key_time'
        )
