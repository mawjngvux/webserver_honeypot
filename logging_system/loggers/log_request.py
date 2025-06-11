from config.config import Config
import json
import re
import uuid
from datetime import datetime
from database.mongo import get_collection

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
        # 1. Metadata / định danh
        "request_id": str(uuid.uuid4()),
        "event_time": datetime.utcnow().isoformat() + "Z",
        
        # 2. Thông tin client
        "remote_addr": req.remote_addr,
        "user_agent": req.user_agent.string,

        # 3. Thông tin HTTP Request
        "method": req.method,
        "request_url": req.full_path,  # bao gồm query string
        "query_params": req.args.to_dict(flat=False),
        "headers": sanitize_headers(req.headers),
        "post_form": form_data,

        # 4. Thông tin phản hồi
        "response_status": response_status
    }
    
    logs = get_collection("requests")
    logs.insert_one(record)