;;; 001_initial_aws_ai_practice.el --- Initial migration for aws-ai-practice

;;; Commentary:
;; This migration creates the initial structure for aws-ai-practice using file-based storage.

;;; Code:

(defun migrate-001-initial-aws-ai-practice ()
  "Create the initial aws-ai-practice structure."
  (let* ((db-file (expand-file-name "aws-ai-practice-db.el"
                                    (file-name-directory load-file-name)))
         (db-contents (if (file-exists-p db-file)
                          (with-temp-buffer
                            (insert-file-contents db-file)
                            (read (buffer-string)))
                        '((practice-data . nil)))))
    ;; Add initial structure if not present
    (unless (assq 'practice-data db-contents)
      (setq db-contents (cons '(practice-data . nil) db-contents)))
    
    ;; Save updated contents
    (with-temp-file db-file
      (prin1 db-contents (current-buffer)))
    
    (message "Initial aws-ai-practice structure created successfully.")))

(provide 'migrate-001-initial-aws-ai-practice)

;;; 001_initial_aws_ai_practice.el ends here
