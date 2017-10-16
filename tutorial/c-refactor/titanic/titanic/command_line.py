import click
from titanic import pipelines


@click.command()
@click.option('--filename',
              type=click.Path(exists=True),
              prompt='Path to the Titanic CSV file',
              help='Path to the Titanic CSV file')
def titanic_analysis(filename):
    pipelines.run_titanic_analysis(filename)
