from django.db import models

DURATION_CHOICES = {
    (0.5, "short"),
    (1, "normal"),
    (1.5, "long"),
    (2, "longer"),
}


class djangoClasses(models.Model):
    courseNumber = models.IntegerField(verbose_name="Course Number", null=False,)
    title = models.CharField(max_length=60, verbose_name="Course", null=False)
    instructorName = models.CharField(
        max_length=80,
        db_column="Instructor's Name",
        verbose_name="Instructor's Name",
        default="",
        null=False,
    )
    duration = models.FloatField(
        db_column="Class Duration",
        verbose_name="Course Duration",
        help_text="Pick short for .5 hours, normal for 1 "
        "hour, long for 1.5 hours,or longer for "
        "2 hours.",
        choices=DURATION_CHOICES,
    )

    objects = models.Manager()

    def __str__(self):
        return self.title


class1 = djangoClasses(
    courseNumber=201,
    title="Underwater Basket Weaving",
    instructorName="Mr. Magoo",
    duration=2.0,
)
class1.save()

class2 = djangoClasses(
    courseNumber=317,
    title="Inverted Speed Reading",
    instructorName="Ms. Smith",
    duration=0.5,
)
class2.save()

class3 = djangoClasses(
    courseNumber=512,
    title="Chemical Explosions & Safety",
    instructorName="Mr. Heisenberg",
    duration=1.5,
)
class3.save()
