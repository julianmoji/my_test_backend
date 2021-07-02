import graphene
from graphene_django.types import DjangoObjectType

from .models import Planet, People, Film, Director, Producer


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        interfaces = (graphene.relay.Node,)
        filter_fields = {'name': ['iexact', 'icontains', 'contains', 'exact'], }


class PeopleType(DjangoObjectType):
    gender = graphene.Enum('PeopleGenderEnum', People.GENDER)

    class Meta:
        model = People
        interfaces = (graphene.relay.Node,)
        filter_fields = {'name': ['iexact', 'icontains', 'contains', 'exact'], 'gender': ['exact']}
        convert_choices_to_enum = False


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director
        interfaces = (graphene.relay.Node,)
        filter_fields = ['name']


class ProducerType(DjangoObjectType):
    class Meta:
        model = Producer
        interfaces = (graphene.relay.Node,)
        filter_fields = ['name']


class FilmType(DjangoObjectType):
    # TODO: Agregar choices para el episode_id
    class Meta:
        model = Film
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'title': ['iexact', 'icontains', 'contains', 'exact'],
            'episode_id': ['exact'],
            'release_date': ['exact']
        }
