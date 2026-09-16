from django.db import models

class Exam(models.Model):
    class Subject(models.IntegerChoices):
        MATH = 0, "Matemáticas"
        LCL = 1, "Castelán"
        LGL = 2, "Galego"
        HIST = 3, "Historia de España"
        FILO = 4, "Historia da Filosofía"
        ING = 5, "Inglés"
        FIS = 6, "Física"
        QUIM = 7, "Químca"
        BIO = 8, "Bioloxía"
        TEC = 9, "Tecnoloxía"
        DIB = 10, "Debuxo Técnico"
        MEN = 11, "Métodos"
        PSI = 12, "Psicoloxía"
        FRA = 13, "Francés"

    class Periods(models.IntegerChoices):
        H1 = 1, "1ª hora"
        H2 = 2, "2ª hora"
        H3 = 3, "3ª hora"
        H4 = 4, "4ª hora"
        H5 = 5, "5ª hora"
        H6 = 6, "6ª hora"
        H7 = 7, "7ª hora"
        T = 8, "Pola tarde"

    subject = models.IntegerField(choices=Subject)
    name = models.CharField(max_length=100)
    date = models.DateField()
    period = models.IntegerField(choices=Subject)
    isConfirmed = models.BooleanField(default=True)
