UPDATE classificador
SET valid_to = '2022-01-01'
WHERE id = 3;

UPDATE classificador
SET valid_to = '2022-01-01'
WHERE id = 4;

INSERT INTO execucao (code, dt_doc, vl_doc) VALUES (10, '2022-02-20', 50);
INSERT INTO execucao (code, dt_doc, vl_doc) VALUES (20, '2022-05-15', 15);
INSERT INTO execucao (code, dt_doc, vl_doc, hist) VALUES (10, '2022-06-15', 5, 'Recurso diretamente arrecadado');
INSERT INTO execucao (code, dt_doc, vl_doc, hist) VALUES (20, '2022-06-15', 4, 'Recurso para reforma de unidades prisionais');
