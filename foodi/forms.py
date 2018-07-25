from django import forms
class DiaryForm(forms.Form):
    servings = forms.ChoiceField(choices= ((str(x), x) for x in [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]))
    date = forms.CharField(widget=forms.DateInput(attrs={'id': 'datepicker'}))
