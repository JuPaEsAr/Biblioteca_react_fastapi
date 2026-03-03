# migrate.py
# Script para generar y aplicar migraciones con Alembic automáticamente.

import os
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command
import pymysql

# Cargar variables del .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Verificar si existe la base de datos y si existe la tabla alembic_version
def clearing_alembic_version():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("""
            SHOW TABLES LIKE 'alembic_version';
        """)
        exits = cursor.fetchone()

        if exits:
            print("✔ Table alembic_version found. OK.")
        else:
            print("ℹ Table alembic_version not found. Continuing...")

        conn.close()
    except Exception as e:
        print("⚠ Error checking alembic_version:", e)


# Ejecutar migración automática
def execute_migration():
    alembic_cfg = Config("alembic.ini")
    print("📌 Building revision self-managed...")
    command.revision(alembic_cfg, autogenerate=True, message="init books")

    print("📌 Applying migration (upgrade head)...")
    command.upgrade(alembic_cfg, "head")
    print("✔ Migration applied successfully.")


if __name__ == "__main__":
    clearing_alembic_version()
    execute_migration()
