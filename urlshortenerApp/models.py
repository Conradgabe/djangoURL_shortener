from django.db import models

from .utils import generate_uuid

class LinkURL(models.Model):
    original_url = models.URLField(max_length=1000)
    shorten_url = models.CharField(max_length=10, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shorten_url}-{self.id}"

    def save(self, *args, **kwargs):
        if self.shorten_url == "":
            uuid = generate_uuid()
            self.shorten_url = uuid
        pass
        super(LinkURL, self).save(*args, **kwargs)
