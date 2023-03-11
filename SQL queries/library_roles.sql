-- create the customers with unique usernames and passwords
CREATE ROLE customer1 LOGIN PASSWORD 'password1';
CREATE ROLE customer2 LOGIN PASSWORD 'password2';
CREATE ROLE customer3 LOGIN PASSWORD 'password3';

-- grant privileges to update their own reserves and borrows in the reserves table
GRANT UPDATE ON TABLE reserves TO customer1, customer2, customer3;
ALTER TABLE reserves ENABLE ROW LEVEL SECURITY;
CREATE POLICY customer1_reserves_policy ON reserves FOR UPDATE TO customer1 USING (user_id = current_user);
CREATE POLICY customer2_reserves_policy ON reserves FOR UPDATE TO customer2 USING (user_id = current_user);
CREATE POLICY customer3_reserves_policy ON reserves FOR UPDATE TO customer3 USING (user_id = current_user);

-- grant privileges to update their own borrows in the borrows table
GRANT UPDATE ON TABLE borrows TO customer1, customer2, customer3;
ALTER TABLE borrows ENABLE ROW LEVEL SECURITY;
CREATE POLICY customer1_borrows_policy ON borrows FOR UPDATE TO customer1 USING (user_id = current_user);
CREATE POLICY customer2_borrows_policy ON borrows FOR UPDATE TO customer2 USING (user_id = current_user);
CREATE POLICY customer3_borrows_policy ON borrows FOR UPDATE TO customer3 USING (user_id = current_user);

-- grant privileges to update their own reservations in the reservations table
GRANT UPDATE ON TABLE reservations TO customer1, customer2, customer3;
ALTER TABLE reservations ENABLE ROW LEVEL SECURITY;
CREATE POLICY customer1_reservations_policy ON reservations FOR UPDATE TO customer1 USING (user_id = current_user);
CREATE POLICY customer2_reservations_policy ON reservations FOR UPDATE TO customer2 USING (user_id = current_user);
CREATE POLICY customer3_reservations_policy ON reservations FOR UPDATE TO customer3 USING (user_id = current_user);

-- grant privileges to update their own borrowings in the borrowings table
GRANT UPDATE ON TABLE borrowings TO customer1, customer2, customer3;
ALTER TABLE borrowings ENABLE ROW LEVEL SECURITY;
CREATE POLICY customer1_borrowings_policy ON borrowings FOR UPDATE TO customer1 USING (user_id = current_user);
CREATE POLICY customer2_borrowings_policy ON borrowings FOR UPDATE TO customer2 USING (user_id = current_user);
CREATE POLICY customer3_borrowings_policy ON borrowings FOR UPDATE TO customer3 USING (user_id = current_user);

