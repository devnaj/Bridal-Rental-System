from django import forms
from .models import Booking
from django.utils import timezone
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        today = timezone.now().date()

        # Prevents booking in the past
        if start_date and start_date < today:
            self.add_error('start_date', "The booking date cannot be in the past.")

        # Ensures the return date is after the pickup date
        if start_date and end_date and end_date < start_date:
            self.add_error('end_date', "The return date must be after the pickup date.")
        
        return cleaned_data