import requests

from src.baseclasses.response import Response
from src.schemas.users import User


def test_getting_users_list(get_users, make_number):
    """
    Test for getting users

    """
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)



def test_another():
    """
    Test to check that 1 is equal to 1
    """
    assert 1 == 1
