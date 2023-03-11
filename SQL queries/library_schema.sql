CREATE TABLE liblocation (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL
);
CREATE TABLE customer(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  contact VARCHAR(10) NOT NULL
);
CREATE TABLE author(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  bio TEXT
);
CREATE TABLE publisher(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address TEXT
);
CREATE TABLE books(
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author_id INTEGER NOT NULL,
  publisher_id INTEGER NOT NULL,
  publication_date DATE NOT NULL,
  isbn VARCHAR(13) NOT NULL,
  copies INTEGER NOT NULL
);
CREATE TABLE copytable(
  book_id INTEGER NOT NULL,
  lib_id INTEGER NOT NULL,
  copy_id INTEGER NOT NULL
);
CREATE TABLE reserves(
  id SERIAL PRIMARY KEY,
  cust_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  lib_id INTEGER NOT NULL,
  copy_id INTEGER NOT NULL
);
CREATE TABLE reservation(
  reserve_id INTEGER NOT NULL,
  reserve_dtime DATE NOT NULL
);
CREATE TABLE borrows(
  id SERIAL PRIMARY KEY,
  cust_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  lib_id INTEGER NOT NULL,
  copy_id INTEGER NOT NULL
);
CREATE TABLE borrowing(
  borrows_id INTEGER NOT NULL,
  borrowed_dtime DATE NOT NULL,
  expected_return DATE NOT NULL,
  actual_return DATE
);
CREATE TABLE latefee(
  borrow_id INTEGER NOT NULL,
  days_late INTEGER,
  latefee money
);
-- Create foreign key constraints for the book table
ALTER TABLE books
ADD CONSTRAINT books_author_id_fk
FOREIGN KEY (author_id)
REFERENCES author (id);

ALTER TABLE books
ADD CONSTRAINT books_publisher_id_fk
FOREIGN KEY (publisher_id)
REFERENCES publisher (id);

-- Create foreign key constraints for the copy table
ALTER TABLE copytable
ADD CONSTRAINT copytable_book_id_fk
FOREIGN KEY (book_id)
REFERENCES books (id);

ALTER TABLE copytable
ADD CONSTRAINT copytable_lib_id_fk
FOREIGN KEY (lib_id)
REFERENCES liblocation (id);

ALTER TABLE copytable ADD CONSTRAINT copytable_partialkey UNIQUE (book_id,lib_id,copy_id);

-- Create foreign key constraints for the reserves table
ALTER TABLE reserves
ADD CONSTRAINT reserves_cust_id_fk
FOREIGN KEY (cust_id)
REFERENCES customer (id);

ALTER TABLE reserves
ADD CONSTRAINT reserves_book_id_fk
FOREIGN KEY (book_id, lib_id, copy_id)
REFERENCES copytable (book_id, lib_id, copy_id);

-- Create foreign key constraints for the borrows table
ALTER TABLE borrows
ADD CONSTRAINT borrows_cust_id_fk
FOREIGN KEY (cust_id)
REFERENCES customer (id);

ALTER TABLE borrows
ADD CONSTRAINT borrows_book_id_fk
FOREIGN KEY (book_id, lib_id, copy_id)
REFERENCES copytable (book_id, lib_id, copy_id);

-- Create foreign key constraints for the reservation table
ALTER TABLE reservation
ADD CONSTRAINT reservation_reserve_id_fk
FOREIGN KEY (reserve_id)
REFERENCES reserves (id);

-- Create foreign key constraints for the borrowing table
ALTER TABLE borrowing
ADD CONSTRAINT borrowing_borrows_id_fk
FOREIGN KEY (borrows_id)
REFERENCES borrows (id);

-- Create foreign key constraints for the latefee table
ALTER TABLE latefee
ADD CONSTRAINT latefee_borrowing_id_fk
FOREIGN KEY (borrow_id)
REFERENCES borrows (id);

-- trigger function for latefee

CREATE OR REPLACE FUNCTION insert_late_fee()
RETURNS TRIGGER AS $$
BEGIN
  -- Calculate the difference in days between the actual return date and the expected return date
  DECLARE
    days_late INTEGER;
    late_fee money;
  BEGIN
   SELECT  NEW.actual_return - NEW.expected_return INTO days_late;

-- Calculate the late fee based on the number of days late
    IF days_late > 0 THEN
      late_fee := days_late * 0.50;
      
      -- Insert the late fee into the late fee table
      INSERT INTO latefee (borrow_id, days_late, latefee)
      SELECT b.id, days_late, late_fee
      FROM borrows b
      WHERE b.id = NEW.borrows_id;
    END IF;
    
    RETURN NEW;
  END;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER insert_late_fee_trigger
AFTER UPDATE ON borrowing
FOR EACH ROW
WHEN (OLD.actual_return IS NULL AND NEW.actual_return IS NOT NULL)
EXECUTE FUNCTION insert_late_fee();
