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
        id
        titulomanga
        generomanga
        descripcionmanga
        lanzamientomanga
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
mutation createMangaMutation($titulomanga: String, $generomanga: String, $descripcionmanga: String, $lanzamientomanga: String, $escritormanga: String, $volumenesmanga: Int, $capitulosmanga: Int, $ilustradormanga: String, $editorialmanga: String, $clasificacionedadmanga: Int ){
    createManga(titulomanga: $titulomanga, generomanga: $generomanga, descripcionmanga: $descripcionmanga,  lanzamientomanga: $lanzamientomanga,  escritormanga: $escritormanga,  volumenesmanga: $volumenesmanga,  capitulosmanga: $capitulosmanga,  ilustradormanga: $ilustradormanga,  editorialmanga: $editorialmanga, clasificacionedadmanga: $clasificacionedadmanga){
    titulomanga
        generomanga
        descripcionmanga
        lanzamientomanga
        escritormanga
        volumenesmanga
        capitulosmanga
        ilustradormanga
        editorialmanga
        clasificacionedadmanga
 }
}
'''

class MangaTestCase(GraphQLTestCase) :
    GRAPHQL_SCHEMA = schema
        
    def setUp(self):
        self.manga1 = mixer.blend(Manga)
        self.manga2 = mixer.blend(Manga)
        
    def test_mangas_query(self):
        response = self.query(
            LINKS_QUERY,
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        print ("query mangas results")
        print (content)
        assert len(content['data']['mangas'])==2
        
    def test_createLink_mutation(self):
        response = self.query(
            CREATE_MANGA_MUTATION,
            variables={'titulomanga': 'Kimi no Todoke!', 'generomanga': 'Romance', 'descripcionmanga': 'Joder claro que si', 'lanzamientomanga': '2002-04-24', 'escritormanga': 'Dios', 'volumenesmanga': 2, 'capitulosmanga': 5, 'ilustradormanga': 'Yo', 'editorialmanga': 'El cielo', 'clasificacionedadmanga': 12}
        )
        print('mutation')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createManga": {"titulomanga": "Kimi no Todoke!",  'generomanga': 'Romance', 'descripcionmanga': 'Joder claro que si', 'lanzamientomanga': '2002-04-24', 'escritormanga': 'Dios', 'volumenesmanga': 2, 'capitulosmanga': 5, 'ilustradormanga': 'Yo', 'editorialmanga': 'El cielo', 'clasificacionedadmanga': 12 }}, content['data'])
                
   

