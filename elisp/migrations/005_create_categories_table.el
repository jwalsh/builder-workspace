;;; 005_create_categories_table.el --- create_categories_table

;;; Commentary:
;; This migration create_categories_table

;;; Code:

(defun migrate-005-create_categories_table ()
  "(sqlite-execute aws-ai-practice-db-file
                        "CREATE TABLE IF NOT EXISTS categories (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL UNIQUE
                         )")"
  (sqlite-execute aws-ai-practice-db-file
                        "CREATE TABLE IF NOT EXISTS categories (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL UNIQUE
                         )"))

(provide 'migrate-005-create_categories_table)

;;; 005_create_categories_table.el ends here
