import os
import logging.config
import yaml
import titanic


def load_yaml_config(path=None, env_key='LOG_CFG'):
    """Setup YAML logging configuration

    Parameters
    ----------
    path: str
        Path of the YAML config file. If path=None, the titanic logging configuration file is used.
    env_key: str
        Environment variable for logging configuration file.

    Returns
    -------
    str
        Path of the loaded config file.

    """

    if not path:
        path = os.path.join(os.path.dirname(titanic.__file__), 'logging.yaml')

    value = os.getenv(env_key, None)

    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
        logging.info('No file or config environment found. Loading basic config with INFO level.')

    return path
