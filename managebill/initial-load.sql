-- Command to load initial data: sqlite3 managebill.db < initial-load.sql

-- load admin users (super admins)
INSERT INTO user (id, username, password, firstname, lastname, email, mobile, adminflag) VALUES (1, 'admin', 'password', 'Admin', 'User', 'avikdeb.select@gmail.com', '9543187077', 1);
INSERT INTO user (id, username, password, firstname, lastname, email, mobile, adminflag) VALUES (2, 'admin', 'admin', 'Admin', 'Admin', 'avikdeb.select@gmail.com', '8322965855', 1);

-- load paymentstatus table
INSERT INTO paymentstatus (id, status) VALUES (1, 'Payment Due');
INSERT INTO paymentstatus (id, status) VALUES (2, 'Under Collection');
INSERT INTO paymentstatus (id, status) VALUES (3, 'Payment Done');
INSERT INTO paymentstatus (id, status) VALUES (4, 'On Hold');
INSERT INTO paymentstatus (id, status) VALUES (5, 'Payment Overdue');
