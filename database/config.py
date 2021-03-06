from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 3306
    user: str = "tarfindb"
    password: str = "123123"
    dialect: str = "mysql"
    driver: str = "pymysql"
