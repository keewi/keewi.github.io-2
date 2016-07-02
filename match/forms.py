from django import forms
from .models import Student

class ApplyForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['user_id',
				  'first_name',
				  'last_name',
				  'is_mentor',
				  'grad_year',
				  'is_avail',
				  'rel_interest',
				  ]

			# 'First Name', 
			# 	  'Last Name',
			# 	  'Computing ID',
			# 	  'University',
			# 	  'Student Status',
			# 	  'Graduation Year',
			# 	  'How available are you over the summer?',
			# 	  'What are you interested in getting out of the program?',)