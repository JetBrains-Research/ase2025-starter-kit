#!/usr/bin/env python3
import json
import jsonschema
import argparse
from pathlib import Path

# Schema for validating submission format
SUBMISSION_SCHEMA = {
    "type": "object",
    "required": ["repo_name", "composed_context", "file_prefix", "completion_snippet", "file_suffix"],
    "properties": {
        "repo_name": {"type": "string"},
        "composed_context": {"type": "string"},
        "file_prefix": {"type": "string"},
        "completion_snippet": {"type": "string"},
        "file_suffix": {"type": "string"}
    }
}

def validate_submission(input_path):
    """Validate the submission JSONL file format."""
    print(f"Validating submission file: {input_path}")
    
    try:
        with open(input_path, 'r') as f:
            line_count = 0
            for line_num, line in enumerate(f, 1):
                try:
                    entry = json.loads(line)
                    jsonschema.validate(instance=entry, schema=SUBMISSION_SCHEMA)
                    line_count += 1
                except json.JSONDecodeError:
                    print(f"❌ Error: Invalid JSON on line {line_num}")
                    return False
                except jsonschema.exceptions.ValidationError as e:
                    print(f"❌ Error: Validation error on line {line_num}: {str(e)}")
                    return False
        
        if line_count == 0:
            print("❌ Error: Submission file is empty")
            return False
            
        print(f"✅ Success: Validated {line_count} entries")
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_path}")
        return False
    except Exception as e:
        print(f"❌ Error: Unexpected error: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Validate competition submission format")
    parser.add_argument("--input", type=str, required=True, help="Path to submission JSONL file")
    args = parser.parse_args()
    
    success = validate_submission(args.input)
    if not success:
        exit(1)

if __name__ == "__main__":
    main() 