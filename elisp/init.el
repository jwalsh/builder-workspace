;; Add AWS AI Practice to load path if the directory exists
(let ((aws-ai-practice-dir "~/.emacs.d/lisp/aws-ai-practice"))
  (when (file-directory-p aws-ai-practice-dir)
    (add-to-list 'load-path aws-ai-practice-dir)
    
    ;; Require the module
    (require 'aws-ai-practice)
    (require 'aws-ai-practice-migration-checker)

    ;; Optional: Create an autoload
    (autoload 'aws-ai-practice-mode "aws-ai-practice" "AWS AI Practice mode" t)
    ;; Optional: Automatically activate for certain files
    (add-to-list 'auto-mode-alist '("aif-c01-practice-.*\\.org\\'" . aws-ai-practice-mode))))
