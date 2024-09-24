;;; aws-ai-practice-run-migrations.el --- Comprehensive runner for AWS AI Practice migrations and checks

;;; Commentary:
;; This script loads the necessary support, runs all pending migrations,
;; lists the completed migrations, and checks for specific function updates.

;;; Code:

(require 'cl-lib)
(require 'sqlite)

;; Ensure we're in the correct directory
(let ((current-dir (file-name-directory (or load-file-name buffer-file-name))))
  (cd current-dir))

;; Load the migrations support
(condition-case err
    (load-file "aws-ai-practice-migrations.el")
  (error
   (message "Error loading aws-ai-practice-migrations.el: %s" (error-message-string err))
   (signal (car err) (cdr err))))

(defun aws-ai-practice-run-and-list-migrations ()
  "Run all pending migrations and list completed migrations."
  (interactive)
  (condition-case err
      (progn
        ;; Ensure database exists and is initialized
        (aws-ai-practice-ensure-db)
        
        ;; Run migrations
        (aws-ai-practice-run-migrations)
        
        ;; List completed migrations
        (aws-ai-practice-list-completed-migrations)
        
        ;; Print a summary
        (let ((completed-count (length (aws-ai-practice-get-completed-migrations))))
          (message "Completed %d migration(s). See *AWS AI Practice Migrations* buffer for details."
                   completed-count)))
    (error
     (message "Error in run-and-list-migrations: %s" (error-message-string err)))))

(defun aws-ai-practice-check-function-updates ()
  "Check if the aws-ai-practice-update-file function has been updated."
  (condition-case err
      (let* ((file-path (or (symbol-file 'aws-ai-practice-update-file)
                            aws-ai-practice-file))
             (function-def (and file-path
                                (with-temp-buffer
                                  (insert-file-contents file-path)
                                  (goto-char (point-min))
                                  (when (re-search-forward "^(defun\\s-+aws-ai-practice-update-file" nil t)
                                    (backward-char)
                                    (read (current-buffer)))))))
        (if function-def
            (let ((checks '((&optional input-file output-file)
                            "Create a backup"
                            "First pass: collect existing defuns"
                            "Second pass: update or add defuns"
                            "Add any remaining new defuns")))
              (if (cl-every (lambda (check)
                              (cond
                               ((stringp check)
                                (string-match-p check (format "%S" function-def)))
                               ((listp check)
                                (equal check (cadr function-def)))))
                            checks)
                  (message "aws-ai-practice-update-file function is up to date.")
                (message "aws-ai-practice-update-file function needs updating.")))
          (message "Could not find aws-ai-practice-update-file function. Please check the file path.")))
    (error
     (message "Error checking function updates: %s" (error-message-string err)))))

(defun aws-ai-practice-run-migrations-and-checks ()
  "Run migrations, list them, and check for function updates."
  (interactive)
  (aws-ai-practice-run-and-list-migrations)
  (aws-ai-practice-check-function-updates))

;; Run the migrations, list them, and perform checks
(aws-ai-practice-run-migrations-and-checks)

(provide 'aws-ai-practice-run-migrations)

;;; aws-ai-practice-run-migrations.el ends here
