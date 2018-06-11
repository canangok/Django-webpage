from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from PIL import Image

class App(models.Model):
    title=models.CharField(_('Başlık'),max_length=255)
    description=models.CharField(_('Açıklama'),max_length=255)
    website_link=models.CharField(_('Web sitesi linki'),max_length=255)
    appstore_link=models.CharField(_('Appstore linki'),max_length=255)
    playstore_link=models.CharField(_('Playstore linki'),max_length=255)
    icon=models.ImageField(_('İkon'))
    app_image=models.ImageField(_('Uygulama resmi'))
    background_image=models.ImageField(_('Arkaplan resmi'), width_field='width', height_field='height')
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True)
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True)
    active=models.BooleanField(_('Active'), default=True)
    yayinlanma_tarihi = models.DateTimeField(_('Yayınlanma Tarihi'),
           blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return "{}".format(self.title)

    def save(self):

        if not self.background_image:
            return

        self.background_image.open()
        image = Image.open(self.background_image)
        (width, height) = image.size
        size = (400, 400)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.background_image.path)
        super(App, self).save()
