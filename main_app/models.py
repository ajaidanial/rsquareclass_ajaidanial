from django.db import models


class Year(models.Model):
    """
    Model to denote the academic years.
    Example:
        2019-2020
    """

    from_year = models.PositiveIntegerField()
    to_year = models.PositiveIntegerField()

    def get_academic_year(self):
        # to return the full year name
        return f"${self.from_year} - ${self.to_year}"

    def __str__(self):
        return self.get_academic_year


class Group(models.Model):
    """
    Model to denote the classes and groups.
    Example:
        11th Science
    """

    standard = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    def get_academic_group(self):
        # to return the full group name and standard
        return f"${self.standard} ${self.name}"

    def __str__(self):
        return self.get_academic_group


class Subject(models.Model):
    """
    Model to denote the subject under the classes and groups.
    Example:
        Physics for 10th Science
    """

    name = models.CharField(max_length=50)
    group = models.ForeignKey(to=Group, related_name="subjects")

    def get_academic_subject(self):
        # to return the full subject name
        return f"${self.name} ${self.group}"

    def __str__(self):
        return self.get_academic_subject
