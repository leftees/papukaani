from papukaaniApp.models import *
from papukaaniApp.utils.parser import ecotones_parse
from django.shortcuts import render
from papukaaniApp.utils.view_utils import *
import json


def upload(request):
    """
    Controller for '/upload/'. GET shows upload screen, POST uploads file.
    Point data is parsed from file and saved to database.
    Point data for Leaflet returned in response.
    """
    if request.method == 'GET':
        return _render_with_message(request)
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            try:
                data = ecotones_parse(file)
            except:
                return redirect_with_param(upload, "?m=Tiedostosi formaatti ei ole kelvollinen!")

            points = _create_points(data)
            return _render_points(points, request)

        return redirect_with_param(upload, "?m=Et valinnut ladattavaa tiedostoa!")


def _render_points(points, request):
    latlongs = extract_latlongs(points)
    return render(request, 'upload.html', {'points': json.dumps(latlongs)})

def _render_with_message(request):
    message = request.GET['m'] if 'm' in request.GET else ''
    return render(request, 'upload.html', {"message": message})


def _create_points(data):
    creature, was_created = Creature.objects.get_or_create(name="Pekka")
    points = [MapPoint(creature=creature, **point) for point in data]
    MapPoint.objects.bulk_create(points)
    return points


