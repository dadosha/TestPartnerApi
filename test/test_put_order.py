import pytest

from requests_http_signature import HTTPSignatureAuth

# test#2.06 Change status payment_pending > paid > cancelling > completed with existing order_id

@pytest.mark.parametrize(('sig', 'order_id', 'order_path', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'order_id',
            ["PAID", "CANCELLING"],
            200,
            {"status": "ok"},

            id='test#2.05 Change status payment_pending > paid > cancelling > completed with existing order_id',
        ),
    )
)
def test_successful_get_partner_id(sig, order_id, order_path, code, result, http_client):

    for status in order_path:
        body = {
            "status": status
        }

        r = http_client.get(f'/test/ext-api/partner/v2/order/{order_id}', json=body, auth=sig)
        print(status)
        print(sig)
        print(r.content)
        assert r.status_code == code
        assert r.json() == result