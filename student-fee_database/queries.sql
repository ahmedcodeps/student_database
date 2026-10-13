-- 1. Show all invoices and outstanding balances
SELECT *
FROM invoice_balances
ORDER BY invoice_id;


-- 2. Find unpaid or partially paid invoices
SELECT invoice_id, student_name, due_date, balance
FROM invoice_balances
WHERE balance > 0
ORDER BY due_date;


-- 3. Show payment history
SELECT
    p.payment_date,
    s.first_name || ' ' || s.last_name AS student_name,
    p.invoice_id,
    p.amount,
    p.payment_method
FROM payments p
JOIN invoices i ON p.invoice_id = i.invoice_id
JOIN students s ON i.student_id = s.student_id
ORDER BY p.payment_date;


-- 4. Calculate total collections
SELECT
    COUNT(*) AS number_of_payments,
    SUM(amount) AS total_collections
FROM payments;


-- 5. Find overdue invoices as of October 13, 2026
SELECT invoice_id, student_name, due_date, balance
FROM invoice_balances
WHERE due_date < '2026-10-13'
AND balance > 0;


-- 6. Calculate balances for each student
SELECT
    student_number,
    student_name,
    SUM(total_due) AS total_billed,
    SUM(paid) AS total_paid,
    SUM(balance) AS outstanding
FROM invoice_balances
GROUP BY student_number, student_name;


-- 7. Calculate billed amounts by fee type
SELECT
    fee_name,
    SUM(total_due) AS total_billed
FROM invoice_balances
GROUP BY fee_name;


-- 8. Calculate collections by month
SELECT
    substr(payment_date, 1, 7) AS payment_month,
    SUM(amount) AS collections
FROM payments
GROUP BY payment_month
ORDER BY payment_month;