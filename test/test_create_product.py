import pytest
import random

from parametrization import Parametrization
from requests_http_signature import HTTPSignatureAuth

# test#2.05 Create product in worked category


@Parametrization.parameters("sig", "age_restricted", "age_restricted_categories", "id_categories", "image_x1_categories", "image_x2_categories", "name_translations_categories_en", 
                            "name_translations_categories_ru", "parent_id", "currency", "description_translations_cn", "description_translations_en", 
                            "description_translations_ru", "description_translations_zh", "full_price", "id_product", "image_x1_product", "image_x2_product", "is_available", 
                            "merchant_branch_id", "price", "code", "result")
@Parametrization.case(
            name ='test#2.05 Create product in worked category',
            sig = HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            age_restricted = False,
            age_restricted_categories = False,
            id_categories = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32)),
            image_x1_categories = None,
            image_x2_categories = None,
            name_translations_categories_en = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8)),
            name_translations_categories_ru = ''.join(random.choice('АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789') for _ in range(8)),
            parent_id = '181',
            currency = 'RUB',
            description_translations_cn = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8)),
            description_translations_en = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8)),
            description_translations_ru = ''.join(random.choice('АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789') for _ in range(8)),
            description_translations_zh = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8)),
            full_price = 10000,
            id_product = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32)),
            image_x1_product = "https://vc-static.sberdevices.ru/b2b2c-cdn/img/without_photo.png",
            image_x2_product = None,
            is_available = True,
            merchant_branch_id = "eda",
            price = 500,

            code = 200,
            result = {},

        )
def test_successful_create_product_without_objects_and_tags(sig, age_restricted, age_restricted_categories, id_categories, image_x1_categories, image_x2_categories, 
                                    name_translations_categories_en, name_translations_categories_ru, parent_id, currency, description_translations_cn, description_translations_en, 
                                    description_translations_ru, description_translations_zh, full_price, id_product, image_x1_product, image_x2_product, is_available, merchant_branch_id,
                                    price, code, result, http_client):

    body = {
        "age_restricted": age_restricted,
        "categories": [
            {
            "age_restricted": age_restricted_categories,
            "id": id_categories,
            "image": {
                "x1": image_x1_categories,
                "x2": image_x2_categories
            },
            "name_translations": {
                "en": name_translations_categories_en,
                "ru": name_translations_categories_ru,
            },
            "parent_id": parent_id
            }
        ],
        "currency": currency,
        "description_translations": {
            "cn": description_translations_cn,
            "en": description_translations_en,
            "ru": description_translations_ru,
            "zh": description_translations_zh
        },
        "full_price": full_price,
        "id": id_product,
        "images": [
            {
            "x1": image_x1_product,
            "x2": image_x2_product,
            }
        ],
        "is_available": is_available,
        "merchant_branch_id": merchant_branch_id,
        "name_translations": {
            "cn": "string",
            "en": "string",
            "ru": "string",
            "zh": "string"
        },
        "options": [],
        "price": price,
    }

    r = http_client.post('/test/ext-api/partner/v2/product/', json=body, auth=sig)
    print(body)
    print(r.content)
    assert r.status_code == code