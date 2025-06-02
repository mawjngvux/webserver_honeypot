import logging
from config.config import Config
import json
import re
import uuid
from datetime import datetime

def honeypot_web_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.HONEYPOT_WEB_SERVER_LOG_FILE),
            logging.StreamHandler()
        ]
    )

def sanitize_headers(headers):
    sanitized = {}
    for k, v in headers.items():
        clean_key = re.sub(r'[\r\n]', '', k)
        clean_val = re.sub(r'[\r\n]', '', v)
        sanitized[clean_key] = clean_val
    return sanitized

def log_request(req, response_status=None):
    if req.method in ["POST", "PUT", "PATCH"]:
        form_data = req.form.to_dict(flat=False)
    else:
        form_data = {}

    record = {
        "request_id": str(uuid.uuid4()),
        "remoteaddr": req.remote_addr,
        "method": req.method,
        "requesturi": req.full_path,    # full path bao gồm query string
        "headers": sanitize_headers(req.headers),
        "query_params": req.args.to_dict(flat=False),
        "useragent": req.user_agent.string,
        "postform": form_data,
        "eventtime": datetime.utcnow().isoformat() + "Z",
        "response_status": response_status
    }

    with open(Config.LOG_REQUEST, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str, ensure_ascii=False) + "\n")