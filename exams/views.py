from django.core import serializers
from django.http import HttpResponse
import exams.logic.exams_logic as exams_logic
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def exams_view(request):
    if request.method == "GET":
        exams = exams_logic.get_exams()
        exams_dto = serializers.serialize("json", exams)
        return HttpResponse(exams_dto, 'application/json')

@csrf_exempt
def exam_view(request, pk):
    if request.method == "GET":
        exam = exams_logic.get_exam(pk)
        exam_dto = serializers.serialize("json", [exam])
        return HttpResponse(exam_dto, 'application/json')
