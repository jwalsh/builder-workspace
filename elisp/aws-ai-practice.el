;;; aws-ai-practice.el --- Support for AWS AI Fundamentals practice questions

;;; Commentary:
;; This module provides support for practicing AWS AI Fundamentals questions
;; in org-mode files, including tracking of attempts and correctness in an SQLite database.

;;; Code:

(require 'org)
(require 'sqlite)

(defvar aws-ai-practice-db-file
  (expand-file-name "~/.emacs.d/aws-ai-practice.db")
  "Path to the SQLite database file for AWS AI practice.")

(defvar-local aws-ai-practice-hide-properties t
  "Whether to hide property drawers in AWS AI practice files.")

(defun aws-ai-practice-ensure-db ()
  "Ensure the SQLite database exists and is initialized."
  (unless (file-exists-p aws-ai-practice-db-file)
    (make-empty-file aws-ai-practice-db-file))
  (condition-case err
      (sqlite-execute aws-ai-practice-db-file
                      "CREATE TABLE IF NOT EXISTS practice_data (
                         user TEXT,
                         file TEXT,
                         question_id TEXT,
                         attempts INTEGER,
                         correct_attempts INTEGER,
                         last_attempted TEXT,
                         PRIMARY KEY (user, file, question_id)
                       )")
    (error
     (message "Error initializing database: %s" (error-message-string err))
     (signal (car err) (cdr err)))))

(defun aws-ai-practice-toggle-property-visibility ()
  "Toggle visibility of property drawers in the current buffer."
  (interactive)
  (setq aws-ai-practice-hide-properties (not aws-ai-practice-hide-properties))
  (aws-ai-practice-update-property-visibility)
  (message "Property drawers are now %s" 
           (if aws-ai-practice-hide-properties "hidden" "visible")))

(defun aws-ai-practice-update-property-visibility ()
  "Update visibility of property drawers based on current setting."
  (save-excursion
    (goto-char (point-min))
    (while (re-search-forward "^[ \t]*:PROPERTIES:" nil t)
      (let ((drawer-begin (match-beginning 0))
            (drawer-end (save-excursion
                          (re-search-forward "^[ \t]*:END:" nil t)
                          (point))))
        (when drawer-end
          (outline-flag-region drawer-begin drawer-end aws-ai-practice-hide-properties))))))

(defun aws-ai-practice-set-answer (index)
  "Set the answer for the current question to the option at INDEX."
  (interactive "nEnter the answer number (1-4): ")
  (save-excursion
    (org-back-to-heading t)
    (let ((options (org-entry-get-multivalued-property nil "ITEM")))
      (when (and (>= index 1) (<= index (length options)))
        (dotimes (i (length options))
          (setf (nth i options) (replace-regexp-in-string "\\[[ X]\\]" "[ ]" (nth i options))))
        (setf (nth (1- index) options) (replace-regexp-in-string "\\[ \\]" "[X]" (nth (1- index) options)))
        (org-entry-put-multivalued-property nil "ITEM" options)))))

(defun aws-ai-practice-check-answer ()
  "Check the answer for the current question and provide feedback."
  (interactive)
  (aws-ai-practice-ensure-db)
  (save-excursion
    (org-back-to-heading t)
    (let* ((correct-answer (org-entry-get nil "ANSWER"))
           (explanation (org-entry-get nil "EXPLANATION"))
           (options (org-entry-get-multivalued-property nil "ITEM"))
           (selected (cl-position "[X]" options :test 'string-match))
           (correct (cl-position correct-answer options :test 'string=))
           (question-id (org-id-get-create))
           (user (user-login-name))
           (file (buffer-file-name))
           (db-data (car (sqlite-select aws-ai-practice-db-file
                                        "SELECT attempts, correct_attempts FROM practice_data
                                         WHERE user = ? AND file = ? AND question_id = ?"
                                        user file question-id)))
           (attempts (if db-data (+ 1 (nth 0 db-data)) 1))
           (correct-attempts (if db-data (nth 1 db-data) 0)))
      (when (eq selected correct)
        (setq correct-attempts (1+ correct-attempts)))
      (condition-case err
          (sqlite-execute aws-ai-practice-db-file
                          "INSERT OR REPLACE INTO practice_data
                           (user, file, question_id, attempts, correct_attempts, last_attempted)
                           VALUES (?, ?, ?, ?, ?, datetime('now'))"
                          user file question-id attempts correct-attempts)
        (error
         (message "Error updating database: %s" (error-message-string err))))
      (if (eq selected correct)
          (message "Correct! %s" explanation)
        (message "Incorrect. The correct answer is: %s. %s" correct-answer explanation)))))

(defun aws-ai-practice-show-explanation ()
  "Show the explanation and stats for the current question."
  (interactive)
  (aws-ai-practice-ensure-db)
  (save-excursion
    (org-back-to-heading t)
    (let* ((explanation (org-entry-get nil "EXPLANATION"))
           (question-id (org-id-get-create))
           (user (user-login-name))
           (file (buffer-file-name))
           (db-data (car (sqlite-select aws-ai-practice-db-file
                                        "SELECT attempts, correct_attempts, last_attempted
                                         FROM practice_data
                                         WHERE user = ? AND file = ? AND question_id = ?"
                                        user file question-id))))
      (if db-data
          (let ((attempts (nth 0 db-data))
                (correct-attempts (nth 1 db-data))
                (last-attempted (nth 2 db-data)))
            (message "Explanation: %s\nLast attempted: %s\nAttempts: %d\nCorrectness: %.2f%%"
                     explanation last-attempted attempts
                     (* 100.0 (/ correct-attempts (float attempts)))))
        (message "Explanation: %s\nNot attempted yet." explanation)))))

(defun aws-ai-practice-show-stats ()
  "Show statistics for the current practice file."
  (interactive)
  (aws-ai-practice-ensure-db)
  (let* ((user (user-login-name))
         (file (buffer-file-name))
         (stats (car (sqlite-select aws-ai-practice-db-file
                                    "SELECT COUNT(*) as total,
                                            SUM(CASE WHEN attempts > 0 THEN 1 ELSE 0 END) as attempted,
                                            SUM(attempts) as total_attempts,
                                            SUM(correct_attempts) as total_correct
                                     FROM practice_data
                                     WHERE user = ? AND file = ?"
                                    user file))))
    (if stats
        (let ((total (nth 0 stats))
              (attempted (nth 1 stats))
              (total-attempts (nth 2 stats))
              (total-correct (nth 3 stats)))
          (message "Progress: %d/%d questions attempted (%.2f%%)\nTotal attempts: %d\nOverall correctness: %.2f%%"
                   attempted total (* 100.0 (/ attempted (float total)))
                   total-attempts
                   (if (> total-attempts 0)
                       (* 100.0 (/ total-correct (float total-attempts)))
                     0.0)))
      (message "No statistics available for this file."))))

(defun aws-ai-practice-reset-all-answers ()
  "Reset all answers and stats in the current practice file."
  (interactive)
  (when (yes-or-no-p "Are you sure you want to reset all answers and stats? ")
    (aws-ai-practice-ensure-db)
    (let ((user (user-login-name))
          (file (buffer-file-name)))
      (condition-case err
          (sqlite-execute aws-ai-practice-db-file
                          "DELETE FROM practice_data WHERE user = ? AND file = ?"
                          user file)
        (error
         (message "Error resetting answers in database: %s" (error-message-string err)))))
    (org-map-entries
     (lambda ()
       (let ((options (org-entry-get-multivalued-property nil "ITEM")))
         (when options
           (setq options (mapcar (lambda (opt) (replace-regexp-in-string "\\[X\\]" "[ ]" opt)) options))
           (org-entry-put-multivalued-property nil "ITEM" options))))
     t 'file)
    (message "All answers and stats have been reset.")))

(defun aws-ai-practice-mode-init ()
  "Initialize AWS AI practice mode."
  (aws-ai-practice-ensure-db)
  (aws-ai-practice-update-property-visibility))

(define-minor-mode aws-ai-practice-mode
  "Minor mode for AWS AI Fundamentals practice questions."
  :lighter " AWS-AI"
  :keymap (let ((map (make-sparse-keymap)))
            (define-key map (kbd "C-c C-c") 'aws-ai-practice-check-answer)
            (define-key map (kbd "C-c C-e") 'aws-ai-practice-show-explanation)
            (define-key map (kbd "C-c C-s") 'aws-ai-practice-show-stats)
            (define-key map (kbd "C-c C-t") 'aws-ai-practice-toggle-property-visibility)
            (define-key map (kbd "C-c C-a") 'aws-ai-practice-set-answer)
            (define-key map (kbd "C-c C-r") 'aws-ai-practice-reset-all-answers)
            map))

(add-hook 'org-mode-hook
          (lambda ()
            (when (and buffer-file-name
                       (string-match "aif-c01-practice-" (buffer-file-name)))
              (aws-ai-practice-mode 1)
              (aws-ai-practice-mode-init))))

(provide 'aws-ai-practice)

;;; aws-ai-practice.el ends here
