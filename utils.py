def engine_func(user, passw, host, port, database, platform):
    from sqlalchemy.engine import create_engine
    uri = '{platform}://{user}:{passw}@{host}:{port}/{database}'
    if platform == 'mysql':
        uri = uri.format(platform='mysql+mysqlconnector',
                         user=user,
                         passw=passw,
                         host=host,
                         port=port,
                         database=database)
        return create_engine(uri)
    elif platform == 'postgresql':
        uri = uri.format(platform='postgresql',
                         user=user,
                         passw=passw,
                         host=host,
                         port=port,
                         database=database)
        return create_engine(uri)


def createdAt_n_days_func( n_days):
    from datetime import timedelta, datetime
    result = datetime.today() - timedelta(days=n_days)
    return result


def fetch_filter(table, engine, filter):
    from sqlalchemy import select
    
    import numpy as np
    
    with engine.connect() as conn:
        result = conn.execute(select(table).where(filter)).all()
    
    return np.array([i._asdict() for i in result])



def migrate_data(table, engine, data):
    import numpy as np
    from sqlalchemy.dialects.mysql import insert
    import uuid
    
    inserted_row = 0
    updated_row = 0 
    chunk_size = 5000 
    data_chunk = [ data[i:i+chunk_size] for i in range(0,len(data),chunk_size)]
    
    with engine.connect() as conn:
        for data in data_chunk:
            for rows in data:
                row = dict()
                for key,val in rows.items():
                    if type(val) == uuid.UUID :
                        row[key] = str(val)
                    else:
                        row[key] = val
                
                insert_stmt = insert(table).values(row)
                update_stmt = insert(table).values(row).on_duplicate_key_update(row)
                # insert(table).values(i).prefix_with('IGNORE')
                try:
                    conn.execute(insert_stmt)
                    inserted_row += 1
                except :
                    conn.execute(update_stmt)
                    updated_row +=1
            conn.commit()
    return inserted_row, updated_row


def log_func(table, engine, process, flag, description):
    from sqlalchemy import insert, func
    from models import MigrationLog
    with engine.connect() as conn:
        conn.execute(insert(MigrationLog)
                     .values(createdAt=func.current_timestamp(),
                             table=table.__str__(),
                             flag=flag,
                             process=process,
                             description=description
                             ))
        conn.commit()

def monitoring_etl(table,engine, started_at,inserted_row,updated_row, description):
    from sqlalchemy import  func,text
    with engine.connect() as conn:
        stmt = f""" 
            insert into monitor.monitoring_etl 
            (etl_name,started_at,finished_at,inserted_row,updated_row,description,inserted_file)
            values 
            ('{table}','{started_at}',{func.current_timestamp()},{inserted_row},{updated_row},'{description}',0 )
        """
        conn.execute(text(stmt))
        conn.commit()
        
def del_log(engine,days):
    from models import MigrationLog
    from sqlalchemy import delete,cast,Date
    with engine.connect() as conn:
        conn.execute(delete(MigrationLog).where( cast(MigrationLog.c.createdAt,Date) < createdAt_n_days_func(days).date() ))
        conn.commit()