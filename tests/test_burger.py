import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class MockBun(Bun):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class MockIngredient(Ingredient):
    def __init__(self, ingredient_type, name, price):
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


@pytest.mark.parametrize("bun_name, bun_price", [("black bun", 200), ("red bun", 150.5)])
def test_set_buns(bun_name, bun_price):
    burger = Burger()
    bun = MockBun(bun_name, bun_price)
    burger.set_buns(bun)
    assert burger.bun == bun


@pytest.mark.parametrize(
    "ingredient_type, ingredient_name, ingredient_price",
    [
        ("SAUCE", "sour cream", 0.5),
        ("FILLING", "dinosaur", 100.0)
    ]
)
def test_add_ingredient(ingredient_type, ingredient_name, ingredient_price):
    burger = Burger()
    ingredient = MockIngredient(ingredient_type, ingredient_name, ingredient_price)
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1

@pytest.mark.parametrize(
    "ingredient_type, ingredient_name, ingredient_price",
    [
        ("SAUCE", "sour cream", 0.5),
        ("FILLING", "dinosaur", 100.0)
    ]
)
def test_add_correct_ingredient(ingredient_type, ingredient_name, ingredient_price):
    burger = Burger()
    ingredient = MockIngredient(ingredient_type, ingredient_name, ingredient_price)
    burger.add_ingredient(ingredient)
    assert burger.ingredients[0] == ingredient

@pytest.mark.parametrize(
    "ingredients, index_to_remove, left_ingredient_name",
    [
        (
                [MockIngredient("SAUCE", "sour cream", 0.5),
                 MockIngredient("FILLING", "dinosaur", 100.0)],
                0,
                "dinosaur"
        )
    ]
)
def test_remove_ingredient(ingredients, index_to_remove, left_ingredient_name):
    burger = Burger()
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    burger.remove_ingredient(index_to_remove)
    assert len(burger.ingredients) == 1


@pytest.mark.parametrize(
    "ingredients, index_to_remove, left_ingredient_name",
    [
        (
                [MockIngredient("SAUCE", "sour cream", 0.5),
                 MockIngredient("FILLING", "dinosaur", 100.0)],
                0,
                "dinosaur"
        )
    ]
)
def test_remove_correct_ingredient_(ingredients, index_to_remove, left_ingredient_name):
    burger = Burger()
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    burger.remove_ingredient(index_to_remove)
    assert burger.ingredients[0].get_name() == left_ingredient_name


@pytest.mark.parametrize(
    "ingredients, from_index, to_index, expected_order",
    [
        (
                [MockIngredient("SAUCE", "sour cream", 0.5), MockIngredient("FILLING", "dinosaur", 100.0)],
                0,
                1,
                ["dinosaur", "sour cream"],
        ),
    ],
)
def test_move_ingredient(ingredients, from_index, to_index, expected_order):
    burger = Burger()
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    burger.move_ingredient(from_index, to_index)
    actual_order = [i.get_name() for i in burger.ingredients]
    assert actual_order == expected_order


@pytest.mark.parametrize(
    "bun, ingredients, expected_price",
    [
        (
                MockBun("red Bun", 150.5),
                [MockIngredient("SAUCE", "sour cream", 0.5),
                 MockIngredient("FILLING", "dinosaur", 100.0)],
                401.5,
        ),
    ],
)
def test_get_price(bun, ingredients, expected_price):
    burger = Burger()
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    assert burger.get_price() == expected_price


def test_get_receipt():
    bun = MockBun("black bun", 200.5)
    sauce = MockIngredient("SAUCE", "sour cream", 0.5)
    filling = MockIngredient("FILLING", "dinosaur", 100.0)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    receipt = burger.get_receipt()
    expected_receipt = (
        f"(==== {bun.get_name()} ====)\n"
        f"= sauce {sauce.get_name()} =\n"
        f"= filling {filling.get_name()} =\n"
        f"(==== {bun.get_name()} ====)\n\n"
        f"Price: {burger.get_price()}"
    )
    assert receipt == expected_receipt
