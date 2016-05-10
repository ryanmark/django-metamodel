from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class MetaManager(models.Manager):
    """
    A related model manager for meta models. Allows you to treat
    the `user.meta` attribute like a dictionary.
    """
    use_for_related_fields = True

    def __getitem__(self, key):
        try:
            item = self.get(key=key)
            return item.value
        except ObjectDoesNotExist:
            return None

    def __setitem__(self, key, value):
        item, created = self.get_or_create(
            key=key, defaults={'value': value})
        if not created and item.value != value:
            item.value = value
            item.save()

    def __delitem__(self, key):
        try:
            item = self.get(key=key)
            item.delete()
        except ObjectDoesNotExist:
            pass

    def __contains__(self, item):
        try:
            item = self.get(key=item)
            return True
        except ObjectDoesNotExist:
            return False


class ModelMeta(models.Model):
    """
    Abstract model for storing key-value metadata. A model would extend
    this and define a foreign key to another model. Metadata are totally
    arbitrary bits of text that describe the model in some way.
    """
    key = models.SlugField(
        help_text="The ID name of this bit of data. Should be only "
        "lowercase numbers and letters, dashes or underscores. No spaces.")
    value = models.TextField(
        help_text="The value, data or code for this item")

    objects = MetaManager()

    def __unicode__(self):
        return unicode(self.value)

    def __str__(self):
        return str(self.value)

    class Meta:
        abstract = True


class UserMeta(ModelMeta):
    """
    Adds a meta data attribute to the builtin user object
    """
    user = models.ForeignKey(User, related_name='meta')

    class Meta:
        unique_together = ('user', 'key')
        verbose_name_plural = "user metadata"
        app_label = 'metamodel'
