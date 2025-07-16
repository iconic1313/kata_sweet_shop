import pytest
from models.sweet import Sweet
from services.sweet_service import SweetService

@pytest.fixture
def service():
    return SweetService()

def test_add_sweet(service):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    service.add_sweet(sweet)
    assert len(service.get_all_sweets()) == 1

def test_duplicate_sweet_id(service):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    service.add_sweet(sweet)
    with pytest.raises(ValueError):
        service.add_sweet(sweet)

def test_delete_sweet(service):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    service.add_sweet(sweet)
    service.delete_sweet(1001)
    assert len(service.get_all_sweets()) == 0

def test_purchase_sweet(service):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    service.add_sweet(sweet)
    service.purchase_sweet(1001, 5)
    assert service.get_all_sweets()[0].quantity == 15

def test_restock_sweet(service):
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    service.add_sweet(sweet)
    service.restock_sweet(1001, 10)
    assert service.get_all_sweets()[0].quantity == 30

def test_search_by_name(service):
    sweet = Sweet(1001, "Gulab Jamun", "Milk-Based", 10, 50)
    service.add_sweet(sweet)
    result = service.search_sweets(name="Gulab")
    assert len(result) == 1

def test_sort_by_price(service):
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    sweet2 = Sweet(1002, "Gajar Halwa", "Veg-Based", 30, 10)
    service.add_sweet(sweet1)
    service.add_sweet(sweet2)
    sorted_list = service.sort_sweets("price")
    assert sorted_list[0].price == 30
