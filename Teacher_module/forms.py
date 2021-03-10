from django import forms
from.models import Student_Notes
Section = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))


class Student_NotesForm(forms.ModelForm):
    Section = forms.ChoiceField(choices=Section, required=True)

    class Meta:
        model = Student_Notes
        fields = ('Semester', 'Branch',  'Subject', 'Notes', 'Description',)
