from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from mangas.schema import schema
from mangas.models import Manga


LINKS_QUERY = '''
    {
    mangas {
        titulomanga
        generomanga
        descripcionmanga
        preciomanga
        escritormanga
        volumenesmanga
        capitulosmanga
        ilustradormanga
        editorialmanga
        clasificacionedadmanga
        }
    }
'''

CREATE_MANGA_MUTATION = '''
mutation createMangaMutation($titulomanga: String, $generomanga: String, $descripcionmanga: String, $preciomanga: Int, $escritormanga: String, $volumenesmanga: Int, $capitulosmanga: Int, $ilustradormanga: String, $editorialmanga: String, $clasificacionedadmanga: Int ){
    createManga(titulomanga: $titulomanga, generomanga: $generomanga, descripcionmanga: $descripcionmanga,  preciomanga: $preciomanga,  escritormanga: $escritormanga,  volumenesmanga: $volumenesmanga,  capitulosmanga: $capitulosmanga,  ilustradormanga: $ilustradormanga,  editorialmanga: $editorialmanga, clasificacionedadmanga: $clasificacionedadmanga){
        titulomanga
 }
}
'''

class MangaTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        self.manga1 = mixer.blend(Manga)

    def test_mangas_query(self):
        response = self.query(
            LINKS_QUERY,
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        print(content)
        assert len(content['data']) == 1

    def test_createManga_mutation(self):
        response = self.query(
            CREATE_MANGA_MUTATION,
            variables={
                'titulomanga': 'Quintillizas', 
                'generomanga': 'Romance', 
                'descripcionmanga': 'Comedia Romantica', 
                'preciomanga': 0, 
                'escritormanga': 'Hirohito', 
                'volumenesmanga': 3, 
                'capitulosmanga': 250, 
                'ilustradormanga': 'Yamaguchi', 
                'editorialmanga': 'Panini', 
                'clasificacionedadmanga': 18
            }
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual(
            {
                "createManga": {
                    "titulomanga": "Quintillizas"
                }
            }, 
            content['data']
        )
