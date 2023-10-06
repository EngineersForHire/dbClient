from dataclasses import dataclass
import edgedb


@dataclass
class DSN:
    user: str
    password: str
    host: str
    port: int
    database: str
    tls_ca: str | None


class dbCLient:
    __edgedbClient: edgedb.AsyncIOClient
    __dsn: DSN | str | None = None
    
    @property
    def dsn(self):
        return self.__dsn

    async def __init__(self, dsn: DSN | str | None = None) -> None:
        if dsn is not None:
            await self.connectToDB(dsn=dsn)

    def dsnToStr(self, dsn: DSN):
        dsnStr = f"edgedb://{dsn.user}:{dsn.password}@{dsn.host}:{dsn.port}/{dsn.database}"
        tls_ca = dsn.tls_ca if dsn.tls_ca is not None else ""
        return dsnStr,tls_ca
        
    async def connectToDB(self, dsn: DSN | str):
        if self.__edgedbClient is not None:
            await self.__edgedbClient.aclose()
        self.__edgedbClient = edgedb.create_async_client(dsn=self.dsnToStr(dsn) if isinstance(dsn, DSN) else dsn)
        self.__dsn = dsn
