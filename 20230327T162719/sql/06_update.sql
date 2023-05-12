UPDATE classificador
SET valid_to = '2023-01-01'
WHERE id = 1;


INSERT INTO classificador (code, description, valid_from) VALUES (10, 'Recursos Não Vinculados', '2023-01-01');

INSERT INTO execucao (code, dt_doc, vl_doc) VALUES (10, '2023-02-20', 75);