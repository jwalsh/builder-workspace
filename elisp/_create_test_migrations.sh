#!/bin/bash

# create_test_migrations.sh
# This script creates three test migration files for the AWS AI Practice module

MIGRATIONS_DIR="./migrations"

# Ensure the migrations directory exists
mkdir -p "$MIGRATIONS_DIR"

# Function to create a migration file
create_migration() {
    local number=$1
    local name=$2
    local content=$3
    local filename=$(printf "%03d_%s.el" $number "$name")
    echo "Creating migration: $filename"
    cat << EOF > "$MIGRATIONS_DIR/$filename"
;;; $filename --- $name

;;; Commentary:
;; This migration $name

;;; Code:

(defun migrate-$(printf "%03d" $number)-$name ()
  "$content"
  $content)

(provide 'migrate-$(printf "%03d" $number)-$name)

;;; $filename ends here
EOF
}

# Create three test migrations
create_migration 003 "add_tags_support" '(sqlite-execute aws-ai-practice-db-file
                        "ALTER TABLE practice_data ADD COLUMN tags TEXT")'

create_migration 004 "add_difficulty_level" '(sqlite-execute aws-ai-practice-db-file
                        "ALTER TABLE practice_data ADD COLUMN difficulty_level INTEGER DEFAULT 1")'

create_migration 005 "create_categories_table" '(sqlite-execute aws-ai-practice-db-file
                        "CREATE TABLE IF NOT EXISTS categories (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL UNIQUE
                         )")'

echo "Test migrations created successfully in $MIGRATIONS_DIR"
