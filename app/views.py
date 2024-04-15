from django.shortcuts import render
import datetime
# Create your views here.
def View_info(request):
    date=datetime.datetime.now()
    course_name='Pyhton'
    prerequities='PYTHON'
    d={'date':date,'course_name':course_name,'prerequities':prerequities}
    return render(request,'result.html',d)