# database_config.py
server = '石头剪刀布\\SQLEXPRESS'
database = '研究生招生目录'
#username = 'YOUR_USERNAME'  # 如果使用Windows身份验证，这可能不需要
#password = 'YOUR_PASSWORD'  # 如果使用Windows身份验证，这可能不需要
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'  # 如果使用Windows身份验证，使用'yes'；否则，使用'no'并提供username和password
)