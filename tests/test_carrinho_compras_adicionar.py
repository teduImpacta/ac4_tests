"""Carrinho de compras feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from pytest import fixture

from app.carrinho_compras import CarrinhoCompras


@fixture
def carrinho():
    return CarrinhoCompras()


@scenario('../features/carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""


@given('que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99')
def camiseta_no_carrinho(carrinho):
    """que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99."""
    carrinho.adicionar_item("Camiseta", 29.99)


@when('eu adiciono o item "Calça" com o preço R$ 49.99')
def adicionar_calca_no_carrinho(carrinho):
    """eu adiciono o item "Calça" com o preço R$ 49.99."""
    carrinho.adicionar_item("Calça", 49.99)


@then('o total do carrnho de compras deve ser R$ 79.98')
def total_do_carrinho(carrinho):
    """o total do carrnho de compras deve ser R$ 79.98."""
    assert carrinho.total() == 79.98
