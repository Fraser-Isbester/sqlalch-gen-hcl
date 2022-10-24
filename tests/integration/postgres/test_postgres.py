import re

from context import sqlalchemy2atlas


def test_postgres(capsys):
    """
    Tests that Provided SQLALchemy schema is converted to a known
    expected Atlas HCL output.
    """

    source_filepath = "tests/integration/postgres/assets/schema.py"
    hcl_filepath = "tests/integration/postgres/assets/schema.hcl"

    with open(hcl_filepath, "r") as hcl:
        expected_hcl = hcl.read()

    # sqlalchemy2atlas.convert(source_filepath, hcl_filepath)
    sqlalchemy2atlas.main([source_filepath, "--flavor", "postgres"])

    output = capsys.readouterr().out

    expected_hcl_normal = re.sub(f"\\s+", " ", expected_hcl).strip()
    output_normal = re.sub(f"\\s+", " ", output).strip()

    assert output_normal == expected_hcl_normal
