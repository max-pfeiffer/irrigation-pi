"""Application configuration."""
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings


class ApplicationSettings(BaseSettings):
    """Application settings."""

    database_name: str = "sqlite"

    @computed_field
    def database_uri(self) -> str:
        """URI for database connection.

        :return:
        """
        db_path: Path = (
            Path(__file__).parent.parent.resolve()
            / "sqlite_db"
            / f"{self.database_name}.db"
        )
        return f"sqlite:///{db_path!s}"


application_settings = ApplicationSettings()
