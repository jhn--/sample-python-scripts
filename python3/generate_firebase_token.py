from firebase_token_generator import create_token

auth_payload = { "uid": "custom:1", "auth_data": "foo", "other_auth_data": "bar" }
token = create_token("CWO3CaLOZcjWr2jzVOstH3q6PAHPzXcKXsJcQOAb", auth_payload)
print(token)