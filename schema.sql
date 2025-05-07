CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL
);

CREATE TABLE lists (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE,
    list_id INTEGER REFERENCES lists(id) ON DELETE CASCADE
);

-- Seed data
INSERT INTO users (username) VALUES ('alice'), ('bob');
INSERT INTO lists (name, user_id) VALUES ('Groceries', 1), ('Work', 1), ('Books', 2);
INSERT INTO tasks (description, list_id) VALUES ('Buy milk', 1), ('Finish report', 2), ('Read Python book', 3);
