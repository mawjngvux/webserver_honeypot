class Config:
    DEBUG = True
    HONEYPOT_WEB_SERVER_LOG_FILE = "logging_system/log_files/honeypot_web_server.log"
    LOG_REQUEST = "logging_system/log_files/log_request.json"
    UPLOAD_DIR = 'honeypot_web_server/uploads/'
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    MONGOURI = "mongodb://localhost:27017/" 
    MONGO_DB_NAME = "webserverhoneypotdb"