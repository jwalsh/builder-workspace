;;; sqlite-test.el --- Test SQLite functionality

;;; Commentary:
;; This file tests basic SQLite functionality in Emacs.

;;; Code:

(require 'sqlite)

(defun sqlite-test ()
  "Test basic SQLite functionality."
  (let ((db-file "/tmp/test.db"))
    (when (file-exists-p db-file)
      (delete-file db-file))
    (condition-case err
        (progn
          (sqlite-execute db-file "CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
          (sqlite-execute db-file "INSERT INTO test (name) VALUES ('test')")
          (let ((result (sqlite-select db-file "SELECT * FROM test")))
            (if result
                (message "SQLite test successful. Result: %S" result)
              (error "No results returned from SQLite query"))))
      (error (message "SQLite test failed: %S" err)))))

(sqlite-test)

(provide 'sqlite-test)

;;; sqlite-test.el ends here
