;;; aws-ai-practice-tests.el --- Tests for AWS AI Practice module

;;; Commentary:
;; This file contains ERT tests for the AWS AI Practice module.

;;; Code:

(require 'ert)
(require 'aws-ai-practice)

(ert-deftest aws-ai-practice-test-database-initialization ()
  "Test that the database is initialized correctly."
  (should (file-exists-p aws-ai-practice-db-file))
  (should (aws-ai-practice-ensure-db))
  (let ((tables (sqlite-select aws-ai-practice-db-file "SELECT name FROM sqlite_master WHERE type='table'")))
    (should (member '("practice_data") tables))
    (should (member '("completed_migrations") tables))
    (should (member '("categories") tables))))

(ert-deftest aws-ai-practice-test-migrations ()
  "Test that migrations are applied correctly."
  (aws-ai-practice-run-migrations)
  (let ((columns (sqlite-select aws-ai-practice-db-file "PRAGMA table_info(practice_data)")))
    (should (member '("tags") (mapcar (lambda (col) (nth 1 col)) columns)))
    (should (member '("difficulty_level") (mapcar (lambda (col) (nth 1 col)) columns))))
  (let ((tables (sqlite-select aws-ai-practice-db-file "SELECT name FROM sqlite_master WHERE type='table'")))
    (should (member '("categories") tables))))

(ert-deftest aws-ai-practice-test-answer-checking ()
  "Test the answer checking functionality."
  (with-temp-buffer
    (insert "* Question\n:PROPERTIES:\n:ANSWER: B\n:EXPLANATION: Test explanation\n:END:\n- [ ] A\n- [ ] B\n- [ ] C\n- [ ] D\n")
    (goto-char (point-min))
    (org-mode)
    (aws-ai-practice-mode 1)
    (aws-ai-practice-set-answer 2)
    (should (string-match-p "\\[X\\] B" (buffer-string)))
    (aws-ai-practice-check-answer)
    (should (string-match-p "Correct!" (buffer-substring-no-properties (point-min) (point-max))))))

(ert-deftest aws-ai-practice-test-stats ()
  "Test the statistics functionality."
  (aws-ai-practice-reset-all-answers)
  (with-temp-buffer
    (insert "* Question 1\n:PROPERTIES:\n:ANSWER: A\n:END:\n- [ ] A\n- [ ] B\n")
    (goto-char (point-min))
    (org-mode)
    (aws-ai-practice-mode 1)
    (aws-ai-practice-set-answer 1)
    (aws-ai-practice-check-answer)
    (let ((stats-output (with-output-to-string (aws-ai-practice-show-stats))))
      (should (string-match-p "1/1 questions attempted" stats-output))
      (should (string-match-p "100.00%" stats-output)))))

(provide 'aws-ai-practice-tests)

;;; aws-ai-practice-tests.el ends here
