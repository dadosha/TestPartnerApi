import pytest
import random

from requests_http_signature import HTTPSignatureAuth

# test_successful_recognition_normalized_text
# test#4 Create room correct

@pytest.mark.parametrize(('sig', 'description', 'id', 'name', 'parent_id', 'room_type', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room - ',
            'test-api-room-',
            'test-api-room-',
            None,
            'ROOM',
            200,
            {},
            id='test#4 Create room correct',
        ),
    )
)
def test_successful_create_room(sig, description, id, name, parent_id, room_type, code, result, http_client):
    number = random.randint(1, 10000)
    body = {
        "description": description + str(number),
        "id": id + str(number),
        "name": name + str(number),
        "parent_id": parent_id,
        "type": {
            "code": room_type
            }
    }
    r = http_client.post('/test/ext-api/partner/v2/placement/', json=body ,auth=sig)
    print(body)
    print(r.content)
    assert r.status_code == code

    if code == 200:
        result = body
    
    assert r.json() == result