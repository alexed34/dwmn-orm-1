from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.all()
    non_closed_visits = []
    for visit in visits:
        if not visit.leaved_at:
            non_closed_visits.append(Visit.format_duration(visit))
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
