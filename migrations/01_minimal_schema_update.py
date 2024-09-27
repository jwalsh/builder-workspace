# File: migrations/01_minimal_schema_update.py

import sqlite3
import os
from datetime import datetime


def get_db_path():
    return os.path.join(os.getcwd(), "tasks.db")


def run_migration():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    try:
        # Start a transaction
        cursor.execute("BEGIN TRANSACTION")

        # Check if migrations table exists, create if not
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            applied_at TIMESTAMP
        )
        """
        )

        # Check if this migration has already been applied
        cursor.execute(
            "SELECT name FROM migrations WHERE name = ?", ("01_minimal_schema_update",)
        )
        if cursor.fetchone():
            print("Migration 01_minimal_schema_update has already been applied.")
            return

        # 1. Check if the implementation_state column exists in the tasks table, add if it doesn't
        cursor.execute("PRAGMA table_info(tasks)")
        columns = [column[1] for column in cursor.fetchall()]
        if "implementation_state" not in columns:
            cursor.execute(
                """
            ALTER TABLE tasks
            ADD COLUMN implementation_state TEXT
            """
            )
            print("Added implementation_state column to tasks table.")
        else:
            print("implementation_state column already exists in tasks table.")

        # 2. Check if the task_types table exists, create if it doesn't
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS task_types (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
        """
        )
        print("Ensured task_types table exists.")

        # 3. Update TaskType enum in the database (only add 'research' as it's the most neutral addition)
        cursor.execute(
            """
        INSERT OR IGNORE INTO task_types (name) VALUES ('research')
        """
        )
        print("Added 'research' task type.")

        # Record this migration as applied
        cursor.execute(
            """
        INSERT INTO migrations (name, applied_at) VALUES (?, ?)
        """,
            ("01_minimal_schema_update", datetime.now().isoformat()),
        )

        # Commit the transaction
        conn.commit()
        print("Migration 01_minimal_schema_update completed successfully!")

    except sqlite3.Error as e:
        # If there's an error, roll back the changes
        conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()


if __name__ == "__main__":
    run_migration()
