from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import get_format_duration
from django.shortcuts import render


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in not_leaved:
        duration = get_duration(visit)
        format_duration = get_format_duration(duration)
        entered_at = visit.entered_at
        who_entered = visit.passcard
        non_closed_visit = {
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': format_duration,
        }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
