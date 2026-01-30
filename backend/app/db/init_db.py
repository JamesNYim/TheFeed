from app.db.session import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""SELECT current_database()""")
    print("Connected to DB:", cur.fetchone())
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMPTZ DEFAULT now()
        );
        """
    )

    cur.execute(
        """
        ALTER TABLE users
        ADD COLUMN IF NOT EXISTS username TEXT UNIQUE NOT NULL
        """
    )

    conn.commit()
    cur.close()
    conn.close()
