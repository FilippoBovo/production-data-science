import sys
import logging
import click
from titanic import pipelines

logging.basicConfig(
    format='[%(asctime)s|%(module)s.py|%(levelname)s]  %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO,
    stream=sys.stdout
)

@click.command()
@click.option('--filename',
              type=click.Path(exists=True),
              prompt='Path to the Titanic CSV file',
              help='Path to the Titanic CSV file')
def titanic_analysis(filename):
    pipelines.run_titanic_analysis(filename)
