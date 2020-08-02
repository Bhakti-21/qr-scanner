

class Config(object):
    pass


class DevelopmentConfig(Config):
    MEDIA_PATH = '/qr_scan/media_files'
    POSTGREHOST = 'ec2-54-236-146-234.compute-1.amazonaws.com'
    POSTGREPASSWORD = '9682020be8c922bea72f66568698315a0b6ff8eaa59e9b0953f2179d2f60f903'
    POSTGREUSER = 'wanturrslkhtcj'
    POSTGREPORT = '5432'
    POSTGREDB = 'd3ddb6d1nmja01'
    ALLOWED_MIMETYPES = ['image/jpg', 'image/jpeg', 'image/png']
    UPLOAD_FOLDER = '/qr_scan/media'
    CONNECTION_STRING = f'postgres://wanturrslkhtcj:9682020be8c922bea72f66568698315a0b6ff8eaa59e9b0953f2179d2f60f903@ec2-54-236-146-234.compute-1.amazonaws.com:5432/d3ddb6d1nmja01'


app_config = {
    'development': DevelopmentConfig
}
