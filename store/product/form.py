# forms.py
from django import forms



class FlutterWavePaymentForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Enter card number'}))
    expiration_date = forms.CharField(label='Expiration Date', max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY'}))
    cvv = forms.CharField(label='CVV', max_length=3, widget=forms.TextInput(attrs={'placeholder': 'Enter CVV'}))
    # Add other necessary fields for FlutterWave payment processing
