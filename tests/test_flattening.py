from __future__ import annotations

from uuid import UUID

from src.main import flatten_model_instance
from src.models import Address, BankDetails, Category, Contact, Supplier, SupplierCategory



def test_flatten_model_instance(supplier: Supplier) -> None:
    data_map = {}
    flatten_model_instance(supplier, data_map)
    assert data_map == {
        Supplier.__table__: [
            {
                "created_at": "2020-02-21 00:00:00",
                "email": "info@loros.example",
                "name": "Loros Grist",
                "address_id": None,
                "bank_details_id": None,
                "id": "2b7e7211-d2c7-4eb4-8c14-05ed58c77473",
            }
        ],
        Address.__table__: [
            {"line_1": "Celestia", "id": "c5fb851f-63fd-4572-872c-3597186c9afe"},
            {
                "line_1": "The imperial road",
                "id": "cd521f7e-df61-4079-b44d-35015b9b5110",
            },
        ],
        BankDetails.__table__: [
            {
                "account_number": "payusnothing",
                "account_type": "cash",
                "id": "ccd390cf-a74c-4897-a923-3d77ce1b97bf",
            }
        ],
        Category.__table__: [
            {"name": "Baked goods", "id": "3674c73c-a967-493f-9a4b-5b70f78a5a99"},
            {"name": "ISP", "id": "f66c3eb7-7b93-4d9f-bc66-8ff07353f5e7"},
        ],
        SupplierCategory.__table__: [
            {
                "supplier_id": UUID("2b7e7211-d2c7-4eb4-8c14-05ed58c77473"),
                "category_id": UUID("3674c73c-a967-493f-9a4b-5b70f78a5a99"),
                "id": UUID("764e903c-3b56-4739-bbad-1f0bbfd60a7e"),
            },
            {
                "supplier_id": UUID("2b7e7211-d2c7-4eb4-8c14-05ed58c77473"),
                "category_id": UUID("f66c3eb7-7b93-4d9f-bc66-8ff07353f5e7"),
                "id": UUID("747e7a96-3493-449a-8e65-9c3adc2d5089"),
            },
        ],
        Contact.__table__: [
            {
                "name": "Sveimann Glort",
                "email": "sveimann@loros.example",
                "address_id": None,
                "supplier_id": None,
                "id": "98a11210-949a-48ad-99c7-1d89c54c2a53",
            }
        ],
    }