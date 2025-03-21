import time
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, text
from sqlalchemy.orm import sessionmaker
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

DATABASES = {
    "mysql": f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@localhost/benchmark_db",
    "postgresql": f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/benchmark_db"
}

fake = Faker()

def create_table(engine):
    metadata = MetaData()
    test_table = Table("test", metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("name", String(100)),
                    Column("email", String(100)))
    metadata.create_all(engine)
    return test_table

def benchmark_insert(session, num_records=10000):
    start = time.time()
    for _ in range(num_records):
        session.execute(
            text("INSERT INTO test (name, email) VALUES (:name, :email)"),  
            {"name": fake.name(), "email": fake.email()}
        )
    session.commit()
    end = time.time()
    return end - start

def benchmark_read(session):
    start = time.time()
    result = session.execute(text("SELECT * FROM test")).fetchall()
    end = time.time()
    return end - start, len(result)

def benchmark_transaction(session):
    start = time.time()
    try:
        for _ in range(1000):
            session.execute(
                text("INSERT INTO test (name, email) VALUES (:name, :email)"),
                {"name": fake.name(), "email": fake.email()}
            )
        session.rollback()
    except Exception as e:
        print("Error in transaction:", e)
    end = time.time()
    return end - start

results = {}
for db, url in DATABASES.items():
    try:
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()

        print(f"Benchmarking {db}...")
        create_table(engine)
        
        insert_time = benchmark_insert(session)
        read_time, record_count = benchmark_read(session)
        transaction_time = benchmark_transaction(session)
        
        results[db] = {
            "insert_time": insert_time,
            "read_time": read_time,
            "record_count": record_count,
            "transaction_time": transaction_time
        }

        session.close()
        engine.dispose()

    except Exception as e:
        print(f"Errore nel benchmark per {db}: {e}")

for db, metrics in results.items():
    print(f"\nResults for {db}:")
    print(f"  Insert time: {metrics['insert_time']} sec")
    print(f"  Read time: {metrics['read_time']} sec (Records: {metrics['record_count']})")
    print(f"  Transaction time (rollback): {metrics['transaction_time']} sec")
