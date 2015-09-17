from papukaaniApp.models import *
from papukaaniApp.utils.parser import ecotones_parse
from django.shortcuts import render
from papukaaniApp.utils.view_utils import redirect_with_param


def upload(request):
    if request.method == 'GET':
        message = request.GET['m'] if 'm' in request.GET else ''
        return render(request, 'upload.html', {"message": message})
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            try:
                data = ecotones_parse(file)
            except:
                return redirect_with_param(upload, "?m=Tiedostosi formaatti ei ole kelvollinen!")

            creature, was_created = Creature.objects.get_or_create(name="Pekka")
            points = [MapPoint(creature = creature, **point) for point in data]

            MapPoint.objects.bulk_create(points)

            latlongs = [[mapPoint.latitude, mapPoint.longitude] for mapPoint in points]
            return render(request, 'upload.html', {'points': latlongs})

        return redirect_with_param(upload, "?m=Et valinnut ladattavaa tiedostoa!")

