import aiosqlite
import sqlite3
import os
from pathlib import Path

class ProfileDatabase:
    def __init__(self, db_name="profiles.db"):
        self.db_name = db_name
        self.db_path = os.path.join(os.path.join(Path(__file__).parent.parent.parent, "data"), self.db_name)
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS profiles (
                    name TEXT NOT NULL,
                    path TEXT NOT NULL,
                    proxy TEXT,
                    user_agent TEXT NOT NULL,
                    wallet_address TEXT NOT NULL,
                    wallet_private_key TEXT NOT NULL,
                    password TEXT NOT NULL,
                    status INTEGER NOT NULL DEFAULT 1
                )
            ''')

            conn.commit()

    async def add_profile(self, name, path, proxy,user_agent, wallet_address, wallet_private_key, password, status = 1):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('''
                INSERT INTO profiles (name,path, proxy, user_agent, wallet_address, wallet_private_key, password, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name,path, proxy,  user_agent, wallet_address, wallet_private_key, password,status))

            await db.commit()

    async def get_profiles(self):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute('SELECT * FROM profiles') as cursor:
                return await cursor.fetchall()

    async def get_profile_by_name(self, name):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute('SELECT * FROM profiles WHERE name = ?', (name,)) as cursor:
                return await cursor.fetchone()


    async def delete_profile_by_name(self, name):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('DELETE FROM profiles WHERE name = ?', (name,))
            await db.commit()

    async def update_status_by_name(self, name, status):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('UPDATE profiles SET status = ? WHERE name = ?', (status, name))
            await db.commit()