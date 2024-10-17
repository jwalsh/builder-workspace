# coordinator/utils/json_utils.py

import json
import logging
from typing import Optional
from json.decoder import JSONDecodeError

from pydantic import ValidationError
import re

from ..llm import llm_manager
from ..models import Task, TaskType, RFCState, ImplementationState

json_logger = logging.getLogger("json_extractor")


def extract_json_from_response(text: str) -> dict:
    json_logger.debug(f"Attempting to extract JSON from text: {text[:100]}...")

    def try_parse(json_str: str, stage: str) -> dict:
        try:
            parsed = json.loads(json_str)
            json_logger.info(f"Successfully parsed JSON at {stage}")
            return parsed
        except JSONDecodeError as e:
            json_logger.debug(f"JSON parse attempt failed at {stage}: {str(e)}")
            return None

    # Step 1: Try to parse the raw text
    parsed = try_parse(text, "raw text stage")
    if parsed:
        return parsed

    # Step 2: Try to extract JSON using regex
    json_logger.debug("Attempting to extract JSON using regex")
    json_match = re.search(r"(\{.*\})", text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        parsed = try_parse(json_str, "regex extraction stage")
        if parsed:
            return parsed

    # Step 3: Remove comments and try again
    json_logger.debug("Removing comments and attempting to parse again")
    text_no_comments = re.sub(r"//.*$", "", text, flags=re.MULTILINE)
    text_no_comments = re.sub(r"/\*.*?\*/", "", text_no_comments, flags=re.DOTALL)

    parsed = try_parse(text_no_comments, "comment removal stage")
    if parsed:
        return parsed

    # Step 4: Clean up whitespace and try one more time
    json_logger.debug("Cleaning up whitespace and attempting to parse again")
    text_clean = re.sub(r"\s+", "", text_no_comments)

    parsed = try_parse(text_clean, "whitespace cleanup stage")
    if parsed:
        return parsed

    # If all attempts fail, log detailed error information
    json_logger.error("Failed to parse JSON after all attempts.")
    json_logger.error(f"Raw text length: {len(text)}")
    json_logger.error(f"Full raw text: {text}")

    # Additional debugging information
    json_logger.error("Character frequency analysis:")
    char_freq = {char: text.count(char) for char in set(text)}
    for char, freq in sorted(char_freq.items(), key=lambda x: x[1], reverse=True):
        json_logger.error(f"'{char}': {freq}")

    json_logger.error("Last 10 characters:")
    json_logger.error(text[-10:])

    # Try to identify where the JSON might be truncated
    last_brace = text.rfind("}")
    if last_brace != -1:
        json_logger.error(f"Last closing brace found at position {last_brace}")
        json_logger.error(f"Text after last closing brace: {text[last_brace+1:]}")
    else:
        json_logger.error("No closing brace found in the text")

    return {}


async def correct_json_with_llm(json_text: str) -> Optional[Task]:
    task_type_values = ", ".join([f'"{t.value}"' for t in TaskType])
    rfc_state_values = ", ".join([f'"{s.value}"' for s in RFCState])
    implementation_state_values = ", ".join(
        [f'"{s.value}"' for s in ImplementationState]
    )

    prompt = f"""
    Please format the following text as a valid JSON object representing a Task, strictly adhering to this structure:

    {{
        "id": integer,
        "project_id": string,
        "title": string,
        "description": string,
        "status": string,
        "assigned_to": string (one of: task-decomposer, project-manager, code-architect, frontend-developer, backend-developer, database-specialist, devops-engineer, qa-tester, security-specialist, technical-writer),
        "priority": integer,
        "dependencies": array of strings,
        "task_type": string (one of: {task_type_values}),
        "rfc_state": string (one of: {rfc_state_values}) or null,
        "implementation_state": string (one of: {implementation_state_values}) or null,
        "review_comments": string or null,
        "approver": string or null,
        "parent_task_id": integer or null,
        "related_rfc_id": integer or null
    }}

    Ensure all string values are properly escaped, especially newlines in the description field. The JSON should be valid according to the provided structure. Do not include any comments or additional text before or after the JSON object.

    Here's the text to format:

    {json_text}
    """

    try:
        response = await llm_manager.run_llm_command(
            prompt=prompt, cache_key="json_correction", role="json_corrector"
        )

        # Attempt to parse the response as JSON
        try:
            corrected_json = json.loads(response)
        except JSONDecodeError:
            json_logger.error("LLM response is not valid JSON")
            return None

        # Validate the corrected JSON against the Task model
        try:
            validated_task = Task(**corrected_json)
            json_logger.info("JSON correction and validation successful")
            return validated_task
        except ValidationError as e:
            json_logger.error(f"Corrected JSON failed validation: {str(e)}")
            return None

    except Exception as e:
        json_logger.error(
            f"An unexpected error occurred during JSON correction: {str(e)}"
        )
        return None


async def extract_and_correct_json(text: str) -> Optional[Task]:
    json_logger.info("Attempting to extract and correct JSON")
    extracted_json = extract_json_from_response(text)

    if not extracted_json:
        json_logger.warning(
            "Failed to extract valid JSON, attempting correction with LLM"
        )
        return await correct_json_with_llm(text)

    try:
        validated_task = Task(**extracted_json)
        json_logger.info("Extracted JSON is valid")
        return validated_task
    except ValidationError:
        json_logger.warning("Extracted JSON is invalid, attempting correction with LLM")
        return await correct_json_with_llm(json.dumps(extracted_json))
