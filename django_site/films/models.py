from django.db import models

from django.urls import reverse


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    year = models.CharField(max_length=5, verbose_name="Год выпуска")
    grade = models.CharField(max_length=10, verbose_name="Оценка")
    watched = models.DateTimeField(null=True, verbose_name="Когда посмотрел")
    comments= models.TextField(verbose_name="Коментарии", blank=True)

    cast = models.ManyToManyField("CastMember", blank=True, verbose_name="Cast")
    genres = models.ManyToManyField("Genre", blank=True, verbose_name="Жанр")
    
    # Для сортировки + комментарии к каждому выбору (если выбран)
    is_top = models.BooleanField(default=False, verbose_name="Top?")
    is_sound = models.BooleanField(default=False, verbose_name="Отличительный Звук?")
    sound_comments = models.CharField(max_length=250, blank=True, verbose_name="Есть что сказать об Звуке?")
    is_beauty = models.BooleanField(verbose_name="Красиво?")
    beauty_comments = models.CharField(max_length=250, blank=True, verbose_name="Комментарии по картинке")
    is_adult = models.BooleanField(verbose_name="Adult?")
    adult_comments = models.CharField(max_length=250, blank=True, verbose_name="Комментарии к Adult")
    is_rewatch = models.BooleanField(verbose_name="Можно пересматривать?")
    rewatch_comments = models.CharField(max_length=250, blank=True, verbose_name="Комментарии к пересмотру")

    movie_poster = models.ImageField(upload_to=r"movies/photos/%Y/%m/%d/", blank=True, verbose_name="Постер")

    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["-watched"]


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название жанра")
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("genre", args=[self.slug])

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


# Need autocreate in movie page
class CastMember(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    born = models.DateField(blank=True, verbose_name="Дата рождения")
    favorite = models.BooleanField(default=False, verbose_name="Буду следить?")
    votes = models.IntegerField(default=0, verbose_name="Сколько раз проголосовали")

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('cast-member', args=[self.slug])

    class Meta:
        verbose_name = "Cast Member"
        verbose_name_plural = "Cast Members"


    

# Нужно делать blank для Ключей иначе на этапе создания записи о фильме невозможно создать корректный CastMemberComment (movie еще банально не существует)
# ИЛИ
# Создавать запись фильма в несколько этапов
class CastMemberComment(models.Model):
    # У одного комментария - один фильм, у одного фильма много комментариев
    cast_member = models.ForeignKey("CastMember", null=True, on_delete=models.SET_NULL, verbose_name="Участник")
    movie = models.ForeignKey("Movie", null=True, on_delete=models.SET_NULL, verbose_name="Фильм")
    comment = models.CharField(max_length=250, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.cast_member} in '{self.movie}'"
    
    class Meta:
        verbose_name = "Cast Member Comment"
        verbose_name_plural = "Cast Member Comments"

