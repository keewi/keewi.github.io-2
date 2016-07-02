from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import University, Student
from .forms import ApplyForm

# Create your views here.
def student_list(request):
	students = Student.objects.all()
	return render(request, 'match/student_list.html', {'students':students})

def apply(request):
	if request.method == "POST":
		form = ApplyForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.university_id = University.objects.get(short_name='CMU')
			student.created_date = timezone.now()

			student.save()
			return redirect('student_list')
	else:
		form = ApplyForm()
	return render(request, 'match/apply.html', {'form':form})
