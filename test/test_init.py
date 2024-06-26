from dbclient import edb_client
from dbclient.db import dbCLient, DSN
import edgedb

# to test instance connection you must create it first with 'edgedb instance create test'
# and then retrieve credentials with 'edgedb instance credentials -I test --json'
instance_credentials = {
    "host": "localhost",
    "port": 10703,
    "user": "edgedb",
    "password": "UtdfFSaPpquGLhj6LbCKH0di",
    "database": "edgedb",
    "tls_cert_data": "-----BEGIN CERTIFICATE-----\nMIIC0jCCAbqgAwIBAgIQC+8NK9ZxQHKoWl2jO54xwTANBgkqhkiG9w0BAQsFADAY\nMRYwFAYDVQQDDA1FZGdlREIgU2VydmVyMB4XDTI0MDYxNDE5NTIyOVoXDTQzMDgx\nNTE5NTIyOVowGDEWMBQGA1UEAwwNRWRnZURCIFNlcnZlcjCCASIwDQYJKoZIhvcN\nAQEBBQADggEPADCCAQoCggEBAK71gMxYiIATBB5m2MAVsfqLOpLr9JjkM5RKacl7\n2J2XWZTZlBSLXpnI2Ibiima5D/gVSMTb0bgqQxWBvOpriVggQSnmbaKQuxuv6+g8\n4rgGA3N2PQUtS4GzahonGvjqvytfmFIFKrGstnIkyYXTrts3XAx5j6Qx7HRwmCcX\nal7TBvxl810QUMKH3E+XJyUB+DBqAX6cT+FDOuNQX8s12GOkv2jXRJIqfn/JCU2V\n8Eh00O0f95OuLWfG/cqu1AYj9S3tYlPtLgqxFe1+9WE8Fqjh3GmcwxH9+qLzq8ZP\nOyFX4uFKql8lEiQkuMLePXLrFOuNxRQJdtiZmjTAbJ7JdiUCAwEAAaMYMBYwFAYD\nVR0RBA0wC4IJbG9jYWxob3N0MA0GCSqGSIb3DQEBCwUAA4IBAQBIVIqhP8LgGRIc\nK/aJpNFaPu368egJCmASPPYtVyVWa9q6SkFOLK9Cw6lRfAGlYZ3X5UQfnZNfFaMv\nFfgsjEnf2/tj+b5Y2slUyq2CwFdV7a2yWqwKY+qBCMJePjVejdDWN3Zs0MXRBNOR\nKO2JHhcsJWc76ipv9MgQhrDDf+qNwkB4Ine7PQVQ1A6Zc1hWFB6Cv9NM2M0puRqT\n6TMNkagz3XwTsxPWyqktqmuSllz5Do8i6B6S90T1sWSTR4FVILpugEriUk8w1aI4\nlxoFwkkPYKT2vCd+hMsLrNB7OW+WNTOIgdJHjhCbEpk+IpAOS/OD+keLrjpr785x\nCH2PjuMy\n-----END CERTIFICATE-----\n",
    "tls_ca": "-----BEGIN CERTIFICATE-----\nMIIC0jCCAbqgAwIBAgIQC+8NK9ZxQHKoWl2jO54xwTANBgkqhkiG9w0BAQsFADAY\nMRYwFAYDVQQDDA1FZGdlREIgU2VydmVyMB4XDTI0MDYxNDE5NTIyOVoXDTQzMDgx\nNTE5NTIyOVowGDEWMBQGA1UEAwwNRWRnZURCIFNlcnZlcjCCASIwDQYJKoZIhvcN\nAQEBBQADggEPADCCAQoCggEBAK71gMxYiIATBB5m2MAVsfqLOpLr9JjkM5RKacl7\n2J2XWZTZlBSLXpnI2Ibiima5D/gVSMTb0bgqQxWBvOpriVggQSnmbaKQuxuv6+g8\n4rgGA3N2PQUtS4GzahonGvjqvytfmFIFKrGstnIkyYXTrts3XAx5j6Qx7HRwmCcX\nal7TBvxl810QUMKH3E+XJyUB+DBqAX6cT+FDOuNQX8s12GOkv2jXRJIqfn/JCU2V\n8Eh00O0f95OuLWfG/cqu1AYj9S3tYlPtLgqxFe1+9WE8Fqjh3GmcwxH9+qLzq8ZP\nOyFX4uFKql8lEiQkuMLePXLrFOuNxRQJdtiZmjTAbJ7JdiUCAwEAAaMYMBYwFAYD\nVR0RBA0wC4IJbG9jYWxob3N0MA0GCSqGSIb3DQEBCwUAA4IBAQBIVIqhP8LgGRIc\nK/aJpNFaPu368egJCmASPPYtVyVWa9q6SkFOLK9Cw6lRfAGlYZ3X5UQfnZNfFaMv\nFfgsjEnf2/tj+b5Y2slUyq2CwFdV7a2yWqwKY+qBCMJePjVejdDWN3Zs0MXRBNOR\nKO2JHhcsJWc76ipv9MgQhrDDf+qNwkB4Ine7PQVQ1A6Zc1hWFB6Cv9NM2M0puRqT\n6TMNkagz3XwTsxPWyqktqmuSllz5Do8i6B6S90T1sWSTR4FVILpugEriUk8w1aI4\nlxoFwkkPYKT2vCd+hMsLrNB7OW+WNTOIgdJHjhCbEpk+IpAOS/OD+keLrjpr785x\nCH2PjuMy\n-----END CERTIFICATE-----\n",
    "tls_security": "default"
}

def get_db_client() -> dbCLient:
    """
    Returns a edgedb client object.

    Args:
        instance_credentials (dict): A dictionary containing the required credentials for the edgedb instance.
            - user: The username to use when connecting to the database.
            - password: The password to use when connecting to the database.
            - host: The hostname or IP address of the database server.
            - port: The port number to use when connecting to the database.
            - database: The name of the database to connect to.
            - tls_ca: A path to a CA certificate file for TLS encryption.

    Returns:
        client (edgedb): The edgedb client object.
    """
    dsn = DSN(instance_credentials["user"], instance_credentials["password"], instance_credentials["host"],
              instance_credentials["port"], instance_credentials["database"], instance_credentials["tls_ca"])
    return dbCLient(dsn)


def test_edb_client_is_created() -> None:
    assert isinstance(edb_client, dbCLient)

def test_dbCLient_init() -> None:
    client = get_db_client()
    assert client is not None

def test_decorator() -> None:
    client = get_db_client()
    
    @client.run_edgedb_func
    def func(edb_client: edgedb.AsyncIOClient, *args, **kwargs) -> None:
        assert edb_client is not None
    
    func(edb_client=client)
