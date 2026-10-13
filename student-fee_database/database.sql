PRAGMA foreign_keys = ON;

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_number TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE fee_types (
    fee_type_id INTEGER PRIMARY KEY,
    fee_name TEXT UNIQUE NOT NULL
);

CREATE TABLE discounts (
    discount_id INTEGER PRIMARY KEY,
    discount_name TEXT NOT NULL,
    discount_amount REAL NOT NULL CHECK (discount_amount >= 0)
);

CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(student_id),
    fee_type_id INTEGER NOT NULL REFERENCES fee_types(fee_type_id),
    discount_id INTEGER REFERENCES discounts(discount_id),
    issue_date TEXT NOT NULL,
    due_date TEXT NOT NULL,
    amount REAL NOT NULL CHECK (amount >= 0)
);

CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY,
    invoice_id INTEGER NOT NULL REFERENCES invoices(invoice_id),
    payment_date TEXT NOT NULL,
    amount REAL NOT NULL CHECK (amount > 0),
    payment_method TEXT NOT NULL
);

INSERT INTO students VALUES
(1, 'S001', 'Aisha', 'Rahman'),
(2, 'S002', 'Omar', 'Nasser'),
(3, 'S003', 'Layla', 'Faris');

INSERT INTO fee_types VALUES
(1, 'Tuition'),
(2, 'Transport'),
(3, 'Laboratory');

INSERT INTO discounts VALUES
(1, 'Sibling Discount', 50),
(2, 'Merit Discount', 100);

INSERT INTO invoices VALUES
(101, 1, 1, 1, '2026-09-01', '2026-09-30', 1000),
(102, 2, 1, NULL, '2026-09-01', '2026-10-10', 800),
(103, 3, 2, NULL, '2026-10-01', '2026-10-20', 200),
(104, 1, 3, 2, '2026-10-01', '2026-10-15', 300);

INSERT INTO payments VALUES
(1, 101, '2026-09-10', 500, 'Bank transfer'),
(2, 101, '2026-09-20', 450, 'Card'),
(3, 102, '2026-10-05', 300, 'Online'),
(4, 104, '2026-10-07', 100, 'Cash');

CREATE INDEX idx_invoices_student
ON invoices(student_id);

CREATE INDEX idx_payments_invoice
ON payments(invoice_id);

CREATE VIEW invoice_balances AS
SELECT
    i.invoice_id,
    s.student_number,
    s.first_name || ' ' || s.last_name AS student_name,
    f.fee_name,
    i.issue_date,
    i.due_date,
    ROUND(i.amount - COALESCE(d.discount_amount, 0), 2)
        AS total_due,
    ROUND(COALESCE(SUM(p.amount), 0), 2) AS paid,
    ROUND(
        MAX(
            i.amount
            - COALESCE(d.discount_amount, 0)
            - COALESCE(SUM(p.amount), 0),
            0
        ),
        2
    ) AS balance
FROM invoices i
JOIN students s ON s.student_id = i.student_id
JOIN fee_types f ON f.fee_type_id = i.fee_type_id
LEFT JOIN discounts d ON d.discount_id = i.discount_id
LEFT JOIN payments p ON p.invoice_id = i.invoice_id
GROUP BY i.invoice_id;