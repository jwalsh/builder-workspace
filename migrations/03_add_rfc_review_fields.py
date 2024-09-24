# File: migrations/03_add_rfc_review_fields.py

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
            "SELECT name FROM migrations WHERE name = ?", ("03_add_rfc_review_fields",)
        )
        if cursor.fetchone():
            print("Migration 03_add_rfc_review_fields has already been applied.")
            return

        # 1. Add new columns to the tasks table
        cursor.execute("PRAGMA table_info(tasks)")
        columns = [column[1] for column in cursor.fetchall()]

        if "review_comments" not in columns:
            cursor.execute("ALTER TABLE tasks ADD COLUMN review_comments TEXT")
            print("Added review_comments column to tasks table.")

        if "approver" not in columns:
            cursor.execute("ALTER TABLE tasks ADD COLUMN approver TEXT")
            print("Added approver column to tasks table.")

        # 2. Create rfc_states table if it doesn't exist
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS rfc_states (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
        """
        )
        print("Ensured rfc_states table exists.")

        # 3. Update RFCState enum in the database
        new_rfc_states = ["PENDING_REVIEW", "IN_REVIEW"]
        for state in new_rfc_states:
            cursor.execute(
                "INSERT OR IGNORE INTO rfc_states (name) VALUES (?)", (state,)
            )
        print("Added new RFC states to the database.")

        # Record this migration as applied
        cursor.execute(
            """
        INSERT INTO migrations (name, applied_at) VALUES (?, ?)
        """,
            ("03_add_rfc_review_fields", datetime.now().isoformat()),
        )

        # Commit the transaction
        conn.commit()
        print("Migration 03_add_rfc_review_fields completed successfully!")

    except sqlite3.Error as e:
        # If there's an error, roll back the changes
        conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()


if __name__ == "__main__":
    run_migration()
