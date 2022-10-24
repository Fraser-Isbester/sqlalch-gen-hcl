import time
import secrets
import logging
import sys
import importlib
from pathlib import Path
from argparse import ArgumentParser

from .containers import PostgreContainer

# DB Connectivity
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

# For Atlas
from os import popen

# Logging Config
Path("./logs").mkdir(parents=True, exist_ok=True)
log_format = "[%(levelname)s] %(asctime)s - %(name)s - %(message)s"
logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt="%y-%m-%dT%H:%M.%S",
    filename="./logs/gen.log",
    filemode="a",
)
formatter = logging.Formatter(log_format)


def main(argv=None):

    parser = ArgumentParser(description="Process a schema module.")
    parser.add_argument(
        "filepath",
        help="The relative path to the sqlalchemy schema fil. Must contain `Base = declarative_base()` .",
    )
    parser.add_argument(
        "--flavor",
        type=str,
        default="postgres",
        choices=["postgres"],
        help="The flavor of the database HCL you want to generate.",
    )

    args = parser.parse_args(argv)

    path = args.filepath.replace("/", ".").replace(".py", "")
    base = importlib.import_module(path).Base

    try:

        if args.flavor == "postgres":
            db = PostgreContainer()
        else:
            raise (f"Flavor {args.flavor} not supported.")

        engine = create_engine(db.connection_string, poolclass=NullPool)

        base.metadata.create_all(engine)

        stream = popen(f'atlas schema inspect --url "{db.connection_string}"')
        output = stream.read()

        logging.info(output)

    finally:
        logging.debug("Completed generating HCL. Cleaning up.")
        try:
            db.container.kill()
        except UnboundLocalError as err:
            logging.warning("db container failed to initialize, nothing to kill.")
        logging.debug("Done cleaning up.")

    print(output, file=sys.stdout)


if __name__ == "__main__":
    main()
