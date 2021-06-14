import logging


from hafiz.app import create_app

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info('INITIALISING ENVIRONMENT')


app = create_app()