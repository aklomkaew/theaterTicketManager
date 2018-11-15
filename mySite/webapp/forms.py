from django import forms
# from ..webapp.models import Post
#
# class PaymentForm(forms.ModelForm):
#     post = forms.CharField
#
#     class Meta:
#         model = Post
#         fields = {'post',}

class PaymentForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=50)
    lastName = forms.CharField(label='Last name', max_length=50)
