from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# 1) Menu Hot:
class MenuKitchenHot(models.Model):
	title_hot = models.CharField('Название', max_length=50, db_index=True)
	text_hot = models.TextField('Описание')
	weight_hot = models.IntegerField('Вес', max_length=10)
	price_hot = models.IntegerField('Цена')
	image_hot = models.ImageField('Картинка', upload_to='hot')
	date_hot_add = models.DateTimeField('Дата добавления', auto_now_add=True)
	slug_hot = models.SlugField('Слаг', unique=True, allow_unicode=True)


	class Meta:
		verbose_name = 'Горячее'
		verbose_name_plural = 'Горячее'

	def __str__(self):
		return self.title_hot

	# def save(self, *args, **kwargs):
	# 	self.slug_hot = slugify(self.title_hot)
	# 	super(MenuKitchenHot, self).save(*args, **kwargs)