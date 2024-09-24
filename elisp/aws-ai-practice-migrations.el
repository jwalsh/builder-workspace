;;; aws-ai-practice-migrations.el --- Run migrations for aws-ai-practice

;;; Commentary:
;; This file manages the running of migrations for aws-ai-practice

;;; Code:

(require 'sqlite)

(defvar aws-ai-practice-migrations-dir
  (expand-file-name "migrations"
                    (file-name-directory load-file-name))
  "Directory containing aws-ai-practice migrations.")

(defvar aws-ai-practice-db-file
  (expand-file-name "aws-ai-practice.db"
                    (file-name-directory load-file-name))
  "Path to the SQLite database file for AWS AI practice.")

(defvar aws-ai-practice-file
  (expand-file-name "aws-ai-practice.el"
                    (file-name-directory load-file-name))
  "Path to the main AWS AI practice file.")

(defun aws-ai-practice-ensure-db ()
  "Ensure the SQLite database exists and is initialized."
  (unless (file-exists-p aws-ai-practice-db-file)
    (with-temp-buffer
      (sqlite-execute aws-ai-practice-db-file "CREATE TABLE IF NOT EXISTS dummy (id INTEGER PRIMARY KEY)")
      (sqlite-execute aws-ai-practice-db-file "DROP TABLE IF EXISTS dummy")))
  (condition-case err
      (sqlite-execute aws-ai-practice-db-file
                      "CREATE TABLE IF NOT EXISTS completed_migrations (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         migration_name TEXT NOT NULL UNIQUE,
                         applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       )")
    (error
     (message "Error initializing database: %s" (error-message-string err))
     (signal (car err) (cdr err)))))

(defun aws-ai-practice-migration-completed-p (migration-name)
  "Check if MIGRATION-NAME has been completed."
  (condition-case nil
      (car (sqlite-select aws-ai-practice-db-file
                          "SELECT 1 FROM completed_migrations WHERE migration_name = ?"
                          migration-name))
    (error nil)))

(defun aws-ai-practice-record-migration (migration-name)
  "Record MIGRATION-NAME as completed."
  (condition-case err
      (sqlite-execute aws-ai-practice-db-file
                      "INSERT INTO completed_migrations (migration_name) VALUES (?)"
                      migration-name)
    (error
     (message "Error recording migration: %s" (error-message-string err))
     (signal (car err) (cdr err)))))

(defun aws-ai-practice-run-migrations ()
  "Run all migrations for aws-ai-practice."
  (aws-ai-practice-ensure-db)
  (let ((migration-files (directory-files aws-ai-practice-migrations-dir t "^[0-9]+_.+\\.el$")))
    (dolist (file (sort migration-files #'string<))
      (let ((migration-name (file-name-nondirectory file)))
        (unless (aws-ai-practice-migration-completed-p migration-name)
          (load file)
          (let ((migrate-func (intern (file-name-base file))))
            (when (fboundp migrate-func)
              (condition-case err
                  (progn
                    (funcall migrate-func)
                    (aws-ai-practice-record-migration migration-name)
                    (message "Ran migration: %s" migration-name))
                (error
                 (message "Error running migration %s: %s" migration-name (error-message-string err))
                 nil)))))))))

(defun aws-ai-practice-list-completed-migrations ()
  "List all completed migrations for aws-ai-practice."
  (interactive)
  (aws-ai-practice-ensure-db)
  (condition-case err
      (let ((migrations (sqlite-select aws-ai-practice-db-file
                                       "SELECT migration_name, applied_at FROM completed_migrations ORDER BY id")))
        (if migrations
            (with-output-to-temp-buffer "*AWS AI Practice Migrations*"
              (princ "Completed migrations:\n\n")
              (dolist (migration migrations)
                (princ (format "%s - Applied at: %s\n" (car migration) (cadr migration)))))
          (message "No migrations have been applied yet.")))
    (error
     (message "Error listing migrations: %s" (error-message-string err)))))

(defun aws-ai-practice-get-completed-migrations ()
  "Get a list of completed migrations."
  (aws-ai-practice-ensure-db)
  (condition-case err
      (sqlite-select aws-ai-practice-db-file
                     "SELECT migration_name FROM completed_migrations ORDER BY id")
    (error
     (message "Error getting completed migrations: %s" (error-message-string err))
     nil)))

(provide 'aws-ai-practice-migrations)

;;; aws-ai-practice-migrations.el ends here
