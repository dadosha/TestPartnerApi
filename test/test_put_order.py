import pytest

from requests_http_signature import HTTPSignatureAuth

# test#2.27 Change status payment_pending > PAID with existing order_id
# test#2.28 Change status payment_pending > CANCELLING with existing order_id
# test#2.28 Change status payment_pending > COMPLETED with existing order_id

@pytest.mark.parametrize(('sig', 'order_id', 'order_path', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            '65f9265c955e39001e8fdff0',
            ["PAID"],
            200,
            {"status": ""},

            id='test#2.27 Change status payment_pending > PAID with existing order_id',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            '65f926a7955e39001e8fe025',
            ["CANCELLING"],
            200,
            {"status": ""},

            id='test#2.28 Change status payment_pending > CANCELLING  with existing order_id',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            '65f926cd955e39001e8fe03a',
            ["COMPLETED"],
            200,
            {"status": ""},

            id='test#2.29 Change status payment_pending > COMPLETED with existing order_id',
        ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["PROCESSING"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.30 Change status NEW > PROCESSING with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["IN_DELIVERY"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.31 Change status NEW > IN_DELIVERY with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["CANCELLING"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.32 Change status NEW > CANCELLING with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["COMPLETED"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.33 Change status NEW > COMPLETED with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     '65f9265c955e39001e8fdff0',
        #     ["PROCESSING"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.34 Change status PAID > PROCESSING with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["IN_DELIVERY"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.35 Change status PAID > IN_DELIVERY with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["CANCELLING"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.36 Change status PAID > CANCELLING with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["COMPLETED"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.37 Change status PAID > COMPLETED with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     '65f9265c955e39001e8fdff0',
        #     ["IN_DELIVERY"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.38 Change status PROCESSING > IN_DELIVERY with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["CANCELLING"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.39 Change status PROCESSING > CANCELLING with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["COMPLETED"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.40 Change status PROCESSING > COMPLETED with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     '65f9265c955e39001e8fdff0',
        #     ["CANCELLING"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.41 Change status IN_DELIVERY > CANCELLING with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["COMPLETED"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.42 Change status IN_DELIVERY > COMPLETED with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     '65f9265c955e39001e8fdff0',
        #     ["COMPLETED"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.43 Change status CANCELLING > COMPLETED with existing order_id',
        # ),
        # pytest.param(
        #     HTTPSignatureAuth(
        #         key_id="3",
        #         key="12345",
        #     ),
        #     'order_id',
        #     ["FAILED"],
        #     200,
        #     {"status": "ok"},

        #     id='test#2.44 Change status CANCELLING > FAILED with existing order_id',
        # ),
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
        print()
        assert r.status_code == code

        if code == 200:
            assert r.json() == body
        else:
            assert r.json() == result