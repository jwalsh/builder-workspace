;;; aws-ai-practice-updater.el --- Update script for aws-ai-practice.el

;;; Commentary:
;; This script updates the aws-ai-practice.el file by adding or updating defuns.

;;; Code:

(require 'cl-lib)

(defvar aws-ai-practice-file "~/.emacs.d/lisp/aws-ai-practice/aws-ai-practice.el"
  "Path to the aws-ai-practice.el file.")

(defvar aws-ai-practice-new-defuns
  '(
    (aws-ai-practice-init-db
     "Initialize the SQLite database for AWS AI practice and run migrations."
     (unless (file-exists-p aws-ai-practice-db-file)
       (with-temp-buffer
         (sqlite-execute aws-ai-practice-db-file "SELECT 1")))
     (aws-ai-practice-run-migrations))

    (aws-ai-practice-get-user
     "Get the current user's identifier."
     (user-login-name))

    (aws-ai-practice-get-question-id
     "Get a unique identifier for the current question."
     (org-id-get-create))

    ;; Add more defuns here as needed
    )
  "List of new or updated defuns to add to aws-ai-practice.el")

(defun aws-ai-practice-parse-defun (defun-form)
  "Parse a DEFUN-FORM and return a list of (name docstring body)."
  (let ((name (nth 1 defun-form))
        (docstring (nth 4 defun-form))
        (body (nthcdr 5 defun-form)))
    (list name docstring body)))

(defun aws-ai-practice-update-file (&optional input-file output-file)
  "Update the aws-ai-practice.el file with new or updated defuns.
Optional INPUT-FILE and OUTPUT-FILE can be specified."
  (let ((input (or input-file aws-ai-practice-file))
        (output (or output-file aws-ai-practice-file)))
    (with-current-buffer (find-file-noselect input)
      ;; Create a backup
      (write-region (point-min) (point-max) (concat input ".bak"))
      
      (goto-char (point-min))
      (let ((existing-defuns (make-hash-table :test 'equal))
            (updated-content ""))
        ;; First pass: collect existing defuns
        (while (re-search-forward "^(defun\\s-+\\([^(]+\\)" nil t)
          (let ((defun-name (match-string 1)))
            (puthash (intern defun-name) t existing-defuns)))
        
        ;; Second pass: update or add defuns
        (goto-char (point-min))
        (while (not (eobp))
          (if (looking-at "^(defun\\s-+\\([^(]+\\)")
              (let* ((defun-name (intern (match-string 1)))
                     (new-defun (assoc defun-name aws-ai-practice-new-defuns)))
                (if new-defun
                    (progn
                      (delete-region (point) (progn (forward-sexp) (point)))
                      (insert (aws-ai-practice-format-defun new-defun))
                      (setq aws-ai-practice-new-defuns
                            (remove new-defun aws-ai-practice-new-defuns)))
                  (setq updated-content (concat updated-content
                                                (buffer-substring (point)
                                                                  (progn (forward-sexp) (point)))
                                                "\n"))))
            (setq updated-content (concat updated-content
                                          (buffer-substring (point) (progn (forward-line) (point)))))))
        
        ;; Add any remaining new defuns
        (dolist (new-defun aws-ai-practice-new-defuns)
          (setq updated-content (concat updated-content
                                        (aws-ai-practice-format-defun new-defun)
                                        "\n")))
        
        ;; Update buffer content
        (erase-buffer)
        (insert updated-content)
        (write-file output)))
    (message "Updated aws-ai-practice.el successfully. Backup created.")))

(defun aws-ai-practice-update-file ()
  "Update the aws-ai-practice.el file with new or updated defuns."
  (with-current-buffer (find-file-noselect aws-ai-practice-file)
    (goto-char (point-min))
    (let ((existing-defuns (make-hash-table :test 'equal))
          (updated-content ""))
      ;; First pass: collect existing defuns
      (while (re-search-forward "^(defun\\s-+\\([^(]+\\)" nil t)
        (let ((defun-name (match-string 1)))
          (puthash (intern defun-name) t existing-defuns)))
      
      ;; Second pass: update or add defuns
      (goto-char (point-min))
      (while (not (eobp))
        (if (looking-at "^(defun\\s-+\\([^(]+\\)")
            (let* ((defun-name (intern (match-string 1)))
                   (new-defun (assoc defun-name aws-ai-practice-new-defuns)))
              (if new-defun
                  (progn
                    (delete-region (point) (progn (forward-sexp) (point)))
                    (insert (aws-ai-practice-format-defun new-defun))
                    (setq aws-ai-practice-new-defuns
                          (remove new-defun aws-ai-practice-new-defuns)))
                (setq updated-content (concat updated-content
                                              (buffer-substring (point)
                                                                (progn (forward-sexp) (point)))
                                              "\n"))))
          (setq updated-content (concat updated-content
                                        (buffer-substring (point) (progn (forward-line) (point)))))))
      
      ;; Add any remaining new defuns
      (dolist (new-defun aws-ai-practice-new-defuns)
        (setq updated-content (concat updated-content
                                      (aws-ai-practice-format-defun new-defun)
                                      "\n")))
      
      ;; Update buffer content
      (erase-buffer)
      (insert updated-content)
      (save-buffer))
    (message "Updated aws-ai-practice.el successfully.")))

(defun aws-ai-practice-format-defun (defun-spec)
  "Format a DEFUN-SPEC into a string."
  (let ((name (nth 0 defun-spec))
        (docstring (nth 1 defun-spec))
        (body (nthcdr 2 defun-spec)))
    (format "(defun %s ()\n  \"%s\"\n  %s)\n"
            name docstring (mapconcat #'prin1-to-string body "\n  "))))

(aws-ai-practice-update-file)

(provide 'aws-ai-practice-updater)

;;; aws-ai-practice-updater.el ends here
