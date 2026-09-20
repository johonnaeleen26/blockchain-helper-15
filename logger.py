import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str = "blockchain_helper",
    log_file: str = "logs/blockchain.log",
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    level: int = logging.INFO,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def log_transaction_event(
    logger: logging.Logger, tx_hash: str, status: str, details: str = ""
) -> None:
    msg = f"TxHash: {tx_hash} | Status: {status}"
    if details:
        msg += f" | Details: {details}"
    logger.info(msg)
