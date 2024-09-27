;;; 003_add_tags_support.el --- add_tags_support

;;; Commentary:
;; This migration add_tags_support

;;; Code:

(defun migrate-003-add_tags_support ()
  "(sqlite-execute aws-ai-practice-db-file
                        \"ALTER TABLE practice_data ADD COLUMN tags TEXT\")"
  (sqlite-execute aws-ai-practice-db-file
                        "ALTER TABLE practice_data ADD COLUMN tags TEXT"))

(provide 'migrate-003-add_tags_support)

;;; 003_add_tags_support.el ends here
