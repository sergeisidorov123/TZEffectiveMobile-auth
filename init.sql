INSERT INTO roles (name) VALUES ('admin'), ('user');

INSERT INTO permissions (resource, action) VALUES
('admin', 'access'),
('documents', 'read'),
('documents', 'create');

INSERT INTO role_permissions VALUES (1, 1), (1, 2), (1, 3);
INSERT INTO role_permissions VALUES (2, 2);
