from django.conf import settings
from django.core.management.utils import get_random_secret_key


def write_env_file_with_secret_key():
    """
    Writes `.env` file into `app/settings` with `SECRET_KEY`
    generation.
    """

    base_dir = settings.BASE_DIR
    env_file_path = base_dir / "settings" / ".env"

    with open(env_file_path, mode="w") as env_file:
        secret_key = get_random_secret_key()
        secret_key_line = f"SECRET_KEY={secret_key}"

        env_file.write(secret_key_line)
