from django.shortcuts import render
from django.views import View

# Create your views here.
class CourseDescription(View):
    def get(self,request):
        holes = []
        for i in range(18):
            holes.append({
                'id': i,
                'hole': i+1,
                'par': 3,
                'distance': 400,
                'hazards': [
                    'Water',
                    'Sand Trap'
                ]
            })

        holes[4]['hazards'] = []
        holes[8]['hazards'] = []
        holes[17]['hazards'] = []
        holes[13]['hazards'] = []

        context = {
            'holes': holes
        }
        print("In Course Description")
        return render(request, 'course/course_description.html', context)