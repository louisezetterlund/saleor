from ...app.models import AppToken
from ..middleware import get_app


def test_get_app(app):
    # given
    token_inst, token = AppToken.objects.create_app_token(app=app, name="test")

    # when
    returned_app = get_app(token)

    # then
    assert returned_app.id == app.id


def test_get_app_no_app_found():
    # when
    returned_app = get_app("test")

    # then
    assert returned_app is None
