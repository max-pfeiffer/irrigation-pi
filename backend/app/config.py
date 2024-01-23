"""Application configuration."""
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
        return f"sqlite:///{self.database_name}.db"


application_settings = ApplicationSettings()
