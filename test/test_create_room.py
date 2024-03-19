import pytest
import random

from requests_http_signature import HTTPSignatureAuth

# test#2.05 Create room correct, no group
# test#2.06 Create room correct with group
# test#2.07 Create group
# test#2.08 Create room correct with incorrect group
# test#2.09 Update recently create room group on GROUP
# test#2.10 Update recently create room group on ROOM
# test#2.11 Update recently create room parent_id on none
# test#2.12 Update recently create room parent_id on real
# test#2.13 Change name for recently create room
# test#2.14 Change description for recently create room

@pytest.mark.parametrize(('sig', 'description', 'id', 'name', 'parent_id', 'room_type', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room for get room',
            'test-api-room-id-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-room-name-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            None,
            'ROOM',
            200,
            {},
            id='test#2.05 Create room correct, no group',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room - ' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-room-id-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-room-name-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-group-id-1',
            'ROOM',
            200,
            {},
            id='test#2.06 Create room correct with group',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test group - ' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-group-id-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-group-name-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            None,
            'GROUP',
            200,
            {},
            id='test#2.07 Create group',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room - ' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-room-id-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-room-name-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-group-id-1fjq;rh;ajvjhrv;oaifor;fjk',
            'ROOM',
            400,
            {},
            id='test#2.08 Create room correct with incorrect group',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room for edit group',
            'test-api-room-id-for-edit-group',
            'test-api-room-name-for-edit-group',
            None,
            'GROUP',
            200,
            {},
            id='test#2.09 Update recently create room group on GROUP',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room for edit group',
            'test-api-room-id-for-edit-group',
            'test-api-room-name-for-edit-group',
            None,
            'ROOM',
            200,
            {},
            id='test#2.10 Update recently create room group on ROOM',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room for edit parent id',
            'test-api-room-id-for-edit-parent_id',
            'test-api-room-name-for-edit-parent_id',
            None,
            'ROOM',
            200,
            {},
            id='test#2.11 Update recently create room parent_id on none',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room for edit parent id',
            'test-api-room-id-for-edit-parent_id',
            'test-api-room-name-for-edit-parent_id',
            'test-api-group-id-1',
            'ROOM',
            200,
            {},
            id='test#2.12 Update recently create room parent_id on real',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room for edit parent id',
            'test-api-room-id-for-edit-text',
            'test-api-room-name-for-edit-text-' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-group-id-1',
            'ROOM',
            200,
            {},
            id='test#2.13 Change name for recently create room',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            'My test room for edit parent id ' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8)),
            'test-api-room-id-for-edit-text',
            'test-api-room-name-for-edit-text',
            'test-api-group-id-1',
            'ROOM',
            200,
            {},
            id='test#2.14 Change description for recently create room',
        ),
    )
)
def test_successful_create_room(sig, description, id, name, parent_id, room_type, code, result, http_client):
    body = {
        "description": description,
        "id": id,
        "name": name,
        "parent_id": parent_id,
        "type": {
            "code": room_type
        }
    }
    r = http_client.post('/test/ext-api/partner/v2/placement/', json=body ,auth=sig)
    print(body)
    print(r.content)
    assert r.status_code == code

    if code == 200:
        result = body
    
    assert r.json() == result