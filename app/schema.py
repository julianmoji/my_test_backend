import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .enums import GenderEnum
from .models import People
from .mutations import CreateOrUpdatePlanet, CreatePeople, UpdatePeople
from .types import PlanetType, PeopleType, FilmType, DirectorType, ProducerType


class Query(graphene.ObjectType):
    planet = graphene.relay.Node.Field(PlanetType)
    all_planets = DjangoFilterConnectionField(PlanetType)

    people = graphene.relay.Node.Field(PeopleType)
    all_people = DjangoFilterConnectionField(PeopleType, gender_enum=GenderEnum())

    def resolve_all_people(self, info, **kwargs):
        if 'gender_enum' in kwargs:
            kwargs['gender'] = kwargs['gender_enum']
            del kwargs['gender_enum']
        return People.objects.filter(**kwargs)

    film = graphene.relay.Node.Field(FilmType)
    all_films = DjangoFilterConnectionField(FilmType)

    director = graphene.relay.Node.Field(DirectorType)
    all_directors = DjangoFilterConnectionField(DirectorType)

    producer = graphene.relay.Node.Field(ProducerType)
    all_producers = DjangoFilterConnectionField(ProducerType)


class Mutation(graphene.ObjectType):
    create_or_update_planet = CreateOrUpdatePlanet.Field()
    create_people = CreatePeople.Field()
    update_people = UpdatePeople.Field()
