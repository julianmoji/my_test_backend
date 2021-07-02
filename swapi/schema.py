import graphene

from app.schema import Query as sw_query, Mutation as sw_mutation


class Query(sw_query):
    pass


class Mutation(sw_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

# def test_query():
#     result = schema.execute(query)
#     assert not result.errors
#     assert result.data == {"patron": {"id": "1", "name": "Syrus", "age": 27}}
