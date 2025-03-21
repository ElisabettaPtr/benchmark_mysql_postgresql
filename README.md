# Benchmark MySQL vs PostgreSQL

Questo progetto esegue un benchmark comparativo tra MySQL e PostgreSQL, misurando le performance di tre operazioni chiave: inserimento di dati, lettura di dati e transazioni con rollback.

## Struttura del Progetto

- **`benchmark_mySQL_postgreSQL.py`**: Script principale che esegue il benchmark.
- **`.env`**: File di configurazione per le credenziali dei database.

## Tecnologie Utilizzate

- **Python 3**
- **SQLAlchemy**: Per la gestione del database.
- **Faker**: Per generare dati casuali.
- **MySQL** e **PostgreSQL**: Database di test.
- **dotenv**: Per caricare le variabili di ambiente.

## Funzionalità

Il progetto esegue i seguenti benchmark per ciascun database:

1. **Inserimento di Dati**: Inserisce 10.000 record e misura il tempo necessario.
2. **Lettura di Dati**: Legge tutti i record e misura il tempo necessario.
3. **Transazioni con Rollback**: Esegue 1.000 insert con rollback e misura il tempo necessario.

## Configurazione

1. Crea un file `.env` nella directory principale del progetto con le seguenti variabili:

    ```env
    MYSQL_USER = tuo_user_mysql
    MYSQL_PASSWORD = tua_password_mysql
    POSTGRES_USER = tuo_user_postgres
    POSTGRES_PASSWORD = tua_password_postgres
    ```

2. Assicurati che i database MySQL e PostgreSQL siano in esecuzione e che esista un database chiamato `benchmark_db` su entrambi i sistemi.

3. Crea un virtual environment per isolare le dipendenze del progetto:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Su Windows usa: venv\Scripts\activate
    ```

## Installazione

1. Installa le dipendenze richieste:

    ```bash
    pip install -r requirements.txt
    ```

2. Esegui lo script:

    ```bash
    python benchmark_mySQL_postgreSQL.py
    ```

## Risultati

Lo script mostrerà i risultati del benchmark per ciascun database, inclusi:

- Tempo di inserimento
- Tempo di lettura
- Numero di record letti
- Tempo di transazione con rollback

## Note

- Assicurati di avere i driver necessari per MySQL (`pymysql`) e PostgreSQL (`psycopg2`) installati.
- I risultati possono variare in base alla configurazione hardware e software del sistema.

## Autore

Progetto sviluppato da Elisabetta Petraccia.
