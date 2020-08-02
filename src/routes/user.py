import os
import io
from flask_restful import Resource
from flask import request, send_file, current_app, jsonify, send_from_directory
import json
import requests
from src.utils import db_query
from src.app import app_config
from src.app.schema import PayloadValidate
from marshmallow import ValidationError
from src.authentication import auth
from sqlalchemy.exc import IntegrityError, InvalidRequestError, SQLAlchemyError


qud = db_query.Query()
input_schema = PayloadValidate()

app_env = os.environ.get('ENV', 'development')
config = app_config[app_env]
# @auth.authentication


class AuthResource(Resource):
    method_decorators = [auth.authentication]


class ScanQr(Resource):
    '''
    This class will scan the qr code
    '''

    def get(self):
        try:
            pass

        except Exception as e:
            print(e)
            raise e


class User(Resource):
    '''
    '''

    def get(self, id_number):
        try:
            print("id_number", id_number)
            if id_number == 'all':
                details = qud.get_user_details()
                if details:
                    return details, 200
            else:

                details = qud.get_user_details(id_number=id_number)
                if details:
                    return details, 200
                else:
                    response = {
                        "message": f"No details found for the given id_number {id_number}"
                    }
                    return response, 401

                # response = {
                #     "message": f"PLease provide id_number in the url"
                # }
                # return response, 401

        except Exception as e:
            raise e

    def post(self):
        try:
            print("heer")
            data = request.form.to_dict()
            print("data", data)

            files_obj = request.files
            print("files_obj", files_obj)
            image = files_obj.get("image")
            json_data = input_schema.load(data)
            id_number = json_data['id_number']

            if image:
                print("image", image)
                print("image mimetype", image.mimetype)
                if image.mimetype in config.ALLOWED_MIMETYPES:
                    upload_folder = config.UPLOAD_FOLDER
                    extension = '.' + image.mimetype.split('/')[-1]
                    if id_number:
                        print("id_number", id_number)
                        directory = f'{upload_folder}'

                        if not os.path.exists(directory):
                            os.makedirs(directory)

                        print("os.path.join(directory, id_number + extension)",
                              os.path.join(directory, id_number + extension))

                        image.save(
                            os.path.join(directory, id_number + extension)
                        )

                        json_data['image_url'] = os.path.join(
                            directory, id_number)
                        print("json_data['image_url']", json_data['image_url'])

                else:
                    response = {
                        "message": f"Unsupported image mimetype for id {id_number}"
                    }
                    return response, 401

            else:
                response = {
                    "message": f"Please upload an image for id {id_number}"
                }
                return response, 401

            details = qud.store_user_details(json_data)

            response = {
                "message": "Data stored succesfully!"
            }

            return response, 200

        # except ValidationError as err:
        #     return err.messages, 422

        except IntegrityError as e_xc:
            response = {
                "message": f"id_number - {id_number} already exists!"
            }
            return response, 422

        except InvalidRequestError as er:
            response = {
                "message": "Invalid Operation!"
            }
            return response,  422

        except Exception as e:
            print("here!!!!")
            raise e

    def put(self, id_number):
        try:
            data = request.form.to_dict()
            print("data", data)
            files_obj = request.files
            image = files_obj.get("image")
            json_data = input_schema.load(data, partial=True)
            print("id_number", id_number)
            if id_number:
                json_data['id_number'] = id_number
                details = qud.get_user_details(id_number)
                if details:
                    if image:

                        if image.mimetype in config.ALLOWED_MIMETYPES:
                            extension = '.' + image.mimetype.split('/')[-1]

                            upload_folder = config.UPLOAD_FOLDER[0]

                            directory = f'{upload_folder}'

                            if not os.path.exists(directory):
                                os.makedirs(directory)

                            image.save(
                                os.path.join(directory, id_number, extension)
                            )

                            json_data['image_url'] = os.path.join(
                                directory, id_number)

                        else:
                            response = {
                                "message": f"Unsupported image mimetype for id {id_number}"
                            }
                            return response, 401

                    details = qud.update_user_details(json_data)

                    response = {
                        "message": f"Data for id {id_number} updated succesfully!"
                    }

                    return response, 200

                else:
                    response = {
                        "message": f"No details found for the given id_number {id_number}"
                    }
                    return response, 401
            else:
                response = {
                    "message": f"PLease provide id_number in the url"
                }
                return response, 401

        except ValidationError as err:
            return err.messages, 500

        except InvalidRequestError as er:
            response = {
                "message": "Invalid Operation!"
            }
            return response,  422

        except Exception as e:
            print("e", e)
            # raise e
            response = {
                "message": "User details not updated!"
            }
            return response,  500

    def delete(self, id_number):
        try:
            if id_number:
                details = qud.delete_user_details(id_number)
                upload_folder = config.UPLOAD_FOLDER
                directory = f'{upload_folder}'

                os.remove(os.path.join(directory, id_number))

                if not details:

                    response = {
                        "message": f"details for id_number = {id_number} are already deleted or do not exist!"
                    }
                    return response, 422
            else:
                response = {
                    "message": "Please provide id_number to be deleted!"
                }
                return response, 422

            response = {
                "message": f"details for id_number = {id_number} are deleted!"
            }
            return response, 200

        except InvalidRequestError as er:
            return "Invalid Operation!", 422

        except Exception as e:
            raise e


class Hello(Resource):
    '''
    '''

    def get(self):
        return jsonify({'hello': 'world'})


class MediaDownload(Resource):
    '''
    Sends media from directory to server
    '''

    def get(self, id_number):
        try:
            upload_folder = config.UPLOAD_FOLDER
            directory = f'{upload_folder}'
            print("directory", directory)

            for file in os.listdir(directory):
                print("file", file)
                # print(file.mimetype)
                if id_number == file.split('.')[0]:
                    filename = file
                    print("filename", filename)
                    with open(os.path.join(directory, filename), 'rb') as bites:
                        return send_file(
                            io.BytesIO(bites.read()),
                            attachment_filename=filename,
                            mimetype='image/jpg'
                        )

        except Exception as e:
            raise e
