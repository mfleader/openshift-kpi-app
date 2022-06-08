import sqlmodel as sqm

import app.config


cfg = app.config.get_config()
engine = sqm.create_engine(
    url = (
        f"{cfg.get('database.dialect')}://"
        f"{cfg.get('database.user')}:"
        f"{cfg.get('database.password')}@"
        f"{cfg.get('database.server_url')}:5432/"
        f"{cfg.get('database.name')}"),
    echo = True
)
