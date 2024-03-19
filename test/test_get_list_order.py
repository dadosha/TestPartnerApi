import pytest

from requests_http_signature import HTTPSignatureAuth

# test#2.07 Change status payment_pending > paid > cancelling > completed with existing order_id

@pytest.mark.parametrize(('sig', 'offset', 'field', 'order', 'per_page', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            1,
            'status',
            'asc',
            1,
            200,
            {"status": "ok"},

            id='test#2.07 Get list order',
        ),
    )
)
def test_get_list_order(sig, offset, field, order, per_page, code, result, http_client):

    r = http_client.get(f'/test/ext-api/partner/v2/order/?offset={offset}&order_by[field]={field}&order_by[order]={order}&per_page={per_page}', auth=sig)
    print(sig)
    print(r.content)
    assert r.status_code == code