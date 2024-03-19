import pytest
from jsonschema import validate

from requests_http_signature import HTTPSignatureAuth

# test#2.26 

@pytest.mark.parametrize(('sig', 'offset', 'field', 'order', 'per_page', 'code'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            0,
            'name',
            'asc',
            5,
            200,

            id='test#2.26 Get list room',
        ),
    )
)
def test_get_list_order(sig, offset, field, order, per_page, code, http_client):

    # schema = {
    #     "items": [
    #         {
    #             "description": "string",
    #             "id": "string",
    #             "name": "string",
    #             "parent_id": "string",
    #             "type": "string"
    #         },
    #     ],
    #     "paging": {
    #         "offset": "number",
    #         "order_by": [
    #         {
    #             "field": "string",
    #             "order": "asc"
    #         }
    #         ],
    #         "per_page": "number",
    #         "record_count": "number"
    #     }
    # }

    r = http_client.get(f'/test/ext-api/partner/v2/placement/?offset={offset}&order_by[field]={field}&order_by[order]={order}&per_page={per_page}', auth=sig)
    print(r.content)
    # print(validate(r.json(), schema))
    assert r.status_code == code