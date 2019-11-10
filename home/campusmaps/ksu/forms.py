from django import forms

class UploadSVG form(forms.Form):
    buildingName = forms.CharField(max_length=200)
    abbreviation = forms.CharField(max_length=10)
    floorNum = forms.IntegerField(default=-1)
    image = forms.ImageField