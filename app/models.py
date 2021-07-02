from django.db import models
from model_utils.models import TimeStampedModel


class SimpleNameModel(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Planet(TimeStampedModel, SimpleNameModel):
    """ Planetas del universo de Star Wars """

    rotation_period = models.CharField(max_length=40, blank=True)
    orbital_period = models.CharField(max_length=40, blank=True)
    diameter = models.CharField(max_length=40, blank=True)
    climate = models.CharField(max_length=40, blank=True)
    gravity = models.CharField(max_length=40, blank=True)
    terrain = models.CharField(max_length=40, blank=True)
    surface_water = models.CharField(max_length=40, blank=True)
    population = models.CharField(max_length=40, blank=True)

    class Meta:
        db_table = 'planet'


class People(TimeStampedModel, SimpleNameModel):
    """ Personajes del universo de Star Wars """
    MALE = 'male'
    FEMALE = 'female'
    HERMAPHRODITE = 'hermaphrodite'
    NA = 'n/a'

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (HERMAPHRODITE, 'Hermaphrodite'),
        (NA, 'N/A'),
    )

    BLACK = 'bc'
    BROWN = 'br'
    BLOND = 'bl'
    RED = 'rd'
    WHITE = 'wh'
    BALD = 'bd'
    HAIR_COLOR = (
        (BLACK, 'Negro'),
        (BROWN, 'Café'),
        (BLOND, 'Rubio'),
        (RED, 'Rojo'),
        (WHITE, 'Blanco'),
        (BALD, 'Calvo')
    )

    BLACK_EYE = 'ebc'
    BROWN_EYE = 'ebr'
    YELLOW_EYE = 'eyl'
    RED_EYE = 'erd'
    GREEN_EYE = 'egr'
    PURPLE_EYE = 'epu'
    UNKNOWN = 'euk'
    EYE_COLOR = (
        (BLACK_EYE, 'Negro'),
        (BROWN_EYE, 'Café'),
        (YELLOW_EYE, 'Amarillo'),
        (RED_EYE, 'Rojo'),
        (GREEN_EYE, 'Verde'),
        (PURPLE_EYE, 'Morado'),
        (UNKNOWN, 'Desconocido')
    )
    height = models.CharField(max_length=16, blank=True)
    mass = models.CharField(max_length=16, blank=True)
    hair_color = models.CharField(max_length=32, blank=True, choices=HAIR_COLOR)
    skin_color = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(max_length=32, blank=True, choices=EYE_COLOR)
    birth_year = models.CharField(max_length=16, blank=True)
    gender = models.CharField(max_length=64, choices=GENDER)
    home_world = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='inhabitants')

    class Meta:
        db_table = 'people'
        verbose_name_plural = 'people'


class Director(SimpleNameModel):
    """ Directores de películas"""

    class Meta:
        db_table = 'director'


class Producer(SimpleNameModel):
    """ Productores de películas"""

    class Meta:
        db_table = 'producer'


class Film(TimeStampedModel):
    title = models.CharField(max_length=100)
    episode_id = models.PositiveSmallIntegerField()  # TODO: Agregar choices
    opening_crawl = models.TextField(max_length=1000)
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='films')
    producer = models.ManyToManyField(Producer, related_name='films')
    characters = models.ManyToManyField(People, related_name='films', blank=True)
    planets = models.ManyToManyField(Planet, related_name='films', blank=True)

    class Meta:
        db_table = 'film'

    def __str__(self):
        return self.title
