# File: migrations/02_add_implementation_state.py

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
            "SELECT name FROM migrations WHERE name = ?",
            ("02_add_implementation_state",),
        )
        if cursor.fetchone():
            print("Migration 02_add_implementation_state has already been applied.")
            return

        # 1. Add new column for implementation_state if it doesn't exist
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

        # 2. Update TaskType enum in the database
        new_task_types = [
            "implementation",
            "testing",
            "documentation",
            "infrastructure",
            "monitoring",
            "diagram",
            "research",
        ]
        for task_type in new_task_types:
            cursor.execute(
                """
            INSERT OR IGNORE INTO task_types (name) VALUES (?)
            """,
                (task_type,),
            )
        print("Updated task types in the database.")

        # 3. Create a new table for implementation states
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS implementation_states (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
        """
        )
        print("Created implementation_states table.")

        # 4. Populate implementation states
        implementation_states = [
            "not_started",
            "in_progress",
            "review",
            "testing",
            "completed",
        ]
        for state in implementation_states:
            cursor.execute(
                """
            INSERT OR IGNORE INTO implementation_states (name) VALUES (?)
            """,
                (state,),
            )
        print("Populated implementation states.")

        # 5. Update existing tasks to set default values
        cursor.execute(
            """
        UPDATE tasks
        SET implementation_state = 'not_started'
        WHERE task_type IN ('implementation', 'testing', 'documentation', 'infrastructure', 'monitoring')
        AND implementation_state IS NULL
        """
        )
        print("Updated existing tasks with default implementation state.")

        # Record this migration as applied
        cursor.execute(
            """
        INSERT INTO migrations (name, applied_at) VALUES (?, ?)
        """,
            ("02_add_implementation_state", datetime.now().isoformat()),
        )

        # Commit the transaction
        conn.commit()
        print("Migration 02_add_implementation_state completed successfully!")

    except sqlite3.Error as e:
        # If there's an error, roll back the changes
        conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()


if __name__ == "__main__":
    run_migration()
