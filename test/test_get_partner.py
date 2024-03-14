import pytest

from requests_http_signature import HTTPSignatureAuth

# test#1 Budapesht signature
# test#2 Incorrect signature
# test#3 Empty signature

@pytest.mark.parametrize(('sig'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),

            id='test#1 Budapesht signature',
        ),
    )
)
def test_successful_get_partner_id(sig, http_client):
    r = http_client.get('/test/ext-api/partner/v2/me/', auth=sig)
    assert r.status_code == 200

@pytest.mark.parametrize(('sig'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3asfgafgahdfahsdh",
                key="12345",
            ),

            id='test#2 Incorrect signature',
        ),
        pytest.param(
            None,

            id='test#3 Empty signature',
        ),
    )
)
def test_unsuccessful_get_partner_id(sig, http_client):
    
    r = http_client.get('/test/ext-api/partner/v2/me/', auth=sig)
    assert r.status_code == 401