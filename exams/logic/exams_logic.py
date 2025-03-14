from ..models import Exam


def get_exams():
    return Exam.objects.all()


def get_exam(exam_pk):
    return Exam.objects.get(pk=exam_pk)
