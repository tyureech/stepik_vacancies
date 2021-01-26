from vacancies.models import Company
from django import forms


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count')
