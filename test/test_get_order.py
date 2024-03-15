import pytest

from requests_http_signature import HTTPSignatureAuth

# test#2.07 Get real order


@pytest.mark.parametrize(('sig', 'id', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            '65f4178d138e87001eb537ea',
            200,
            {"partner_id": 3},

            id='test#2.01 Budapesht signature',
        ),
    )
)
def test_successful_get_room(sig, id, code, result, http_client):
    r = http_client.get(f'/test/ext-api/partner/v2/order/{id}', auth=sig)
    result = 0
    print(r.content)
    assert r.status_code == code