(ns deprecation-detective.core
  (:require [babashka.cli :as cli]
            [babashka.fs :as fs]
            [clojure.java.io :as io]
            [clojure.string :as str]
            [cheshire.core :as json]))

;; Deprecated pattern database
(def deprecation-patterns
  [{:id "py-distutils"
    :lang "python"
    :pattern #"(?i)from\s+distutils"
    :message "distutils is deprecated since Python 3.10, use setuptools"
    :severity "high"
    :replacement "setuptools"}
   {:id "py-imp"
    :lang "python"
    :pattern #"(?i)import\s+imp\b"
    :message "imp module deprecated since Python 3.4, use importlib"
    :severity "high"
    :replacement "importlib"}
   {:id "py-optparse"
    :lang "python"
    :pattern #"(?i)import\s+optparse"
    :message "optparse deprecated since Python 3.2, use argparse"
    :severity "medium"
    :replacement "argparse"}
   {:id "py-cgi"
    :lang "python"
    :pattern #"(?i)import\s+cgi\b"
    :message "cgi module deprecated since Python 3.11"
    :severity "medium"
    :replacement "urllib.parse"}
   {:id "py-unittest-makesuite"
    :lang "python"
    :pattern #"(?i)unittest\.makeSuite"
    :message "unittest.makeSuite deprecated since Python 3.11"
    :severity "medium"
    :replacement "unittest.TestLoader.loadTestsFromTestCase"}
   {:id "js-var"
    :lang "javascript"
    :pattern #"\bvar\s+"
    :message "var is discouraged in modern JS, use let/const"
    :severity "low"
    :replacement "let/const"}
   {:id "js-arguments"
    :lang "javascript"
    :pattern #"\barguments\b"
    :message "arguments object is discouraged, use rest parameters"
    :severity "low"
    :replacement "...args"}
   {:id "node-domain"
    :lang "javascript"
    :pattern #"require\(['\"]domain['\"]\)"
    :message "domain module deprecated in Node.js"
    :severity "high"
    :replacement "async_hooks"}
   {:id "java-date"
    :lang "java"
    :pattern #"new\s+Date\(\)"
    :message "java.util.Date constructors deprecated, use java.time"
    :severity "medium"
    :replacement "java.time.Instant.now()"}
   {:id "go-ioutil"
    :lang "go"
    :pattern #"\"io/ioutil\""
    :message "io/ioutil deprecated since Go 1.16, use io and os"
    :severity "high"
    :replacement "io, os"}])

(defn file-extension [path]
  (let [name (str (fs/file-name path))]
    (when-let [idx (str/last-index-of name ".")]
      (subs name (inc idx)))))

(def ext->lang
  {"py" "python" "pyw" "python"
   "js" "javascript" "mjs" "javascript" "cjs" "javascript" "ts" "javascript"
   "java" "java" "kt" "java"
   "go" "go"
   "rb" "ruby" "rs" "rust" "clj" "clojure"})

(defn scan-file [path]
  (let [ext (file-extension path)
        lang (get ext->lang ext)
        content (slurp (str path))
        lines (str/split-lines content)]
    (when lang
      (->> deprecation-patterns
           (filter #(= (:lang %) lang))
           (mapcat (fn [pattern]
                     (->> lines
                          (map-indexed vector)
                          (filter (fn [[_ line]] (re-find (:pattern pattern) line)))
                          (map (fn [[line-num line]]
                                 {:file (str path)
                                  :line (inc line-num)
                                  :id (:id pattern)
                                  :severity (:severity pattern)
                                  :message (:message pattern)
                                  :replacement (:replacement pattern)
                                  :match (str/trim line)})))))))))

(defn scan-directory [dir opts]
  (let [extensions (set (keys ext->lang))
        files (->> (fs/glob dir "**")
                   (filter fs/regular-file?)
                   (filter #(contains? extensions (file-extension %)))
                   (remove #(str/includes? (str %) "node_modules"))
                   (remove #(str/includes? (str %) ".git"))
                   (remove #(str/includes? (str %) "venv")))]
    (->> files
         (mapcat scan-file)
         (sort-by (juxt :severity :file :line)))))

(defn format-text [findings]
  (if (empty? findings)
    "No deprecations found."
    (str/join "\n"
      (concat
        [(format "Found %d deprecation(s):\n" (count findings))]
        (map (fn [{:keys [file line severity message replacement match]}]
               (format "  %s:%d [%s] %s\n    -> Replace with: %s\n    |  %s"
                       file line (str/upper-case severity) message replacement match))
             findings)
        [""
         (format "Summary: %d high, %d medium, %d low"
                 (count (filter #(= (:severity %) "high") findings))
                 (count (filter #(= (:severity %) "medium") findings))
                 (count (filter #(= (:severity %) "low") findings)))]))))

(defn format-json [findings]
  (json/generate-string
    {:total (count findings)
     :by-severity {:high (count (filter #(= (:severity %) "high") findings))
                   :medium (count (filter #(= (:severity %) "medium") findings))
                   :low (count (filter #(= (:severity %) "low") findings))}
     :findings findings}
    {:pretty true}))

(def cli-spec
  {:dir {:desc "Directory to scan"
         :default "."
         :alias :d}
   :format {:desc "Output format: text, json, edn"
            :default "text"
            :alias :f}
   :severity {:desc "Minimum severity: low, medium, high"
              :default "low"
              :alias :s}
   :help {:desc "Show help"
          :alias :h
          :coerce :boolean}})

(defn -main [& args]
  (let [opts (cli/parse-opts args {:spec cli-spec})
        _ (when (:help opts)
            (println "DeprecationDetective — find deprecated code patterns")
            (println)
            (println (cli/format-opts {:spec cli-spec}))
            (System/exit 0))
        severity-rank {"high" 3 "medium" 2 "low" 1}
        min-severity (get severity-rank (:severity opts) 1)
        findings (->> (scan-directory (:dir opts) opts)
                      (filter #(>= (get severity-rank (:severity %) 0) min-severity)))]
    (println
      (case (:format opts)
        "json" (format-json findings)
        "edn" (pr-str findings)
        (format-text findings)))
    (System/exit (if (seq findings) 1 0))))

(when (= *file* (System/getProperty "babashka.file"))
  (apply -main *command-line-args*))
