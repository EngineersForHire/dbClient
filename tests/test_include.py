from dbclient import edb_client
from dbclient.db import dbCLient

def test_edb_client_is_created() -> None:
    assert isinstance(edb_client, dbCLient)
