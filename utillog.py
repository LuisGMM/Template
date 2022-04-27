import logging

logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w', format='%(asctime)s - %(levelname) - %(message)s')

# logging.info('info')
# logging.debug('debug')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('log.log')
formatter = logging.Formatter('%(asctime)s - %(levelname) - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

