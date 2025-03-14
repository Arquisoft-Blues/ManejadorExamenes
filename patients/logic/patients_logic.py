from exams.models import Exam


def get_exams_by_patient(patient_id):
    return Exam.objects.filter(patient_id=patient_id)
