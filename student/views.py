from django.shortcuts import render ,redirect
from django.core.management import call_command
from django.contrib import messages


def home(request):
    return render(request, 'student/home.html')

# Create your views here.
def import_students(request):
    if request.method == 'POST':
        try:
            call_command('ImportStudent')
            messages.success(request, 'Successfully imported students.')
        except Exception as e:
            messages.error(request, f'Error importing students: {e}')
        return redirect('/')
    else:
        return redirect('/')