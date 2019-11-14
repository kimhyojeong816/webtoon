from django.db import models

# Create your models here.
class WebToon(models.Model):
    webtoon_id=models.CharField(max_length=100,primary_key=True)
    site_name=models.CharField(max_length=50)
    webtoon_name=models.CharField(max_length=200)
    webtoon_author=models.CharField(max_length=100)
    webtoon_img_url=models.CharField(max_length=300)

    def __str__(self):
        return self.site_name+":"+self.webtoon_name