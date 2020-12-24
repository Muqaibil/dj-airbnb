from django import forms
from . models import RoomBook, RoomReview

class RoomBookForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
    class Meta:
        model = RoomBook
        exclude = ['room',]


class RoomReviewForm(forms.ModelForm):
    class Meta:
        model = RoomReview
        fields = ['rate', 'feedback',]

        