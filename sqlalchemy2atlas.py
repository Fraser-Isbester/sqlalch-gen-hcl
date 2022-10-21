import time
import secrets
import logging
import sys
import importlib
from pathlib import Path


# Docker Management
import docker

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
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)


def main():

    # parse = ArgumentParser(description="Process a schema module.")
    # parse.add_argument(
    #     "--namespace",
    #     type=str,
    #     description="The path to the schema file with the declarative base.",
    # )
    # parse.add_argument(
    #     "--path",
    #     type=str,
    #     description="The path to the schema file with the declarative base.",
    # )

    # base = load_sqla_base()
    base = importlib.import_module("test.schema").Base
    # base = get_base()

    try:
        db = PostgreContainer()

        engine = create_engine(db.connection_string, poolclass=NullPool)

        base.metadata.create_all(engine)

        stream = popen(f'atlas schema inspect --url "{db.connection_string}"')
        output = stream.read()

        logging.debug(output)
        print(output, file=sys.stdout)

    finally:
        logging.debug("Completed. Cleaning up....")
        try:
            db.container.kill()
        except UnboundLocalError as err:
            logging.info("db container failed to initialize, nothing to kill.")
        logging.debug("Done cleaning up.")


# def get_base(
#     namespace="test.schema",
#     filepath="/Users/fraserisbester/Documents/code/sqlalch-gen-hcl/gen/test/schema.py",
# ):
#     """Fetches the SQLAlchemy Base from File"""

#     spec = importlib.util.spec_from_file_location(namespace, filepath)
#     mod = importlib.util.module_from_spec(spec)
#     sys.modules["module.name"] = mod
#     spec.loader.exec_module(mod)
#     return mod.Base


class PostgreContainer:
    """Postgres flavored container"""

    def __init__(
        self, image="postgres:latest", port=5432, password=None, wait_for_ready=True
    ):
        self.container = None

        self.db_image = image
        self.db_port = port
        self.db_password = password or self._gen_password()

        self._init_db_container()
        if wait_for_ready:
            self._wait_for_db_ready()

    @property
    def connection_string(self):
        connection_string = f"postgresql://postgres:{self.db_password}@localhost:{self.db_port}/postgres?sslmode=disable"
        return connection_string

    def _wait_for_db_ready(self):
        ready_string = "database system is ready to accept connections"
        logging.debug("Waiting for the DB to be initialize...")
        for log in self.container.logs(stream=True):
            if ready_string in log.decode("ascii"):
                logging.debug("DB is ready with note: '%s'", ready_string)
                time.sleep(0.25)  # TODO: Invesitgate ready failure without this
                return

    def _gen_password(self):
        return secrets.token_urlsafe(8)

    def _init_db_container(self):
        container_name_hash = secrets.token_urlsafe(4).lower()
        container_name = f"dev-postgres-{container_name_hash}"
        logging.debug("Initializing DB container with name: '%s'", container_name)

        client = docker.from_env()
        self.container = client.containers.run(
            self.db_image,
            name=container_name,
            environment=[f"POSTGRES_PASSWORD={self.db_password}"],
            ports={"5432/tcp": self.db_port},
            detach=True,
        )
        logging.debug("Initializing DB container: %s", self.container)


if __name__ == "__main__":
    logging.debug("=============== Gen. Start ===============")
    main()
    logging.debug("=============== Gen. End ===============")
