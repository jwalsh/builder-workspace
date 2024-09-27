import json
import re
import logging
from json.decoder import JSONDecodeError

json_logger = logging.getLogger('json_extractor')

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
    json_match = re.search(r'(\{.*\})', text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        parsed = try_parse(json_str, "regex extraction stage")
        if parsed:
            return parsed

    # Step 3: Remove comments and try again
    json_logger.debug("Removing comments and attempting to parse again")
    text_no_comments = re.sub(r'//.*$', '', text, flags=re.MULTILINE)
    text_no_comments = re.sub(r'/\*.*?\*/', '', text_no_comments, flags=re.DOTALL)
    
    parsed = try_parse(text_no_comments, "comment removal stage")
    if parsed:
        return parsed

    # Step 4: Clean up whitespace and try one more time
    json_logger.debug("Cleaning up whitespace and attempting to parse again")
    text_clean = re.sub(r'\s+', '', text_no_comments)
    
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
    last_brace = text.rfind('}')
    if last_brace != -1:
        json_logger.error(f"Last closing brace found at position {last_brace}")
        json_logger.error(f"Text after last closing brace: {text[last_brace+1:]}")
    else:
        json_logger.error("No closing brace found in the text")

    return {}
