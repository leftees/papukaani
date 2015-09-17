from django.test import TestCase
from django.test import Client
from papukaaniApp.models import *
from datetime import datetime

class TestChoose(TestCase):

    def setUp(self):
        self.c = Client()
        self. creature = Creature.objects.create(name="Creature")
        self.A = MapPoint.objects.create(
            creature = self.creature,
            latitude = 22.22,
            longitude = 22.22,
            altitude = 222.22,
            temperature = 22.2,
            timestamp = datetime.now(),
        )
        self.B = MapPoint.objects.create(
            creature = self.creature,
            latitude = 11.22,
            longitude = 11.22,
            altitude = 111.22,
            temperature = 11.2,
            timestamp = datetime.now()
        )


    def test(self):
        Aid = self.A.id
        Bid = self.B.id
        response = self.c.post('/papukaani/choose/', {'data' : '[{"id" : '+str(Aid)+', "public" : 1},{"id" : '+str(Bid)+', "public" : 0}]'})

        self.A = MapPoint.objects.get(id=Aid)
        self.B = MapPoint.objects.get(id=Bid)

        self.assertTrue(self.A.public)
        self.assertFalse(self.B.public)



