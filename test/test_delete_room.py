import pytest

from requests_http_signature import HTTPSignatureAuth

# test#2.15 Delete room correct
# test#2.16 Delete incorrect room ID
# test#2.17 Delete with incorrect partner Key Id
# test#2.18 Delete room with incorrect partner Key Secret
# test#2.19 Delete room without partner

@pytest.mark.parametrize(('sig', 'id', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'test-api-room-id-f4gGOgxm',
            200,
            {'status': 'ok'},

            id='test#2.15 Delete room correct',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'test-api-room-1804895410459613',
            404,
            {"status":"not_found"},

            id='test#2.16 Delete incorrect room ID',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="skdlnfkasnf",
                key="valo_test_40",
            ),
            'test-api-room-id-Bl2Ek82k',
            401,
            {"code":401,"data":None,"message":"Unexpected key ID","name":"Unauthorized"},

            id='test#2.17 Delete with incorrect partner Key Id',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="ljdvjlvhvdsl",
            ),
            'test-api-room-id-j9WUIQmp',
            401,
            {"code":401,"data":None,"message":"Invalid signature","name":"Unauthorized"},

            id='test#2.18 Delete room with incorrect partner Key Secret',
        ),
        pytest.param(
            None,
            'test-api-group-id-iaxefeC7',
            401,
            {"code":401,"data":None,"message":"Invalid signature","name":"Unauthorized"},

            id='test#2.19 Delete room without partner',
        )
    )
)
def test_delete_room(sig, id, code, result, http_client):
    r = http_client.delete(f'/test/ext-api/partner/v2/placement/{id}', auth=sig)

    print(r.content)
    assert r.status_code == code
    assert r.json() == result