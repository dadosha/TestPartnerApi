import pytest
import random

from requests_http_signature import HTTPSignatureAuth

# test_successful_recognition_normalized_text
# test#39 Create merchant branch

@pytest.mark.parametrize(('sig', 'id', 'kind', 'cn', 'en', 'ru', 'zh', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'test-merchat-id-' + str(random.randint(1, 100000)),
            'MEAL',
            'My text - aa',
            'My text - en',
            'My text - ru',
            'My text - zh',
            200,
            {},
            id='test#39 Create merchant branch',
        ),
    )
)
def test_successful_create_room(sig, id, kind, cn, en, code, ru, zh, result, http_client):
    number = random.randint(1, 10000)
    body = params = {
        "id": id,
        "kind": kind,
        "name_translations": {
            "cn": cn,
            "en": en,
            "ru": ru,
            "zh": zh
        }
    }
    r = http_client.post('/test/ext-api/partner/v2/merchant/branch/', json=body ,auth=sig)
    print(body)
    print(r.content)
    assert r.status_code == code
    
    if code == 200:
        result = body
    
    assert r.json() == result