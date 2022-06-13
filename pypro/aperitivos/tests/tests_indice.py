import pytest
from django.urls import reverse

# Create your tests here.
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))

def test_status_code(resp):
    assert resp.status_code==200
@pytest.mark.parametrize(
    'titulo',[
"Video Aperitivo: Motivação",
"Programação Orientada a Objetos - Com Luciano Ramalho"
    ]
)
def test_titulo_video(resp,titulo):
    assert_contains(resp,'Video Aperitivo: Motivação')
#
# def test_conteudo_video(resp):
#     assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/_UfhOwkwXZ4"')
