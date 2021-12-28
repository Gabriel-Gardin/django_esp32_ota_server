from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from django.conf import settings

from .serializer import DeviceSerializer, FirmwareSerializer
from apps.ota_api.models import Device, Firmware


class DeviceViewSet(ModelViewSet):
    #queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, BasicAuthentication)


    def get_queryset(self):
        return Device.objects.all()

    def retrieve(self, request, *args, **kwargs):
        device_mac = kwargs['pk']
        firmware_name = Device.objects.get(mac_addr = device_mac).firmware
        print("firmware_name", firmware_name)
        firmware_path = settings.MEDIA_ROOT + "/firmwares/firmware_v{}.bin".format(firmware_name)
        print("piedade", firmware_path)

        firmware = open(firmware_path, "rb")
        response = HttpResponse(firmware,content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename=firmware.bin'

        return response



class FirmwareViewSet(ModelViewSet):

    queryset = Firmware.objects.all()
    serializer_class = FirmwareSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, BasicAuthentication)