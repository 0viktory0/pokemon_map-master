from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название на русском")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Название на английском")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Название на китайском")
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(
        null=True,
        verbose_name="Изображение"
    )
    previous_evolution = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolution',
        verbose_name="Эволюция покемона"
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='entities',
        verbose_name="Покемон"
    )
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Дата и время появления")
    disappeared_at = models.DateTimeField(verbose_name="Дата и время исчезновения")
    level = models.IntegerField(null=True, blank=True, verbose_name="Уровень")
    health = models.IntegerField(null=True, blank=True, verbose_name="Здоровье")
    strength = models.IntegerField(null=True, blank=True, verbose_name="Сила")
    defence = models.IntegerField(null=True, blank=True, verbose_name="Защита")
    stamina = models.IntegerField(null=True, blank=True, verbose_name="Выносливость")

    def __str__(self):
        return f"{self.pokemon.title} {self.lat} {self.lon}"