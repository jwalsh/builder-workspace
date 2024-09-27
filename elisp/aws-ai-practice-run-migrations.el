;;; aws-ai-practice-run-migrations.el --- Comprehensive runner for AWS AI Practice migrations and checks

;;; Commentary:
;; This script loads the necessary support, runs all pending migrations,
;; and lists the completed migrations.

;;; Code:

(require 'cl-lib)

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
          (message "Completed %d migration(s)." completed-count)))
    (error
     (message "Error in run-and-list-migrations: %s" (error-message-string err)))))

;; Run the migrations and list them
(aws-ai-practice-run-and-list-migrations)

(provide 'aws-ai-practice-run-migrations)

;;; aws-ai-practice-run-migrations.el ends here
