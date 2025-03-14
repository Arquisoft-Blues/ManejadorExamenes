import patients.logic.patients_logic as patients_logic
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def exams_by_patient_view(request, patient_id):
    if request.method == "GET":
        exams = patients_logic.get_exams_by_patient(patient_id)
        exams_dto = serializers.serialize("json", exams)
        return HttpResponse(exams_dto, 'application/json')
