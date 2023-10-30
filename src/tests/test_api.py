from http import HTTPStatus
from flask import url_for,json

def test_all(client):
    resp=client.get(url_for('api.all'))
    assert resp.status_code==HTTPStatus.OK
    json=resp.get_json()
    assert len(json)==2