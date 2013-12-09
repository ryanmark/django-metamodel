from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from UserDict import DictMixin


class MetaManager(models.Manager, DictMixin):
    """
    A related model manager for meta models. Allows you to treat
    the `user.meta` attribute like a dictionary.
    """
    use_for_related_fields = True
    cache_prefix = 'foo'

    def __init__(self, *args, **kwargs):
        #self.cache_prefix = self.model._meta.db_table

        return super(MetaManager, self).__init__(*args, **kwargs)

    def __getitem__(self, key):
        ret = cache.get(self._makekey(key))
        if ret:
            return ret
        try:
            item = self.get(key=key)
            cache.set(self._makekey(key), item.value)
            return item.value
        except ObjectDoesNotExist:
            return None

    def __setitem__(self, key, value):
        item, created = self.get_or_create(
            key=key, defaults={'value': value})
        if not created and item.value != value:
            item.value = value
            item.save()
        cache.set(self._makekey(key), value)

    def __delitem__(self, key):
        try:
            item = self.get(key=key)
            item.delete()
            cache.delete(self._makekey(key))
        except ObjectDoesNotExist:
            pass

    def __contains__(self, key):
        items = self.filter(key=key).count()
        if items > 0:
            return True
        return False

    def __iter__(self):
        items = self.all()
        for i in items:
            yield (i.key, i.value)

    def keys(self):
        return self.all().values_list('key', flat=True)

    def _makekey(self, *args):
        return '_'.join([self.cache_prefix, self.instance.pk] + args)


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
