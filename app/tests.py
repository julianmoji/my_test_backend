import json

from graphene_django.utils.testing import GraphQLTestCase

from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)

    def test_create_people_mutation(self):
        input_data = {
            "name": "soy como la decima persona con peliculas",
            "homeWorldId": "UGxhbmV0VHlwZTox",
            "films": [
                {
                    "id": "RmlsbVR5cGU6MQ=="
                },
                {
                    "id": "RmlsbVR5cGU6Mg=="
                }
            ]
        }
        response = self.query(
            '''
            mutation createPeople($input: CreatePeopleInput!) {
              createPeople(input: $input) {
                people {
                  name
                  films {
                    edges {
                      node {
                        title
                      }
                    }
                  }
                }
              }
            }
            ''',
            op_name='createPeople',
            input_data=input_data
        )
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(len(content['data']['createPeople']['people']['films']['edges']), len(input_data['films']))

    def test_update_people_mutation(self):
        input_data = {
            "id": "UGVvcGxlVHlwZToy",
            "name": "Esta es una actualizacion",
            "hairColor": "euk",
            "mass": "1200"

        }
        response = self.query(
            '''
            mutation updatePeople($input:UpdatePeopleInput!){
                 updatePeople(input:$input){
                   people{
                     id
                     name
                     hairColor
                     mass
                   }
                 }
               }
           ''',
            op_name='updatePeople',
            input_data=input_data
        )

        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        print('content \n', content)
        for key, value in input_data.items():
            self.assertEqual(value, content['data']['updatePeople']['people'][key])
