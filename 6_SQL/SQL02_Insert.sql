INSERT INTO public."Customer"
    (first_name, last_name, email, balance)
    VALUES ('Bob', 'Marley', 'bob.marley@gmail.com', 900000);
INSERT INTO public."Customer"
    (first_name, last_name, email, balance)
    VALUES ('Jimmy', 'Cliff', 'jimmy.cliff@gmail.com', 800000);
INSERT INTO public."Customer"
    (first_name, last_name, email, balance)
    VALUES ('Peter', 'Tosh', 'peter.tosh@gmail.com', 700000);
INSERT INTO public."Customer"
    (first_name, last_name, email, balance)
    VALUES ('Burning', 'Spear', 'burning.spear@gmail.com', 600000);


 select *
   from public."Customer"
   where first_name in ('Bob', 'Jimmy')