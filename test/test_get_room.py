import pytest

from requests_http_signature import HTTPSignatureAuth

# test_successful_recognition_normalized_text
# test#6 Get room correct
# test#7 Get incorrect room ID
# test#8 Get third partner room
# test#9 Get room with incorrect partner
# test#10 Get room without partner

@pytest.mark.parametrize(('sig', 'id', 'code'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'test-api-room-1',
            200,
            id='test#6 Get room correct',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'test-api-room-1804895410459613',
            404,
            id='test#7 Get incorrect room ID',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="hobot_yuzhnyy_test",
                key="qtKaYRXkoPfC",
            ),
            'test-api-room-1',
            404,
            id='test#8 Get third partner room',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="`ljdvhlrvjh`klsvd`",
                key="12345",
            ),
            'test-api-room-1',
            401,
            id='test#9 Get room with incorrect partner key id',
        ),
        pytest.param(
            None,
            'test-api-room-1',
            401,
            id='test#10 Get room without partner',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3`",
                key="`ljdvjlv`hvdsl`",
            ),
            'test-api-room-1',
            401,
            id='test#15 Get room with incorrect partner key',
        )
    )
)
def test_successful_get_room(sig, id, code, http_client):
    r = http_client.get(f'/test/ext-api/partner/v2/placement/{id}', auth=sig)

    print(r.content)
    assert r.status_code == code