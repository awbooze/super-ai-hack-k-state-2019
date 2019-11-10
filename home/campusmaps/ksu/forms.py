from django import forms

class UploadSVG (forms.Form):
    building_name = forms.CharField(label="Building Name", max_length=200)
    abbreviation = forms.CharField(label="Abbreviation", max_length=10)
    floorNum = forms.IntegerField(label="Floor Number")
    image = forms.FileField(label="Upload SVG")