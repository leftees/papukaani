from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from django.conf import settings
from papukaaniApp.tests.page_models.page_models import UploadPage


class FileUploadSeleniumTest(StaticLiveServerTestCase):
    def setUp(self):
        self.upload = UploadPage()
        self.upload.navigate()

    def tearDown(self):
        self.upload.close()

    def test_selenium_file_can_be_uploaded_and_points_will_be_shown_on_map(self):
        self.upload.upload_file(settings.BASE_DIR + "/papukaaniApp/tests/test_files/ecotones.csv")
        self.assertNotEquals("Tiedostosi formaatti ei ole kelvollinen", self.upload.get_message())
        self.assertNotEquals("Et valinnut ladattavaa tiedostoa", self.upload.get_message())
        self.assertNotEquals(self.upload.get_map_polyline_elements(), None)
