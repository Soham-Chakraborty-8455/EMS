from django import forms  

class CertificateForm(forms.Form):  
    file = forms.FileField() 