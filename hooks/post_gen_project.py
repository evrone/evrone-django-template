import os
import secrets
from pathlib import Path

RANDOM_CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
SECRET_KEY_LENGTH = 50


def get_random_secret_key():
    """
    Copied and adopted from `django.utils.crypto.get_random_string`
    """

    secret_key_chars = [
        secrets.choice(RANDOM_CHARACTERS) for _ in range(SECRET_KEY_LENGTH)
    ]

    return "".join(secret_key_chars)


def write_env_file_with_secret_key():
    """
    Writes `.env` file into `app/settings` with `SECRET_KEY`
    generation.
    """

    base_dir = Path.cwd()
    env_file_path = str(base_dir / "app" / "settings" / ".env")

    with open(env_file_path, mode="w") as env_file:
        secret_key = get_random_secret_key()
        secret_key_line = f"SECRET_KEY={secret_key}"

        env_file.write(secret_key_line)

        # add empty line at end of file
        env_file.write(os.linesep)
        env_file.write(os.linesep)


def remove_poetry_files() -> None:
    os.remove("pyproject.toml")
    os.remove("poetry.lock")


def remove_uv_files() -> None:
    os.remove("pyproject-uv.toml")
    os.remove("uv.lock")


if __name__ == "__main__":
    write_env_file_with_secret_key()

    if "{{ cookiecutter.package_manager }}" == "Poetry":
        remove_uv_files()
    elif "{{ cookiecutter.package_manager }}" == "uv":
        os.rename("pyproject-uv.toml", "pyproject.toml")
        remove_poetry_files()
