"""Sqlalchemy2atlas Unit Tests."""
import context


def test_test():
    """Test test, should always pass."""
    assert True


def test_flavor_postgres_repr():
    """Test postgres flavor."""
    assert context.containers.Flavors.POSTGRES.value == "postgres"
