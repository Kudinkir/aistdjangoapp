from django import forms
from aistsiteapp.models import Subscribe, Callback

class SubscribeForm(forms.ModelForm):
    # user_name = forms.CharField(max_length=100, required=True)
    # email = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Subscribe
        fields = ('email', 'amount')

class CallbackForm(forms.ModelForm):
    # user_name = forms.CharField(max_length=100, required=True)
    # email = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Callback
        fields = ( 'email', 'text')

# class UserFormFormEdit(forms.ModelForm):
#     email = forms.CharField(max_length=100, required=True)
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
# class PizzaShopForm(forms.ModelForm):
#     class Meta:
#         model = PizzaShop
#         fields = ('name', 'phone', 'address', 'logo')
#
# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ('name', 'short_description', 'image', 'price')
