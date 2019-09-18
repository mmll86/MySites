from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# 1) Menu Hot:
class MenuKitchenHot(models.Model):
	title_hot = models.CharField('Название', max_length=50, db_index=True)
	text_hot = models.TextField('Описание')
	weight_hot = models.IntegerField('Вес')
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

# 2) Бронирование

class Reservation(models.Model):
	first_name = models.CharField('Имя', max_length=20)
	last_name = models.CharField('Фамилия',max_length=20)
	number_phone = models.CharField('Номер телефона', max_length=12)
	email = models.CharField('E-email', max_length=20)
	date_reservation = models.DateField('Дата бронирования')
	time_reservation = models.TimeField('Время бронирования')
	number_persone = models.IntegerField('Количество персон')

	class Meta:
		verbose_name = 'Персона'
		verbose_name_plural = 'Персоны'

	def __str__(self):
		return self.first_name