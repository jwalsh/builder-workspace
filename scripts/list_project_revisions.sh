sqlite3 -header -csv tasks.db "
SELECT 
    pv.id,
    json_extract(pv.definition, '$.llm_config.provider') AS llm_provider,
    CASE 
        WHEN json_extract(pv.definition, '$.llm_config.provider') = 'ollama' 
        THEN json_extract(pv.definition, '$.llm_config.ollama_model')
        WHEN json_extract(pv.definition, '$.llm_config.provider') = 'claude' 
        THEN json_extract(pv.definition, '$.llm_config.claude_model')
        ELSE json_extract(pv.definition, '$.llm_config.' || json_extract(pv.definition, '$.llm_config.provider') || '_model')
    END AS llm_model,
    json_extract(pv.definition, '$.name') AS project_name,
    substr(json_extract(pv.definition, '$.description'), 1, 50) || '...' AS truncated_description,
    pv.created_at
FROM 
    project_versions pv
ORDER BY 
    pv.created_at DESC
LIMIT 20;
"
