from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'cus_name': "Customer Name:",
            'cus_ph': "Customer Phone:",
            'name': "Event Name:",
            'booking_date': "Booking Date:",
            'members_attending': "Number of Members Attending:",
            'approximate_amount': "Approximate Amount:",  
        }
    
    approximate_amount = forms.DecimalField(max_digits=10, decimal_places=2, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  
            self.fields['approximate_amount'].initial = self.instance.members_attending * 50  
        else: 
            self.fields['approximate_amount'].initial = 0
