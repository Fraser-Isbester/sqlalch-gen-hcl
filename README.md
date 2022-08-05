# Summary
A little tool for converting [SQLAlchemy](https://www.sqlalchemy.org/) models to [AtlasGo](https://atlasgo.io/) HCL. Mostly an exercise in Programic docker control and hacky go/c importing. :shrug:

# Driver Support
- [] PostgreSQL

# Todo
- [] Spin up & connect to an empty postgres container with python
- [] Given a SQLAlchemy model, generate a table in the postgres container
- [] Run Atlas Inspector on the postgres container to generate an HCL file
- [] Wrap the whole thing in a CLI

# Notes
