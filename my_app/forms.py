from django import forms

from . models import Individual


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Individual
        fields = ('fullname','address','mobile','balence')
                #(or) '__all__' for importing all fields in Employee model
        labels = {
            'fullname': 'Full Name',

        }



class IndividualForm(forms.ModelForm):

    class Meta:

        model = Individual
        fields = ('product','price','balence')
