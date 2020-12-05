from django import forms
from . models import RoomBook

class RoomBookForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
    class Meta:
        model = RoomBook
        exclude = ['room',]
        