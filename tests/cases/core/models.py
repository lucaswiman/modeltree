from django.db import models


class NonUniqueModelName(models.Model):
    meeting = models.ForeignKey('tests.Meeting')


class DisconnectedNonUniqueModelName(models.Model):
    meeting = models.ForeignKey('tests.Meeting', related_name='+')
