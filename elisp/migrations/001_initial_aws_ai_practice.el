;;; 001_initial_aws_ai_practice.el --- Initial migration for aws-ai-practice

;;; Commentary:
;; This migration creates the initial structure for aws-ai-practice.el

;;; Code:

(defun migrate-001-initial-aws-ai-practice ()
  "Create the initial aws-ai-practice.el file."
  (let ((file-path (expand-file-name "aws-ai-practice.el" 
                                     (file-name-directory 
                                      (directory-file-name 
                                       (file-name-directory load-file-name))))))
    (with-temp-file file-path
      (insert ";;; aws-ai-practice.el --- Support for AWS AI Fundamentals practice questions

;;; Commentary:
;; This module provides support for practicing AWS AI Fundamentals questions
;; in org-mode files, including tracking of attempts and correctness in an SQLite database.

;;; Code:

(require 'org)
(require 'sqlite)

(defvar aws-ai-practice-db-file \"~/.emacs.d/aws-ai-practice.db\"
  \"Path to the SQLite database file for AWS AI practice.\")

(defvar-local aws-ai-practice-hide-properties t
  \"Whether to hide property drawers in AWS AI practice files.\")

(defun aws-ai-practice-init-db ()
  \"Initialize the SQLite database for AWS AI practice.\"
  (unless (file-exists-p aws-ai-practice-db-file)
    (with-temp-buffer
      (sqlite-execute aws-ai-practice-db-file
                      \"CREATE TABLE IF NOT EXISTS practice_data (
                         user TEXT,
                         file TEXT,
                         question_id TEXT,
                         attempts INTEGER,
                         correct_attempts INTEGER,
                         last_attempted TEXT,
                         PRIMARY KEY (user, file, question_id)
                       )\"))))

(defun aws-ai-practice-mode-init ()
  \"Initialize AWS AI practice mode.\"
  (aws-ai-practice-init-db)
  (aws-ai-practice-update-property-visibility))

(define-minor-mode aws-ai-practice-mode
  \"Minor mode for AWS AI Fundamentals practice questions.\"
  :lighter \" AWS-AI\"
  :keymap (let ((map (make-sparse-keymap)))
            (define-key map (kbd \"C-c C-c\") 'aws-ai-practice-check-answer)
            (define-key map (kbd \"C-c C-e\") 'aws-ai-practice-show-explanation)
            (define-key map (kbd \"C-c C-s\") 'aws-ai-practice-show-stats)
            (define-key map (kbd \"C-c C-t\") 'aws-ai-practice-toggle-property-visibility)
            (define-key map (kbd \"C-c C-a\") 'aws-ai-practice-set-answer)
            (define-key map (kbd \"C-c C-r\") 'aws-ai-practice-reset-all-answers)
            map))

(add-hook 'org-mode-hook
          (lambda ()
            (when (and buffer-file-name
                       (string-match \"aif-c01-practice-\" (buffer-file-name)))
              (aws-ai-practice-mode 1)
              (aws-ai-practice-mode-init))))

(provide 'aws-ai-practice)

;;; aws-ai-practice.el ends here
"))))

(provide 'migrate-001-initial-aws-ai-practice)

;;; 001_initial_aws_ai_practice.el ends here
