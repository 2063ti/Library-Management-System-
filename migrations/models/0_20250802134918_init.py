from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "author" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "bio" TEXT
);
CREATE TABLE IF NOT EXISTS "book" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "isbn" VARCHAR(13) UNIQUE,
    "publication_year" INT,
    "publisher" VARCHAR(255),
    "copies_available" INT NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "member" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "phone" VARCHAR(20),
    "address" TEXT,
    "password_hash" VARCHAR(255) NOT NULL,
    "membership_date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "staff" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password_hash" VARCHAR(255) NOT NULL,
    "role" VARCHAR(50) NOT NULL DEFAULT 'librarian',
    "phone" VARCHAR(20),
    "address" TEXT,
    "joined_on" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "loan" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "loan_date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "return_date" TIMESTAMP,
    "due_date" TIMESTAMP NOT NULL,
    "returned" INT NOT NULL DEFAULT 0,
    "book_id" INT NOT NULL REFERENCES "book" ("id") ON DELETE CASCADE,
    "member_id" INT NOT NULL REFERENCES "member" ("id") ON DELETE CASCADE,
    "staff_id" INT REFERENCES "staff" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "book_author" (
    "book_id" INT NOT NULL REFERENCES "book" ("id") ON DELETE CASCADE,
    "author_id" INT NOT NULL REFERENCES "author" ("id") ON DELETE CASCADE
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_book_author_book_id_818352" ON "book_author" ("book_id", "author_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
