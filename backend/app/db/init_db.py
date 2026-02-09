from app.db.session import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Users Table
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

    # Posts Table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            CONSTRAINT fk_posts_user
                FOREIGN KEY (user_id)
                REFERENCES users(id)
                ON DELETE CASCADE
        );
        """
    )

    conn.commit()
    cur.close()
    conn.close()
