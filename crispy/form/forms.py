import datetime
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy


class SRC_FORMS(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('index')
        self.helper.form_method = 'GET'
        self.helper.add_input('submit','Submit') 


    COURSE_CHOICES = (
        (1,"Engineering"),
        (2,"Nursing and midwifrey"),
        (3,"Law"),
        (4,"Business"),
    )
       
    
    name = forms.CharField()
    age = forms.IntegerField()
    course = forms.ChoiceField(choices=COURSE_CHOICES,
     widget=forms.RadioSelect()
    )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type":"date",
    "max":datetime}))
