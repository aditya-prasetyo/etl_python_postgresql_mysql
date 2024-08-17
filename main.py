# Konfigurasi
from dotenv import load_dotenv
import os 
from sqlalchemy import text

load_dotenv()

SOURCE_USER=os.getenv('SOURCE_USER')
SOURCE_PASS=os.getenv('SOURCE_PASS')
SOURCE_HOST=os.getenv('SOURCE_HOST')
SOURCE_PORT=os.getenv('SOURCE_PORT')
SOURCE_DATABASE=os.getenv('SOURCE_DATABASE')
SOURCE_ENGINE=os.getenv('SOURCE_ENGINE')

TARGET_USER=os.getenv('TARGET_USER')
TARGET_PASS=os.getenv('TARGET_PASS')
TARGET_HOST=os.getenv('TARGET_HOST')
TARGET_PORT=os.getenv('TARGET_PORT')
TARGET_DATABASE=os.getenv('TARGET_DATABASE')
TARGET_ENGINE=os.getenv('TARGET_ENGINE')

N_DAYS=2


def main():
    from tqdm import tqdm
    from sqlalchemy import or_,and_,func,cast,Date
    import models
    import utils
    from datetime import datetime
    import pytz
    
    started_at = datetime.now(tz=pytz.timezone('Asia/Jakarta'))
    total_inserted_row = 0
    total_updated_row = 0
    errors = []
    
    psql_engine = utils.engine_func(SOURCE_USER,
                                SOURCE_PASS,
                                SOURCE_HOST,
                                SOURCE_PORT,
                                SOURCE_DATABASE,
                                SOURCE_ENGINE
                                )
    
    mysql_engine = utils.engine_func(   TARGET_USER,
                                    TARGET_PASS,
                                    TARGET_HOST,
                                    TARGET_PORT,
                                    TARGET_DATABASE,
                                    TARGET_ENGINE
                                    )

    
    # models.metadata_obj.create_all(mysql_engine)
    
    models_obj = models.metadata_obj.tables.values()
    # models_obj = [ models.Ticket]
    
    pbar = tqdm(models_obj)
    for i in pbar:
        
        if i.__str__() == 'MigrationLog':
            continue
        else:
            pbar.set_description(f'Processing {i}')
            utils.log_func(i, mysql_engine, 'GET', 'INFO',
                     f'Starting Process')
            created_n_days = utils.createdAt_n_days_func(N_DAYS)
            try:
                fetch_source = utils.fetch_filter(
                i, psql_engine, i.c.updatedAt > created_n_days )
            except Exception as e:
                utils.log_func(i, mysql_engine, 'FAIL', 'ERROR', str(e))
                errors.append(i.__str__())
                continue
            
            try:
                inserted_rows,updated_rows = utils.migrate_data(i, mysql_engine, fetch_source)  
            except Exception as e:
                utils.log_func(i, mysql_engine, 'FAIL', 'ERROR', str(e))
                errors.append(i.__str__())
                continue
            
            total_inserted_row += inserted_rows
            total_updated_row += updated_rows

            utils.log_func(i, mysql_engine, 'POST', 'SUCCESS', f'{len(fetch_source)} rows retrieved. Migration Done')
    
    if len(errors) < 1:
        utils.monitoring_etl('ETL Mobile Python',mysql_engine,started_at,total_inserted_row,total_updated_row,'Success')
    else:
        e = ', '.join(errors)
        utils.monitoring_etl('ETL Mobile Python',mysql_engine,started_at,total_inserted_row,total_updated_row,f'Fail : {e}')
    
    utils.del_log(mysql_engine,30)
    
    print('Migration Done')


if __name__ == '__main__':
    main()
