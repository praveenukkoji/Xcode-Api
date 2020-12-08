from user.models import Users

def login_payload(data):
    try:
        payload = []
        for user in data:
            new_user = {
                "user_id": user.user_id
            }
        payload.append(new_user)
    except Exception as e:
        print(e)
        raise e
    return payload, "Logged in successfully."

def get_users_payload(data, count):
    try:
        payload = []
        for user in data:
            date = str(user.date_of_birth).split()[0]
            new_user = {
                "user_id": user.user_id,
                "usn": user.usn,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "name": user.name,
                "email": user.email,
                "mobile_number": user.mobile_number,
                "gender": user.gender,
                "image_url": user.image_url,
                "score": user.score,
                "date_of_birth": date
            }
            payload.append(new_user)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " users fetched.", count


user_columns = {
    "user_id": Users.user_id,
    "usn": Users.usn,
    "first_name": Users.first_name,
    "last_name": Users.last_name,
    "name": Users.name,
    "email": Users.email,
    "mobile_number": Users.mobile_number,
    "gender": Users.gender,
    "image_url": Users.image_url,
    "date_of_birth": Users.date_of_birth
}


def get_top_performer_payload(data):
    try:
        payload = []
        for user in data:
            date = str(user.date_of_birth).split()[0]
            new_user = {
                "user_id": user.user_id,
                "usn": user.usn,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "name": user.name,
                "email": user.email,
                "mobile_number": user.mobile_number,
                "gender": user.gender,
                "image_url": user.image_url,
                "score": user.score,
                "date_of_birth": date
            }
            payload.append(new_user)
    except Exception as e:
        print(e)
        raise e
    return payload
