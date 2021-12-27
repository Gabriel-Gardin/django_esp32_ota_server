from django.db import models


def firmware_file_name(instance, filename):
    return "firmwares/firmware_v{}.bin".format(instance.version)


class Firmware(models.Model):
    firmware = models.FileField(upload_to = firmware_file_name)
    version = models.CharField(max_length=100)
    comentarios = models.CharField(max_length=200)
    received_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.version


class Device(models.Model):
    mac_addr = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=100)
    firmware = models.ForeignKey(Firmware, null=True, on_delete=models.PROTECT) #One to many. 1 firmware pode ter vários devices, mas 1 device só pode ter 1 firmware

    def __str__(self):
        return self.mac_addr