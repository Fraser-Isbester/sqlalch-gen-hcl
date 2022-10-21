# Summary
Converts [SQLAlchemy](https://www.sqlalchemy.org/) models to [AtlasGo](https://atlasgo.io/) HCL.
# installation
    - pip install sqlalchemy2atlas
# Quickstart
    - Clone the repo
    <!-- Insall deps? Docker? -->
    - Run `make`
    <!-- Usage -->
    - Run `sqlalchemy2atlasgo -m ./schemas` to generate HCL

# Driver Support
- [x] PostgreSQL
    - [x] 14.x
- [ ] Spanner

# Todo
- [x] Spin up & Manage an empty postgres container with python
- [x] Connect to the temporary container with SQLAlchemy
- [x] Given a SQLAlchemy model, generate a table in the postgres container
- [ ] Run Atlas Inspector on the postgres container to generate an HCL file
- [ ] Wrap the whole thing in a CLI
- [ ] Schema semantics
