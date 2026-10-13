STUDENTS
   |
   | one student has many invoices
   v
INVOICES ------ FEE_TYPES
   |
   | may use a discount
   v
DISCOUNTS

INVOICES
   |
   | one invoice can have multiple payments
   v
PAYMENTS