CREATE TABLE IF NOT EXISTS classificador (
    id INTEGER PRIMARY KEY,
    code INTEGER NOT NULL,
    description TEXT NOT NULL,
    valid_from DATE NOT NULL,
    valid_to DATE DEFAULT '9999-12-31',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_classificador_code ON classificador(code);

CREATE TRIGGER update_updated_at
AFTER UPDATE ON classificador
FOR EACH ROW
BEGIN
    UPDATE classificador
    SET updated_at = strftime('%Y-%m-%d %H:%M:%f', 'now')
    WHERE id = NEW.id;
END;

CREATE TABLE IF NOT EXISTS execucao (
    doc INTEGER PRIMARY KEY,
    code INTEGER NOT NULL,
    dt_doc DATE NOT NULL,
    vl_doc REAL NOT NULL,
    hist TEXT
);
