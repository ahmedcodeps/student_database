# Student Fee Database

## Purpose

This project uses SQLite to manage students, fee types, invoices, discounts, payments, and outstanding balances.

## Setup

1. Install a SQL client such as DB Browser for SQLite.
2. Open or create a database called `student_fees.db`.
3. Run the SQL statements in `database.sql` to create the tables and sample data.
4. Open `queries.sql` and run the queries.

## Files

- `database.sql`: Tables and sample data.
- `queries.sql`: Eight SQL queries.
- `query_results.md`: Sample results.
- `erd.md`: Table relationships.
- `sample_payment_records.csv`: Sample payment records.
- `AI_DATA_QUALITY.md`: Data-quality risks for AI.

## Database Concepts

The project uses primary keys, foreign keys, joins, indexes, and basic normalization. A relational database is useful because invoices and payments must be linked reliably. A document database offers more flexibility for unstructured information but may make these financial relationships harder to maintain.

## Complexity

Indexes can speed up searches and joins, but they also use storage and can slow down inserts and updates.

## Limitations

This is a small demonstration database, not a production financial system. Its records are fictional, and each invoice contains one fee type.