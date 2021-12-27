from rest_framework.serializers import ModelSerializer
from apps.ota_api.models import Device, Firmware


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ['mac_addr', 'nome', 'observacoes', 'firmware']


class FirmwareSerializer(ModelSerializer):
    class Meta:
        model = Firmware
        fields = ['firmware', 'version', 'comentarios', 'received_data']