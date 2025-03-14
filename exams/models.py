from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class ExamTypeEnum(models.TextChoices):
    MRI = "MRI", "MRI"
    EEG = "EEG", "EEG"
    MI_RNA = "MI_RNA", "miRNA"
    NEUROPSYCHOLOGICAL_EVALUATION = (
        "NEUROPSYCHOLOGICAL_EVALUATION",
        "Neuropsychological Evaluation",
    )


class Exam(models.Model):
    exam_type = models.CharField(
        max_length=50, choices=ExamTypeEnum.choices, default=None
    )
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    exam_path = models.TextField()
    exam_results_path = models.TextField()

    def __str__(self):
        return (
            self.exam_type
            + " "
            + str(self.date)
            + " "
            + self.patient.name
            + " "
            + self.doctor.name
        )
