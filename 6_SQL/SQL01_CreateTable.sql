CREATE TABLE public."Customer"
(
  id integer NOT NULL DEFAULT nextval('"Customer_ID_seq"'::regclass), -- Primary Key
  first_name character varying(15),
  last_name character varying(15),
  email character varying(100),
  balance money,
  CONSTRAINT "CustomerPK" PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Customer"
  OWNER TO postgres;
COMMENT ON COLUMN public."Customer".id IS 'Primary Key';