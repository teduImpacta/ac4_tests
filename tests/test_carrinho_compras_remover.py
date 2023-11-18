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

@scenario('../features/carrinho.feature', 'Remover item do carrinho')
def test_remover_item_do_carrinho():
    """Remover item do carrinho."""


@given('que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99')
def camiseta_no_carrinho(carrinho):
    """que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99."""
    carrinho.adicionar_item("Camiseta", 29.99)


@when('eu removo o item do carrinho')
def remover_item_do_carrinho(carrinho):
    """eu removo o item do carrinho."""
    carrinho.remover_item()


@then('o carrinho de compras deve estar vazio')
def deve_estar_vazio(carrinho):
    """o carrinho de compras deve estar vazio."""
    assert carrinho.esta_vazio()

