;;; aws-ai-practice-migrations.el --- Run migrations for aws-ai-practice

;;; Commentary:
;; This file manages the running of migrations for aws-ai-practice using file-based storage

;;; Code:

(defvar aws-ai-practice-migrations-dir
  (expand-file-name "migrations"
                    (file-name-directory load-file-name))
  "Directory containing aws-ai-practice migrations.")

(defvar aws-ai-practice-db-file
  (expand-file-name "aws-ai-practice-db.el"
                    (file-name-directory load-file-name))
  "Path to the file-based database for AWS AI practice.")

(defvar aws-ai-practice-file
  (expand-file-name "aws-ai-practice.el"
                    (file-name-directory load-file-name))
  "Path to the main AWS AI practice file.")

(defun aws-ai-practice-ensure-db ()
  "Ensure the file-based database exists and is initialized."
  (message "Initializing database at: %s" aws-ai-practice-db-file)
  (unless (file-exists-p aws-ai-practice-db-file)
    (with-temp-file aws-ai-practice-db-file
      (insert "((completed-migrations . nil))")))
  (message "Database initialized successfully."))

(defun aws-ai-practice-get-db-contents ()
  "Get the contents of the file-based database."
  (with-temp-buffer
    (insert-file-contents aws-ai-practice-db-file)
    (read (buffer-string))))

(defun aws-ai-practice-save-db-contents (contents)
  "Save CONTENTS to the file-based database."
  (with-temp-file aws-ai-practice-db-file
    (prin1 contents (current-buffer))))

(defun aws-ai-practice-migration-completed-p (migration-name)
  "Check if MIGRATION-NAME has been completed."
  (let ((db-contents (aws-ai-practice-get-db-contents)))
    (member migration-name (cdr (assq 'completed-migrations db-contents)))))

(defun aws-ai-practice-record-migration (migration-name)
  "Record MIGRATION-NAME as completed."
  (let* ((db-contents (aws-ai-practice-get-db-contents))
         (completed-migrations (cdr (assq 'completed-migrations db-contents))))
    (unless (member migration-name completed-migrations)
      (setq completed-migrations (cons migration-name completed-migrations))
      (setq db-contents (cons (cons 'completed-migrations completed-migrations)
                              (assq-delete-all 'completed-migrations db-contents)))
      (aws-ai-practice-save-db-contents db-contents))))


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
  (let* ((db-contents (aws-ai-practice-get-db-contents))
         (completed-migrations (cdr (assq 'completed-migrations db-contents))))
    (if completed-migrations
        (progn
          (message "Completed migrations:")
          (dolist (migration completed-migrations)
            (message "- %s" migration)))
      (message "No migrations have been applied yet."))))

(defun aws-ai-practice-get-completed-migrations ()
  "Get a list of completed migrations."
  (aws-ai-practice-ensure-db)
  (cdr (assq 'completed-migrations (aws-ai-practice-get-db-contents))))

(provide 'aws-ai-practice-migrations)

;;; aws-ai-practice-migrations.el ends here
