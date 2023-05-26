SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'nicolassreis',
        senha = 'senhauser',
        servidor = 'localhost',
        database = 'pet_db'
    )