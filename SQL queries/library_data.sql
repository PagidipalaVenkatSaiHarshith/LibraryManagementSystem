INSERT INTO liblocation(name,location)
VALUES
  ('golden arch','philidelphia'),
  ('yelow flower','ohio'),
  ('city square','new york');

INSERT INTO author(name,bio)
VALUES
  ('j.k.rowling','2017894567'),
  ('annie brown','2017891562'),
  ('austinbrant','2018629847'),
  ('kelly grant','2018623567'),
  ('sam flynn','2018628997');

INSERT INTO publisher(name,address)
VALUES
  ('new world inc','9734560001'),
  ('maple tree','9734560002'),
  ('blue sea','9734560003'),
  ('horizon','9734560004'),
  ('oakland','9734560005');

INSERT INTO customer(name,contact)
VALUES
  ('bruce','2012680001'),
  ('tony','2012680002'),
  ('natasha','2012680003'),
  ('tom','2012680004'),
  ('hanabi','2012680005');

INSERT INTO books(title,author_id,publisher_id,publication_date,isbn,copies)
VALUES
  ('harry potter',1,1,'1997-06-26','0-1040-5640-1',2),
  ('subtle life',2,2,'2016-09-13','0-1401-7684-5',3),
  ('legacy leaf',3,3,'2022-10-12','0-7910-7310-6',4),
  ('me and my city',4,4,'2019-04-16','0-6800-5671-8',3),
  ('a day in future',5,5,'2017-05-26','0-3753-8986-5',4);

INSERT INTO copytable(book_id,lib_id,copy_id)
VALUES
  (1,1,1),
  (1,1,2),
  (2,1,1),
  (3,1,1),
  (4,1,1),
  (5,1,1),
  (5,1,2),
  (2,2,1),
  (2,2,2),
  (3,2,1),
  (4,2,1),
  (5,2,1),
  (3,3,1),
  (3,3,2),
  (4,3,1),
  (4,3,2),
  (5,3,1);

INSERT INTO reserves(cust_id,book_id,lib_id,copy_id)
VALUES
  (5,1,1,1),
  (4,1,1,2),
  (3,2,2,2);

INSERT INTO borrows(cust_id,book_id,lib_id,copy_id)
VALUES
  (1,1,1,1),
  (2,5,3,1),
  (3,3,3,1);

INSERT INTO reservation(reserve_id,reserve_dtime)
VALUES
  (1,'2023-02-28'),
  (2,'2023-03-01'),
  (3,'2023-03-02');

INSERT INTO borrowing(borrows_id,borrowed_dtime,expected_return,actual_return)
VALUES
  (1,'2023-02-19','2023-02-26',NULL),
  (2,'2023-02-23','2023-03-02',NULL),	
  (3,'2023-02-25','2023-03-04',NULL);

UPDATE borrowing SET actual_return='2023-02-27' WHERE borrows_id=1;	
