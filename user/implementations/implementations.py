from user.models import Users
from XcodeApi.connection import DBConnection
from user.utils import get_users_payload, get_top_performer_payload, login_payload
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from sqlalchemy import func
import uuid
from user.utils import user_columns
from passlib.hash import pbkdf2_sha256


class UserImplementation:
    def __init__(self, requests):
        self.requests = requests

    def login_user(self):
        payload = []
        message = ""
        user = self.requests.get("user", None)
        with DBConnection() as session:
            try:
                query = session.query(Users.user_id, Users.usn, Users.password,)\
                    .filter(Users.usn == user[0]["usn"].lower())
                data = query.all()
                if data:
                    if pbkdf2_sha256.verify(user[0]["password"], data[0][2]):
                        payload, message = login_payload(data)
            except Exception as e:
                print(e)
                raise e
        return payload, message

    def get_users(self):
        payload = []
        count = 0
        try:
            users_to_find = self.requests.get("users", None)
            with DBConnection() as session:
                if len(users_to_find):
                    for user in users_to_find:
                        query = session.query(Users).filter(Users.user_id == user)
                        data = query.all()
                        if data:
                            payload1, message, count = get_users_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"user_id": user, "message": "User doesn't exists."})
                    message = str(count) + " user fetched."
                else:
                    query = session.query(Users)
                    data = query.all()
                    payload, message, count = get_users_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    def create_users(self):
        payload = []
        count = 0
        try:
            users_to_create = self.requests.get("users", None)
            with DBConnection() as session:
                for user in users_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_user = Users(
                            user_id=_id,
                            usn=user['usn'].lower(),
                            first_name=user['first_name'],
                            last_name=user['last_name'],
                            name=user['first_name']+" "+user['last_name'],
                            email=user['email'],
                            password=pbkdf2_sha256.encrypt(user['password'], rounds=1200, salt_size=32),
                            mobile_number=user['mobile_number'],
                            gender=user['gender'].lower(),
                            image_url=user['image_url'],
                            score=0,
                            date_of_birth=user['date_of_birth'],
                            created_by=_id,
                            created_on=datetime.now(),
                            modified_by=_id,
                            modified_on=datetime.now(),
                        )
                        session.add(new_user)
                        session.commit()
                        payload.append({"user_id": _id, "message": "added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"user_id": _id, "message": str(e._message).split("Key (")[1].split(")")[0]
                                                                   + " already exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " users created."

    def update_users(self):
        payload = []
        count = 0
        try:
            users_to_update = self.requests.get("users", None)
            with DBConnection() as session:
                for user in users_to_update:
                    columns_to_update = {}
                    for key, value in user["update_data"].items():
                        columns_to_update[user_columns[key]] = value
                    columns_to_update[Users.modified_by] = user['user_id']
                    columns_to_update[Users.modified_on] = datetime.now()

                    try:
                        query = session.query(Users).filter(Users.user_id == user['user_id'])\
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"user_id": user['user_id'], "message": "updated successfully."})
                        else:
                            payload.append({"user_id": user['user_id'], "message": "User doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"user_id": user['user_id'], "message": str(e._message).split("Key (")[1].split(")")[0]
                                                                   + " already exists."})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " user updated."

    def delete_users(self):
        payload = []
        count = 0
        try:
            users_to_delete = self.requests.get('users', None)
            with DBConnection() as session:
                for user in users_to_delete:
                    query = session.query(Users).filter(Users.user_id == user)\
                        .delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"user_id": user, "message": "Deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"user_id": user, "message": "User doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " rows deleted."

    def top_performer_users(self):
        try:
            with DBConnection() as session:
                query = session.query(Users).filter(Users.score > 0).order_by(Users.score.desc()).limit(7)
                data = query.all()
                payload = get_top_performer_payload(data)
        except Exception as e:
            print(e)
            raise e
        return payload, str(len(data)) + " top performers fetched."
