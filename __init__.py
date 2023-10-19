import asyncio
import db

event_loop = asyncio.get_event_loop()
edb_client = event_loop.run_until_complete(db.dbCLient())
