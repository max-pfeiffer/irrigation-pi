"""Repositories for data persistence."""
from sqlmodel import Session, select

from app.database.models import Schedule


class ScheduleRepository:
    """Repository for persisting Schedule objects."""

    def __init__(self, session: Session) -> None:
        """Initialize object.

        :param Session session:
        """
        self.session: Session = session

    def get(self, primary_key: int) -> Schedule:
        """Get one schedule by primary_key.

        :param int primary_key:
        :return:
        """
        schedule: Schedule = self.session.get_one(Schedule, primary_key)
        return schedule

    def query(self, **kwargs) -> list[Schedule]:
        """Query for Schedule objects.

        :param kwargs:
        :return:
        """
        statement = select(Schedule)
        for key, value in kwargs.items():
            statement = statement.where(getattr(Schedule, key) == value)

        result = self.session.scalars(statement).all()
        return result

    def create(self, **kwargs) -> Schedule:
        """Create a new Schedule object.

        :param kwargs:
        :return Schedule:
        """
        schedule: Schedule = Schedule(**kwargs)
        self.session.add(schedule)
        # Don't commit just flush the session in order to leverage sqlalchemy's
        # unit of work feature/pattern.
        # https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#flushing
        self.session.flush()
        return schedule

    def update(self, **kwargs):
        """Update a Schedule object.

        :param kwargs:
        :return:
        """
        primary_key: int = kwargs.pop("primary_key")
        schedule: Schedule = self.get(primary_key)

        for key, value in kwargs.items():
            setattr(schedule, key, value)

        self.session.flush()

    def delete(self, primary_key: int):
        """Delete a schedule by primary_key.

        :param int primary_key:
        :return:
        """
        schedule: Schedule = self.get(primary_key)
        self.session.delete(schedule)
        self.session.flush()
