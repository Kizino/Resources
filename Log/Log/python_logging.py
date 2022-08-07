import logging

logging.basicConfig(filename='app.log',
                    filemode='a',
                    format='[%(asctime)s.%(msecs)03d] %(name)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d - %H:%M:%S',
                    level=logging.INFO)

logging.info("Log Message")