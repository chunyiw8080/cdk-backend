CREATE TABLE cdk (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cdk VARCHAR(64) NOT NULL UNIQUE,
    used BOOLEAN NOT NULL DEFAULT FALSE,
    used_by INT NULL,
    used_at DATETIME NULL,
    content VARCHAR(50) NOT NULL,
    
    INDEX idx_cdk (cdk),
    INDEX idx_id (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;