from snowflake import connector


def sfconnect():
    conn=connector.connect(
        account='lq20748.europe-west2.gcp',
        user='tbc',
        password='tbc',
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC'
    )
    return conn

