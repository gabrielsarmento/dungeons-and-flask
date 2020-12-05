DATABASE = {
    'engine': 'mysql',
    'username': 'root',
    'password': 'password',
    'hostname': '127.0.0.1',
    'port': 3306,
    'schema': 'dungeon',
    'connection_creation': "{engine}://{username}:{password}@{hostname}:{port}/{schema}?charset=utf8" # noqa
}
