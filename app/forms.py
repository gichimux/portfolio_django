from django import forms

class ContactForm(forms.Form):
	contact_name= forms.CharField(max_length=50, label="Name")
	contact_email=forms.EmailField(max_length=50, label="Email")
	content=forms.CharField(label="Message",widget=forms.Textarea(),required=True,)
