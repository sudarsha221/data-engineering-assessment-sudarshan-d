-- PROPERTIES MASTER TABLE
CREATE TABLE properties (
    property_id INT PRIMARY KEY AUTO_INCREMENT,
    raw_property_id VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zipcode VARCHAR(20),
    bedrooms INT,
    bathrooms FLOAT,
    sqft INT,
    lot_size FLOAT,
    year_built INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- HOA DETAILS
CREATE TABLE hoa_details (
    hoa_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT,
    hoa_fee DECIMAL(10,2),
    hoa_frequency VARCHAR(50),
    hoa_contact VARCHAR(255),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- REHAB ESTIMATES
CREATE TABLE rehab_estimates (
    rehab_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT,
    estimated_cost DECIMAL(12,2),
    description TEXT,
    contractor_name VARCHAR(255),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- VALUATION DATA
CREATE TABLE valuations (
    valuation_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT,
    market_value DECIMAL(12,2),
    as_is_value DECIMAL(12,2),
    arv_value DECIMAL(12,2),
    valuation_date DATE,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- RAW JSON STORAGE (OPTIONAL)
CREATE TABLE raw_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    raw_json LONGTEXT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
