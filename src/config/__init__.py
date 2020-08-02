

class Config(object):
    pass


class DevelopmentConfig(Config):
    MEDIA_PATH = '/home/abhishek/Bhakti/media_files'
    POSTGREHOST = 'localhost'
    POSTGREPASSWORD = 'qr_user'
    POSTGREUSER = 'qr_user'
    POSTGREPORT = '5432'
    POSTGREDB = 'qr_db'
    ALLOWED_MIMETYPES = ['image/jpg', 'image/jpeg', 'image/png']
    UPLOAD_FOLDER = '/home/abhishek/bhakti_projects/qr_scan/media'
    CONNECTION_STRING = f'postgresql://qr_user:qr_user@localhost:5432/qr_db'


app_config = {
    'development': DevelopmentConfig
}
