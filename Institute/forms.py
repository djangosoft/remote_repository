from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name :",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name..'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email:",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email..'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile number..'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your Location:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your location..'
            }
        )
    )
class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name..'
            }
        )
    )
    ratings = forms.IntegerField(
       label="Enter Ratings:",
       widget=forms.NumberInput(
           attrs={
               'class':'form-control',
               'placeholder':'Ratings..'
           }
       )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback:",
        widget= forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback..'
            }
        )
    )

