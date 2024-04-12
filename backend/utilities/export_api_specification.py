"""Script for exporting backend API specification."""

import json
from pathlib import Path

from app.main import app


def main():
    """Export API specifications as JSON.

    :return:
    """
    api_specs: dict = app.openapi()
    version: str = api_specs["info"]["version"].replace(".", "_")

    api_specs_path: Path = (
        Path(__file__).parent.parent.resolve()
        / "api_specification"
        / f"api_specs_v{version}.json"
    )

    with open(api_specs_path, "w") as file:
        file.write(json.dumps(api_specs))


if __name__ == "__main__":
    main()
