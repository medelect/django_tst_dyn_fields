from __future__ import unicode_literals

from django.db import models


class TestTab(models.Model):
    name = models.CharField(max_length=20)
    numb = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.name, self.numb)

