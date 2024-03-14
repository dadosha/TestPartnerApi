import pytest

from requests_http_signature import HTTPSignatureAuth

# test_successful_recognition_normalized_text
# test#5 Delete room correct
# test#11 Delete incorrect room ID
# test#12 Delete third partner room
# test#13 Delete room with incorrect partner
# test#14 Delete room without partner

@pytest.mark.parametrize(('sig', 'id', 'code'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'test-api-room-6152',
            200,
            id='test#5 Delete room correct',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'test-api-room-1804895410459613',
            404,
            id='test#11 Delete incorrect room ID',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="hobot_yuzhnyy_test",
                key="qtKaYRXkoPfC",
            ),
            'test-api-room-1',
            404,
            id='test#12 Delete third partner room',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="`ljdvhlrvjh`klsvd`",
                key="`ljdvjlv`hvdsl`",
            ),
            'test-api-room-1',
            401,
            id='test#13 Delete room with incorrect partner',
        ),
        pytest.param(
            None,
            'test-api-room-1',
            401,
            id='test#14 Delete room without partner',
        )
    )
)
def test_successful_delete_room(sig, id, code, http_client):
    r = http_client.delete(f'/test/ext-api/partner/v2/placement/{id}', auth=sig)

    print(r.content)
    assert r.status_code == code