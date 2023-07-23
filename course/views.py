from django.shortcuts import render
from django.views import View

# Create your views here.

class GetCourses(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class GetCourse(View):
    def get(self,request):
        course = {
            id: 1,
            'name': "Test Course 1"
        }
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
            'course': course,
            'holes': holes
        }
        print("In Course Description")
        return render(request, 'course/course_description.html', context)
    
class CreateCourse(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class EditCourse(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class DeleteCourse(View):
    def delete(self, request):
        pass


class PreviewCourse(View):
    def get(self, request):
        pass

class GetHoles(View):
    def get(self, request):
        pass

class GetHole(View):
    def get(self, request, pk, holeId):
        pass

class CreateHole(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
    
class EditHole(View):
    def get(self, request, pk, holeId):
        pass

    def post(self, request):
        pass

class DeleteHole(View):
    def delete(self, request, pk, holeId):
        pass

   