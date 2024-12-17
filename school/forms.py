from django import forms
from .models import CustomUser,FeesHistory
from .models import LibraryHistory
from .models import LibraryRecord
from django.forms import DateInput 

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        label="Password",
        required=False  
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label="Confirm Password",
        required=False  
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password']  

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

     
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        
      
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password']) 
        
        if commit:
            user.save()
        return user

class FeesHistoryForm(forms.ModelForm):
    class Meta:
        model = FeesHistory
        fields = ['student', 'fee_type', 'amount', 'payment_date', 'remarks'] 
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class LibraryHistoryForm(forms.ModelForm):
    class Meta:
        model = LibraryHistory
        fields = ['student', 'book_name', 'borrow_date', 'return_date', 'status']
        widgets = {
            'borrow_date': DateInput(attrs={'type': 'date'}),
            'return_date': DateInput(attrs={'type': 'date'}),
        }
class LibraryHistoryForm(forms.ModelForm):
    class Meta:
        model = LibraryRecord
        fields = ['book_name', 'status']       

class LibraryRecordForm(forms.ModelForm):
    class Meta:
        model = LibraryRecord
        fields = ['book_name', 'status'] 
        widgets = {
            'status': forms.Select(choices=LibraryRecord.STATUS_CHOICES),
        }      