from django.db import models
from django.utils import timezone
import time


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(visit):
        if not visit.leaved_at:
            now = timezone.now()
            visit_time = (now - visit.entered_at).seconds
        else:
            visit_time = (visit.leaved_at - visit.entered_at).seconds
        return visit_time

    def format_duration(visit):
        non_closed_visit = {"who_entered": visit.passcard.owner_name}
        non_closed_visit["entered_at"] = visit.entered_at
        non_closed_visit["duration"] = time.strftime("%H:%M:%S", time.gmtime(Visit.get_duration(visit)))
        non_closed_visit["is_strange"] = Visit.is_visit_long(visit)
        return non_closed_visit

    def is_visit_long(visit, minutes=60):
        visit_time = Visit.get_duration(visit) / 60
        if visit_time > minutes:
            return True
        return False

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
