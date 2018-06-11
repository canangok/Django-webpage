from django.db import models
from django.utils.translation import gettext as _
from PIL import Image

class Hackathon(models.Model):
    icon = models.ImageField(_('hackathon ikonu'))
    main_image = models.ImageField(_('hackathon resmi'))
    background_image=models.ImageField(_('hackathon arkaplan resmi'), null=True, blank=True)
    sponsors_background_image = models.ImageField(_('Sponsorlar Arka Planı'),null=True, blank=True)
    committee_background_image = models.ImageField(_('Jüriler Arkaplan Resmi'),null=True, blank=True)
    footer_background_image = models.ImageField(_('Footer Arkaplan Resmi'),null=True, blank=True)
    footer_title=models.CharField(_('Footer Başlık'),max_length=255,blank=True,null=True)
    footer_social_facebook = models.CharField(_('Facebook link'),max_length=255,blank=True,null=True)
    footer_social_twitter = models.CharField(_('Twitter link'),max_length=255,blank=True,null=True)
    color = models.CharField(_('Menü Arkaplan Rengi'), max_length=6,blank=True)
    title = models.CharField(_('Başlık'),max_length=255)
    slogan = models.CharField(_('Slogan'),max_length=255)
    date = models.CharField(_('Tarih'),max_length=255)
    starting_date=models.DateTimeField(_('Başlangıç Tarihi'),blank=True,null=True)
    place = models.CharField(_('Yer'),max_length=255)
    description = models.TextField(_('Açıklama'))
    address = models.TextField(_('Adres'))
    directions = models.TextField(_('Yol Tarifi'),blank=True,null=True)
    email = models.EmailField(_('E-posta'), unique=False, null=False, blank=False)
    phone = models.CharField(_('Telefon'), max_length=20, default='', blank=True)
    latitude = models.DecimalField(_('Enlem'), max_digits=19, decimal_places=10,blank=True,null=True)
    longitude = models.DecimalField(_('Boylam'), max_digits=19, decimal_places=10, blank=True,null=True)
    form_active = models.BooleanField(_('Form aktifliği'),default=True)
    active = models.BooleanField(_('Active'))

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Hackathon'
        verbose_name_plural = 'Hackathonlar'


class Navigation(models.Model):
    name = models.CharField(_('Menü ismi'),max_length=255)
    order = models.CharField(_('Sırası'), max_length=10, default='', blank=True)
    hackathon = models.ForeignKey(Hackathon, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Menü'
        verbose_name_plural = 'Menüler'


class Sponsors(models.Model):
    icon = models.ImageField(_('sponsor ikonu'))
    name = models.CharField(_('Sponsor ismi'),max_length=255)
    description = models.TextField(_('Sponsor açıklama'))
    hackathon = models.ForeignKey(Hackathon, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsorlar'


class Prize(models.Model):
    name = models.CharField(_('Ödül ismi'), max_length=255)
    order = models.CharField(_('Ödül Sırası'), max_length=3, default='', blank=True)
    icon = models.ImageField(_('Ödül ikonu'))
    hackathon = models.ForeignKey(Hackathon, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Ödül'
        verbose_name_plural = 'Ödüller'


class Program(models.Model):
    day = models.IntegerField(choices=((1, _("1. Gün")), (2, _("2. Gün")), (3, _("3. Gün"))), default=1)
    time_interval = models.CharField(_('Zaman aralığı'), max_length=255)
    order = models.CharField(_('Sırası'), max_length=10, default='', blank=True)
    title = models.CharField(_('Başlık'), max_length=255)
    hackathon = models.ForeignKey(Hackathon, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programlar'


class Committee(models.Model):
    name = models.CharField(_('Kişi ismi'), max_length=255)
    title = models.CharField(_('Ünvanı'), max_length=255)
    business = models.CharField(_('Firma/Şirket'), max_length=255)
    mentor = models.BooleanField(_('Mentor'), default=False)
    jury = models.BooleanField(_('Juri'), default=False)
    linkedin_link = models.CharField(_('Linkedin link'),max_length=255,blank=True,null=True)
    twitter_link = models.CharField(_('Twitter link'),max_length=255,blank=True,null=True)
    avatar = models.ImageField(_('Fotoğraf (370x370)'), width_field='width', height_field='height')
    height = models.PositiveIntegerField(
        'Image Height (370)',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width (370)',
        blank=True,
        null=True
    )
    hackathon = models.ForeignKey(Hackathon, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)

    def save(self):

        if not self.avatar:
            return

        self.avatar.open()
        image = Image.open(self.avatar)
        (width, height) = image.size
        size = (370, 370)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.avatar.path)
        super(Committee, self).save()

    class Meta:
        verbose_name = 'Juri ve Mentor'
        verbose_name_plural = 'Juriler ve Mentorler'


class Sss(models.Model):
    question = models.TextField(_('Soru'))
    answer = models.TextField(_('Cevap'))
    order = models.CharField(_('Soru sırası'), max_length=10, default='', blank=True)
    hackathon = models.ForeignKey(Hackathon, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.question)

    class Meta:
        verbose_name = 'Sık Sorulan Soru'
        verbose_name_plural = 'Sık Sorulan Sorular'
