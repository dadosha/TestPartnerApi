import pytest

from requests_http_signature import HTTPSignatureAuth

# test#2.01 Budapesht signature
# test#2.02 Incorrect partner Key Id
# test#2.03 Incorrect partner Key Secret
# test#2.04 Empty signature

@pytest.mark.parametrize(('sig', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            200,
            {"partner_id": 3},

            id='test#2.01 Budapesht signature',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3asfgafgahdfahsdh",
                key="12345",
            ),
            401,
            {"code":401,"data":None,"message":"Unexpected key ID","name":"Unauthorized"},

            id='test#2.02 Incorrect partner Key Id',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="jlhfdsaklfgajsgh",
            ),
            401,
            {"code":401,"data":None,"message":"Invalid signature","name":"Unauthorized"},

            id='test#2.03 Incorrect partner Key Secret',
        ),
        pytest.param(
            None,
            401,
            {"code":401,"data":None,"message":"Invalid signature","name":"Unauthorized"},

            id='test#2.04 Empty signature',
        ),
    )
)
def test_successful_get_partner_id(sig, code, result, http_client):
    r = http_client.get('/test/ext-api/partner/v2/me/', auth=sig)
    print(sig)
    print(r.content)
    assert r.status_code == code
    assert r.json() == result