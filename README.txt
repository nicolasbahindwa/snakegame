docker exec -it c570dc1855a4 psql -U snakegame // connect to database in cmd



PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website python
Python 3.7.5 (default, Nov 23 2019, 06:10:46)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from snakegame.app import create_app
>>> app = create_app()
>>> app.app_context().push()
>>> from snakegame.blueprints.user.models import User


running migration
====================================

docker-compose exec --user "$(id -u):$(id -g)" website alembic revision -m "create inquiry table"


PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic revision -m "create inquiry table"


PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> ce897533b3ec
INFO  [alembic.runtime.migration] Running upgrade ce897533b3ec -> 0f38a0f403db
PS C:\Users\USER\Desktop\ASAS-APP>


PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic downgrade -1

migration history
===================
PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic current
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
0f38a0f403db (head)
PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic history --verbose
Rev: 0f38a0f403db (head)
Parent: ce897533b3ec
Path: /snakegame/snakegame/migrations/versions/0f38a0f403db_create_inquiry_table.py



Rev: ce897533b3ec
Parent: <base>
Path: /snakegame/snakegame/migrations/versions/ce897533b3ec_create_inquiry_table.py



PS C:\Users\USER\Desktop\ASAS-APP>


generate automatic migration
==========================================================================
PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic current
PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic revision --autogenerate -m "add secret_pharase to users"
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
ERROR [alembic.util.messaging] Target database is not up to date.
  FAILED: Target database is not up to date.
PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic upgrade headINFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade ce897533b3ec -> 0f38a0f403db
PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic upgrade head                                 >
PS C:\Users\USER\Desktop\ASAS-APP>
PS C:\Users\USER\Desktop\ASAS-APP>
PS C:\Users\USER\Desktop\ASAS-APP> docker-compose exec website alembic revision --autogenerate -m "add secret_pharase to users"
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] Detected sequence named 'inquiry_id_seq' as owned by integer column 'inquiry(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare] Detected removed table 'inquiry'
INFO  [alembic.ddl.postgresql] Detected sequence named 'credit_cards_id_seq' as owned by integer column 'credit_cards(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'invoices_id_seq' as owned by integer column 'invoices(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'subscriptions_id_seq' as owned by integer column 'subscriptions(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'coupons_id_seq' as owned by integer column 'coupons(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'bets_id_seq' as owned by integer column 'bets(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare] Detected added column 'users.secret_phrase'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_users_secret_phrase' on '['secret_phrase']'
  Generating /snakegame/snakegame/migrations/versions/b0fbd2eb478c_add_secret_pharase_to_users.py ... done
PS C:\Users\USER\Desktop\ASAS-APP>