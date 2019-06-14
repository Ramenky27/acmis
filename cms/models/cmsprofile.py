from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.utils.encoding import force_text
from django.dispatch import receiver
from django.conf import settings
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User, Group
from cms.utils import PathAndRename

class CmsProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    avatar = models.ImageField(upload_to=PathAndRename('avatars/'), blank=True, null=True, verbose_name=_("Аватар"))
    birth_date = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Дата рождения"))
    location = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Местоположение"))

    facebook = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Facebook"))
    vk = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Vkontakte"))
    instagram = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Instagram"))
    twitter = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Twitter"))
    youtube = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("YouTube"))

    telegram = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Telegram"))
    skype = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("Skype"))
    last_activity = models.DateTimeField(null=True, blank=True, verbose_name=_("Был в сети"))

    email_change_token = models.CharField(max_length=42, verbose_name=_("Код подтверждения смены e-mail"))
    new_email = models.CharField(max_length=256, verbose_name=_("Новый e-mail"))

    @property
    def avatar_url(self):
        try:
            return self.avatar.url
        except:
            return getattr(settings, 'STATIC_URL', '') + 'images/no_avatar.png'

    @property
    def online(self):
        if self.last_activity:
            now = timezone.now()
            if now < self.last_activity + timezone.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
                return True

        return False

    def get_display_name(self):
        try:
            if hasattr(self, 'user'):  # we have OneToOne foreign key to user model
                return self.user.get_username()
        except Exception:
            return force_text(self)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})

    class Meta:
      verbose_name = _("Профиль пользователя")
      verbose_name_plural = _("Профили пользователей")

    @receiver(post_save, sender=User)
    def add_to_default_group(sender, instance, created, **kwargs):
        if created and not instance.is_superuser:
            group = Group.objects.get(name=settings.DEFAULT_REGISTRATION_GROUP)
            instance.groups.add(group)