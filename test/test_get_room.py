import pytest

from requests_http_signature import HTTPSignatureAuth

# test_successful_recognition_normalized_text
# test#2.20 Get room without group
# test#2.21 Get incorrect room ID
# test#2.22 Get room with incorrect partner Key Id
# test#2.23 Get room with incorrect partner Key Secret
# test#2.24 Get room without partner
# test#2.25 Get room with group

@pytest.mark.parametrize(('sig', 'id', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'test-api-room-id-for-get-room',
            200,
            {'description': 'My test room for get room', 'id': 'test-api-room-id-for-get-room', 'name': 'test-api-room-id-for-get-room', 'parent_id': None, 'type': {'code': 'ROOM'}},

            id='test#2.20 Get room without group',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'test-api-room-1804895410459613',
            404,
            {"status":"not_found"},

            id='test#2.21 Get incorrect room ID',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="skdlnfkasnf",
                key="valo_test_40",
            ),
            'test-api-room-id-Bl2Ek82k',
            401,
            {"code":401,"data":None,"message":"Unexpected key ID","name":"Unauthorized"},

            id='test#2.22 Get room with incorrect partner Key Id',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="ljdvjlvhvdsl",
            ),
            'test-api-room-id-j9WUIQmp',
            401,
            {"code":401,"data":None,"message":"Invalid signature","name":"Unauthorized"},

            id='test#2.23 Get room with incorrect partner Key Secret',
        ),
        pytest.param(
            None,
            'test-api-group-id-iaxefeC7',
            401,
            {"code":401,"data":None,"message":"Invalid signature","name":"Unauthorized"},

            id='test#2.24 Get room without partner',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'test-api-room-id-for-get-room-with-group',
            200,
            {'description': 'My test room for get room', 'id': 'test-api-room-id-for-get-room-with-group', 'name': 'test-api-room-name-for-get-room-with-group', 'parent_id': 'test-api-group-id-1', 'type': {'code': 'ROOM'}},

            id='test#2.25 Get room with group',
        )
    )
)
def test_get_room(sig, id, code, result, http_client):
    r = http_client.get(f'/test/ext-api/partner/v2/placement/{id}', auth=sig)

    print(r.content)
    assert r.status_code == code
    assert r.json() == result