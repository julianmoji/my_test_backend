import graphene
from graphql_relay import from_global_id

from .models import Planet, People, Film
from .types import PlanetType, PeopleType, FilmType
from .utils import generic_model_mutation_process, clean_global_ids


class CreateOrUpdatePlanet(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return CreateOrUpdatePlanet(planet=planet)


class FilmInput(graphene.InputObjectType):
    id = graphene.GlobalID(parent_type=FilmType)


class CreatePeople(graphene.relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String
        birth_year = graphene.String()
        films = graphene.List(of_type=FilmInput, required=False)
        home_world_id = graphene.GlobalID(parent_type=PlanetType)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        home_world_id = input.get('home_world_id', None)
        films = input.pop('films', [])
        data = input
        if home_world_id:
            data['home_world_id'] = from_global_id(home_world_id)[1]

        people = generic_model_mutation_process(People, data)

        films_ids = []
        for film in films:
            films_ids.append(from_global_id(film['id'])[1])

        films = Film.objects.filter(id__in=films_ids)
        people.films.add(*films)
        return CreatePeople(people=people)


class UpdatePeople(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.GlobalID(parent_type=PeopleType)
        name = graphene.String()
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String
        birth_year = graphene.String()
        home_world_id = graphene.GlobalID(parent_type=PlanetType, required=False)
        gender = graphene.String()

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        input = clean_global_ids(input)
        id = input.pop('id')
        # Todo: Cuando el id sea convertido debe validarse que sea del Type esperado
        people = generic_model_mutation_process(People, input, id=id)
        return UpdatePeople(people=people)
