;;; 004_add_difficulty_level.el --- add_difficulty_level

;;; Commentary:
;; This migration add_difficulty_level

;;; Code:

(defun migrate-004-add_difficulty_level ()
  "(sqlite-execute aws-ai-practice-db-file
                        "ALTER TABLE practice_data ADD COLUMN difficulty_level INTEGER DEFAULT 1")"
  (sqlite-execute aws-ai-practice-db-file
                        "ALTER TABLE practice_data ADD COLUMN difficulty_level INTEGER DEFAULT 1"))

(provide 'migrate-004-add_difficulty_level)

;;; 004_add_difficulty_level.el ends here
