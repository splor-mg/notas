INSERT INTO classificador (code, description, valid_from) VALUES (10, 'Recursos Ordinarios', '0001-01-01');
INSERT INTO classificador (code, description, valid_from) VALUES (20, 'Recursos Vinculados', '0001-01-01');
INSERT INTO classificador (code, description, valid_from) VALUES (60, 'Recursos Diretamente Arrecadados', '0001-01-01');


INSERT INTO execucao (code, dt_doc, vl_doc) VALUES (10, '2021-02-15', 5);
INSERT INTO execucao (code, dt_doc, vl_doc) VALUES (10, '2021-02-20', 60);
INSERT INTO execucao (code, dt_doc, vl_doc) VALUES (20, '2021-05-15', 35);
INSERT INTO execucao (code, dt_doc, vl_doc) VALUES (60, '2021-04-15', 10);
INSERT INTO execucao (code, dt_doc, vl_doc, hist) VALUES (60, '2021-04-15', 2, 'Recurso para reforma de unidades prisionais');
