;;; 002_add_completed_migrations_feature.el --- Add feature to list completed migrations

;;; Commentary:
;; This migration adds a table to track completed migrations and
;; a function to list them in the main aws-ai-practice.el file.

;;; Code:

(defun migrate-002-add-completed-migrations-feature ()
  "Add completed migrations feature to aws-ai-practice."
  ;; Create migrations table in the database
  (sqlite-execute aws-ai-practice-db-file
                  "CREATE TABLE IF NOT EXISTS completed_migrations (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     migration_name TEXT NOT NULL UNIQUE,
                     applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )")
  
  ;; Add new function to aws-ai-practice.el
  (let ((file-path (expand-file-name "aws-ai-practice.el" 
                                     (file-name-directory 
                                      (directory-file-name 
                                       (file-name-directory load-file-name))))))
    (with-current-buffer (find-file-noselect file-path)
      (goto-char (point-max))
      (forward-line -1)  ; Move up one line to insert before the last line
      (insert "
(defun aws-ai-practice-list-completed-migrations ()
  \"List all completed migrations for aws-ai-practice.\"
  (interactive)
  (let ((migrations (sqlite-select aws-ai-practice-db-file
                                   \"SELECT migration_name, applied_at FROM completed_migrations ORDER BY id\")))
    (if migrations
        (with-output-to-temp-buffer \"*AWS AI Practice Migrations*\"
          (princ \"Completed migrations:\\n\\n\")
          (dolist (migration migrations)
            (princ (format \"%s - Applied at: %s\\n\" (car migration) (cadr migration)))))
      (message \"No migrations have been applied yet.\"))))
")
      (save-buffer)))
  
  ;; Record this migration as completed
  (sqlite-execute aws-ai-practice-db-file
                  "INSERT INTO completed_migrations (migration_name) VALUES (?)"
                  "002_add_completed_migrations_feature"))

(provide 'migrate-002-add-completed-migrations-feature)

;;; 002_add_completed_migrations_feature.el ends here
