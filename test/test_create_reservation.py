import pytest
import datetime
import random

from requests_http_signature import HTTPSignatureAuth

# test_successful_recognition_normalized_text
# test#17 Create correct reservation
# test#18 Create reservation with same arrival_date and departure_date
# test#19 Create reservation with arrival_date < departure_date


@pytest.mark.parametrize(('sig', 'arrival_date', 'departure_date', 'first_name', 'language_code', 'id', 'room_name', 'room_number', 'room_type', 'code'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(days=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-1',
            'test-api-room-1',
            'ROOM',
            200,
            id='test#17 Create reservation correct arrival_date = now',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-2',
            'test-api-room-2',
            'ROOM',
            200,
            id='test#18 Create reservation with same arrival_date and departure_date',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(days=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-2289',
            'test-api-room-2289',
            'ROOM',
            200,
            id='test#19 Create reservation with arrival_date < departure_date',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            (datetime.datetime.now() - datetime.timedelta(days=1)).astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(days=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-6987',
            'test-api-room-6987',
            'ROOM',
            200,
            id='test#20 Create reservation arrival_date < now',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            (datetime.datetime.now() + datetime.timedelta(days=1)).astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(days=2)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-',
            'test-api-room-8886',
            'test-api-room-8886',
            'ROOM',
            200,
            id='test#20 Create reservation arrival_date > now',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            None,
            (datetime.datetime.now() + datetime.timedelta(days=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-2319',
            'test-api-room-2319',
            'ROOM',
            422,
            id='test#21 None arrival date',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            None,
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-2371',
            'test-api-room-2371',
            'ROOM',
            422,
            id='test#22 None depature date',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            None,
            'test-api-room-6511',
            'test-api-room-6511',
            'ROOM',
            422,
            id='test#23 None id',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            True,
            'test-api-room-5432',
            'test-api-room-5432',
            'ROOM',
            422,
            id='test#25 Id boolean',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            '2024-03-03',
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-6861',
            'test-api-room-6861',
            'ROOM',
            422,
            id='test#26 arrival_date only datet',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            '2024-03-03',
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-9504',
            'test-api-room-9504',
            'ROOM',
            422,
            id='test#27 departure_date only date',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            '2024-03-03T16:55',
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-9142',
            'test-api-room-9142',
            'ROOM',
            422,
            id='test#28 arrival_date with minutes and hour without timezone',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            '2024-03-03T16',
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-1042',
            'test-api-room-1042',
            'ROOM',
            422,
            id='test#29 arrival_date with hour and minutes',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            'adasdad',
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-9787',
            'test-api-room-9787',
            'ROOM',
            422,
            id='test#30 arrival_date text',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            True,
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-6611',
            'test-api-room-6611',
            'ROOM',
            422,
            id='test#31 arrival_date True',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(minutes=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-8539',
            'test-api-room-8539',
            'ROOM',
            200,
            id='test#32 Create reservation 1 minutes',
        ),
        pytest.param(
            None,
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(minutes=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-4687',
            'test-api-room-4687',
            'ROOM',
            401,
            id='test#33 Create reservation without auth',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="kldshglksghlgafs",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(minutes=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-5391',
            'test-api-room-5391',
            'ROOM',
            401,
            id='test#34 Create reservation without incorrect key in auth',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="jfdnlgsjfldgj",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(minutes=1)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-9862',
            'test-api-room-9862',
            'ROOM',
            401,
            id='test#35 Create reservation without incorrect key_id in auth',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(minutes=20)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'akdfadgadgamga',
            'akdfadgadgamga',
            'ROOM',
            404,
            id='test#36 Create reservation with uncreated room',
        ),
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'RU',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            None,
            None,
            None,
            200,
            id='test#37 room data None',
        ),
    )
)
def test_reservation_room(sig, arrival_date, departure_date, first_name, language_code, id, room_name, room_number, room_type, code, http_client):

    body = {
        "reservation": {
            "arrival": {
            "arrival_date": arrival_date
            },
            "departure": {
                "departure_date": departure_date
            },
            "guests": [
            {
                "first_name": first_name,
                "language_code": language_code
            }
            ],
            "id": id,
            "last_modified_date": "2024-03-13T07:56:10.204Z",
            "reservation_number": "string",
            "room_stays": [
            {
                "room_name": room_name,
                "room_number": room_number,
                "room_type": room_type
            }
            ],
            "status": "UNKNOWN"
        }
    }
    r = http_client.post('/test/ext-api/partner/v2/reservation/', json=body ,auth=sig)

    print(body)
    print(r.content)
    assert r.status_code == code

    


@pytest.mark.parametrize(('sig', 'arrival_date', 'departure_date', 'first_name', 'language_code', 'id', 'room_name', 'room_number', 'room_type', 'code',
                          'arrival_date_new', 'departure_date_new', 'first_name_new', 'language_code_new', 'room_name_new', 'room_number_new', 'room_type_new', 'code_new'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="3",
                key="12345",
            ),
            datetime.datetime.now(),
            datetime.datetime.now() + datetime.timedelta(days=1),
            'Станислав',
            'RU',
            'test-reservation-room-',
            'test-api-room-7224',
            'test-api-room-7224',
            'ROOM',
            200,
            datetime.datetime.now(),
            datetime.datetime.now() + datetime.timedelta(days=1),
            'Койфман',
            'EN',
            'test-api-room-5777',
            'test-api-room-5777',
            'ROOM',
            200,
            id='test#21 Create reservation and another request on same id after',
        ),
    )
)
def test_two_requests_reservation(sig, arrival_date, departure_date, first_name, language_code, id, room_name, room_number, room_type, code,
                                   arrival_date_new, departure_date_new, first_name_new, language_code_new, room_name_new, room_number_new, room_type_new, code_new, http_client):
    number = random.randint(1, 100000)

    body = {
        "reservation": {
            "arrival": {
            "arrival_date": arrival_date.astimezone().replace(microsecond=0).isoformat()
            },
            "departure": {
                "departure_date": departure_date.astimezone().replace(microsecond=0).isoformat()
            },
            "guests": [
            {
                "first_name": first_name,
                "language_code": language_code
            }
            ],
            "id": id + str(number),
            "last_modified_date": "2024-03-13T07:56:10.204Z",
            "reservation_number": "string",
            "room_stays": [
            {
                "room_name": room_name,
                "room_number": room_number,
                "room_type": room_type
            }
            ],
            "status": "UNKNOWN"
        }
    }
    r = http_client.post('/test/ext-api/partner/v2/reservation/', json=body ,auth=sig)

    print(r.content)
    assert r.status_code == code

    body_new = {
        "reservation": {
            "arrival": {
            "arrival_date": arrival_date_new.astimezone().replace(microsecond=0).isoformat()
            },
            "departure": {
                "departure_date": departure_date_new.astimezone().replace(microsecond=0).isoformat()
            },
            "guests": [
            {
                "first_name": first_name_new,
                "language_code": language_code_new
            }
            ],
            "id": id + str(number),
            "last_modified_date": "2024-03-13T07:56:10.204Z",
            "reservation_number": "string",
            "room_stays": [
            {
                "room_name": room_name_new,
                "room_number": room_number_new,
                "room_type": room_type_new
            }
            ],
            "status": "UNKNOWN"
        }
    }

    r = http_client.post('/test/ext-api/partner/v2/reservation/', json=body_new ,auth=sig)

    print(r.content)
    assert r.status_code == code_new


@pytest.mark.parametrize(('sig', 'arrival_date', 'departure_date', 'first_name', 'language_code', 'id', 'room_name', 'room_number', 'room_type', 'status', 'code', 'result'), (
        pytest.param(
            HTTPSignatureAuth(
                key_id="Valo_40",
                key="valo_test_40",
            ),
            (datetime.datetime.now() - datetime.timedelta(hours=1)).astimezone().replace(microsecond=0).isoformat(),
            (datetime.datetime.now() + datetime.timedelta(hours=23)).astimezone().replace(microsecond=0).isoformat(),
            'Станислав',
            'ru',
            'test-reservation-room-' + str(random.randint(1, 100000)),
            'test-api-room-6705',
            'test-api-room-6705',
            'ROOM',
            'IN_HOUSE',
            200,
            {'status': 'ok'},
            id='test#38 room data IN_HOUSE',
        ),
    )
)
def test_reservation_room_status(sig, arrival_date, departure_date, first_name, language_code, id, room_name, room_number, room_type, code, status, result, http_client):

    body = {
        "reservation": {
            "arrival": {
            "arrival_date": arrival_date
            },
            "departure": {
                "departure_date": departure_date
            },
            "guests": [
            {
                "first_name": first_name,
                "language_code": language_code
            }
            ],
            "id": id,
            "last_modified_date": "2024-03-13T07:56:10.204Z",
            "reservation_number": "string",
            "room_stays": [
            {
                "room_name": room_name,
                "room_number": room_number,
                "room_type": room_type
            }
            ],
            "status": status
        }
    }
    r = http_client.post('/test/ext-api/partner/v2/reservation/', json=body ,auth=sig)

    print(body)
    print(r.content)
    print(r.json())
    assert r.status_code == code
    assert r.json() == result