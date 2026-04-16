import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body ["firstName"] = first_name
    return current_body

def positive_assert(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 201
    assert response.json()["authToken"] !=""

    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + response.json()["authToken"]

    users_table_response = sender_stand_request.get_users_table()
    assert users_table_response.text.count(str_user) == 1

def negative_assert(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400



def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

def test_create_user_4_letter_in_first_name_get_success_response():
    positive_assert("aaaa")

def test_create_user_6_letter_in_first_name_get_success_response():
    positive_assert("Elissa")

def test_create_user_1_letter_in_first_name_get_success_response():
        negative_assert("A")

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400

def test_create_user_1_letter_in_first_name_get_error_response():
        negative_assert_symbol("A")

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")
    