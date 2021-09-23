#1)

#  CREATE DATABASE kurut taxi;
# ERROR:  syntax error at or near ";"
# LINE 1: CREATE DATABASE kurut taxi;
                    
# postgres=# CREATE DATABASE kurut_taxi;

# CREATE DATABASE



# kurut_taxi=# CREATE TABLE Auto(id integer PRIMARY KEY, marka varchar(50), model varchar(50), fuel varchar(50), obem varchar(50), type_korobki_peredach varchar(50), year integer, color varchar(50));
# CREATE TABLE




# kurut_taxi=# CREATE TABLE driver(id integer, name varchar(50), surname varchar(60), date_of_birth date, drivers_stage_years integer, gender varchar(50), car integer REFERENCES Auto(id));
# CREATE TABLE

# kurut_taxi=# CREATE TABLE Operator_call_center( id integer, name varchar(50), surname varchar(50), date_of_birth date, gender varchar(50));
# CREATE TABLE




# kurut_taxi=# \d Auto;
#                               Table "public.auto"
#         Column         |         Type          | Collation | Nullable | Default 
# -----------------------+-----------------------+-----------+----------+---------
#  id                    | integer               |           | not null | 
#  marka                 | character varying(50) |           |          | 
#  model                 | character varying(50) |           |          | 
#  fuel                  | character varying(50) |           |          | 
#  obem                  | character varying(50) |           |          | 
#  type_korobki_peredach | character varying(50) |           |          | 
#  year                  | integer               |           |          | 
#  color                 | character varying(50) |           |          | 
# Indexes:
#     "auto_pkey" PRIMARY KEY, btree (id)


#2)

# kurut_taxi=# INSERT INTO Auto(id, marka, model, fuel, obem, type_korobki_peredach, year, color) VALUES( 1, 'BMW', 'X5', 'Бензин', '5.5 litr', 'автомат', 2019, 'White'), (2, 'Mercedes', 's350', 'Электричество', '500kw', 'автомат', 2020, 'Black'), (3, 'Toyota', 'Camry', 'benzin', '3.5 litr', 'механика', 2017, 'Gray'), (4, 'Honda', 'fit', 'benzin', '1.5 litr', 'автомат', 2016, 'White'), (5, 'ROLLS ROYCE', 'Cullinan', 'benzin', '10 litr', 'автомат', 2021, 'Black'), (6, 'BMW', 'X5', 'Бензин', '5.5 litr', 'автомат', 2019, 'White'), (7, 'Honda', 'fit', 'benzin', '1.5 litr', 'автомат', 2016, 'White'), (8, 'Toyota', 'Camry', 'benzin', '3.5 litr', 'механика', 2017, 'Gray'), (9, 'Mercedes', 's350', 'Электричество', '500kw', 'автомат', 2020, 'Black'), (10, 'ROLLS ROYCE', 'Cullinan', 'benzin', '10 litr', 'автомат', 2021, 'Black'), (11, 'Toyota', 'Camry', 'benzin', '3.5 litr', 'механика', 2017, 'Gray'), (12, 'Honda', 'fit', 'benzin', '1.5 litr', 'автомат', 2016, 'White');
# INSERT 0 12




# kurut_taxi=# \d driver;
#                             Table "public.driver"
#        Column        |         Type          | Collation | Nullable | Default 
# ---------------------+-----------------------+-----------+----------+---------
#  id                  | integer               |           |          | 
#  name                | character varying(50) |           |          | 
#  surname             | character varying(60) |           |          | 
#  date_of_birth       | date                  |           |          | 
#  drivers_stage_years | integer               |           |          | 
#  gender              | character varying(50) |           |          | 
#  car                 | integer               |           |          | 
# Foreign-key constraints:




# kurut_taxi=# INSERT INTO driver(id, name, surname, date_of_birth, drivers_stage_years, gender, car) VALUES(1, 'Azamat', 'Azamatov', '2000-12-25', 3, 'male', 1), (2, 'Adyl', 'Malikov', '1995-06-15', 5, 'male', 2), (3, 'Alina', 'Kalyeva', '1980-01-18', 10, 'female', 3), (4, 'Max', 'Talantbaev', '1976-03-02', 15, 'male', 4), (5, 'Lina', 'Kate', '1988-04-17', 12, 'female', 5), (6, 'Mika', 'Bardo', '1992-08-01', 10, 'female', 6), (7, 'Marat', 'Samaev', '1995-11-20', 13, 'male', 7), (8, 'Max', 'Talantbaev', '1976-03-02', 15, 'male', 8), (9, 'Silvia', 'Toni', '1996-10-16', 12, 'female', 9), (10, 'Petr', 'Romanov', '1985-04-28', 8, 'male', 10), (11, 'Sasha', 'Rinova', '1987-01-27', 15, 'female', 11), (12, 'Kutman', 'Samiev', '1986-08-19', 7, 'male', 12);
# INSERT 0 12






# kurut_taxi=# \d Operator_call_center;

#                   Table "public.operator_call_center"
#     Column     |         Type          | Collation | Nullable | Default 
# ---------------+-----------------------+-----------+----------+---------
#  id            | integer               |           |          | 
#  name          | character varying(50) |           |          | 
#  surname       | character varying(50) |           |          | 
#  date_of_birth | date                  |           |          | 
#  gender        | character varying(50) |           |          | 



# kurut_taxi=# INSERT INTO Operator_call_center(id, name, surname, date_of_birth, gender) VALUES(1, 'Alia', 'Monyva', '1995-06-07', 'feamle'), (2, 'Nina', 'Saeva', '1992-03-16', 'female'), (3 ,'Dani', 'Fog', '1988-11-11', 'male');
# INSERT 0 3





# kurut_taxi=# SELECT * FROM Auto WHERE marka = 'Toyota' AND model = 'Camry' ORDER BY year DESC;
#  id | marka  | model |  fuel  |   obem   | type_korobki_peredach | year | color 
# ----+--------+-------+--------+----------+-----------------------+------+-------
#   3 | Toyota | Camry | benzin | 3.5 litr | механика              | 2017 | Gray
#   8 | Toyota | Camry | benzin | 3.5 litr | механика              | 2017 | Gray
#  11 | Toyota | Camry | benzin | 3.5 litr | механика              | 2017 | Gray
# (3 rows)

#                        ^

#                ^

#                 
# 
#        ^
# kurut_taxi=# SELECT DISTINCT name FROM Operator_call_center ORDER BY name DESC LIMIT 10;
#  name 
# ------
#  Nina
#  Dani
#  Alia
# (3 rows)




# kurut_taxi=# UPDATE Auto SET marka = 'Mersus' WHERE marka = 'Mercedes';
# UPDATE 2





# kurut_taxi=# SELECT * FROM Auto;
#  id |    marka    |  model   |     fuel      |   obem   | type_korobki_peredach | year | color 
# ----+-------------+----------+---------------+----------+-----------------------+------+-------
#   1 | BMW         | X5       | Бензин        | 5.5 litr | автомат               | 2019 | White
#   3 | Toyota      | Camry    | benzin        | 3.5 litr | механика              | 2017 | Gray
#   4 | Honda       | fit      | benzin        | 1.5 litr | автомат               | 2016 | White
#   5 | ROLLS ROYCE | Cullinan | benzin        | 10 litr  | автомат               | 2021 | Black
#   6 | BMW         | X5       | Бензин        | 5.5 litr | автомат               | 2019 | White
#   7 | Honda       | fit      | benzin        | 1.5 litr | автомат               | 2016 | White
#   8 | Toyota      | Camry    | benzin        | 3.5 litr | механика              | 2017 | Gray
#  10 | ROLLS ROYCE | Cullinan | benzin        | 10 litr  | автомат               | 2021 | Black
#  11 | Toyota      | Camry    | benzin        | 3.5 litr | механика              | 2017 | Gray
#  12 | Honda       | fit      | benzin        | 1.5 litr | автомат               | 2016 | White
#   2 | Mersus      | s350     | Электричество | 500kw    | автомат               | 2020 | Black
#   9 | Mersus      | s350     | Электричество | 500kw    | автомат               | 2020 | Black
# (12 rows)







# kurut_taxi=# SELECT * FROM Auto; 
#  id |    marka    |  model   |     fuel      |   obem   | type_korobki_peredach | year | color 
# ----+-------------+----------+---------------+----------+-----------------------+------+-------
#   1 | BMW         | X5       | Бензин        | 5.5 litr | автомат               | 2019 | White
#   3 | Toyota      | Camry    | benzin        | 3.5 litr | механика              | 2017 | Gray
#   4 | Honda       | fit      | benzin        | 1.5 litr | автомат               | 2016 | White
#   5 | ROLLS ROYCE | Cullinan | benzin        | 10 litr  | автомат               | 2021 | Black
#   6 | BMW         | X5       | Бензин        | 5.5 litr | автомат               | 2019 | White
#   7 | Honda       | fit      | benzin        | 1.5 litr | автомат               | 2016 | White
#   8 | Toyota      | Camry    | benzin        | 3.5 litr | механика              | 2017 | Gray
#  10 | ROLLS ROYCE | Cullinan | benzin        | 10 litr  | автомат               | 2021 | Black
#  11 | Toyota      | Camry    | benzin        | 3.5 litr | механика              | 2017 | Gray
#  12 | Honda       | fit      | benzin        | 1.5 litr | автомат               | 2016 | White
#   2 | Mersus      | s350     | Электричество | 500kw    | автомат               | 2020 | Black
#   9 | Mersus      | s350     | Электричество | 500kw    | автомат               | 2020 | Black
# (12 rows)







# kurut_taxi=# SELECT * FROM driver; 
#  id |  name  |  surname   | date_of_birth | drivers_stage_years | gender | car 
# ----+--------+------------+---------------+---------------------+--------+-----
#   1 | Azamat | Azamatov   | 2000-12-25    |                   3 | male   |   1
#   2 | Adyl   | Malikov    | 1995-06-15    |                   5 | male   |   2
#   3 | Alina  | Kalyeva    | 1980-01-18    |                  10 | female |   3
#   4 | Max    | Talantbaev | 1976-03-02    |                  15 | male   |   4
#   5 | Lina   | Kate       | 1988-04-17    |                  12 | female |   5
#   6 | Mika   | Bardo      | 1992-08-01    |                  10 | female |   6
#   7 | Marat  | Samaev     | 1995-11-20    |                  13 | male   |   7
#   8 | Max    | Talantbaev | 1976-03-02    |                  15 | male   |   8
#   9 | Silvia | Toni       | 1996-10-16    |                  12 | female |   9
#  10 | Petr   | Romanov    | 1985-04-28    |                   8 | male   |  10
#  11 | Sasha  | Rinova     | 1987-01-27    |                  15 | female |  11
#  12 | Kutman | Samiev     | 1986-08-19    |                   7 | male   |  12
# (12 rows)

#               





# kurut_taxi=# SELECT * FROM driver WHERE drivers_stage_years >= 10 AND gender = 'female';
#  id |  name  | surname | date_of_birth | drivers_stage_years | gender | car 
# ----+--------+---------+---------------+---------------------+--------+-----
#   3 | Alina  | Kalyeva | 1980-01-18    |                  10 | female |   3
#   5 | Lina   | Kate    | 1988-04-17    |                  12 | female |   5
#   6 | Mika   | Bardo   | 1992-08-01    |                  10 | female |   6
#   9 | Silvia | Toni    | 1996-10-16    |                  12 | female |   9
#  11 | Sasha  | Rinova  | 1987-01-27    |                  15 | female |  11
# (5 rows)








# kurut_taxi=# SELECT * FROM driver WHERE drivers_stage_years > 10 AND gender = 'female';
#  id |  name  | surname | date_of_birth | drivers_stage_years | gender | car 
# ----+--------+---------+---------------+---------------------+--------+-----
#   5 | Lina   | Kate    | 1988-04-17    |                  12 | female |   5
#   9 | Silvia | Toni    | 1996-10-16    |                  12 | female |   9
#  11 | Sasha  | Rinova  | 1987-01-27    |                  15 | female |  11
# (3 rows)






# kurut_taxi=# SELECT drivers_stage_years FROM driver WHERE date_of_birth > '1975-10-10';
#  drivers_stage_years 
# ---------------------
#                    3
#                    5
#                   10
#                   15
#                   12
#                   10
#                   13
#                   15
#                   12
#                    8
#                   15
#                    7
# (12 rows)


#                
# kurut_taxi=# SELECT marka, COUNT(marka) FROM Auto GROUP BY marka;
#     marka    | count 
# -------------+-------
#  ROLLS ROYCE |     2
#  Mersus      |     2
#  Honda       |     3
#  BMW         |     2
#  Toyota      |     3
# (5 rows)


                                                            
# kurut_taxi=# SELECT marka, COUNT(marka) FROM Auto GROUP BY marka ORDER BY marka DESC;
#     marka    | count 
# -------------+-------
#  Toyota      |     3
#  ROLLS ROYCE |     2
#  Mersus      |     2
#  Honda       |     3
#  BMW         |     2
# (5 rows)

# kurut_taxi=# SELECT car, COUNT(car) FROM driver GROUP BY car ORDER BY car DESC;
#  car | count 
# -----+-------
#   12 |     1
#   11 |     1
#   10 |     1
#    9 |     1
#    8 |     1
#    7 |     1
#    6 |     1
#    5 |     1
#    4 |     1
#    3 |     1
#    2 |     1
#    1 |     1
# (12 rows)





# DELETE FROM driver WHERE name = 'Azamat';
# DELETE 1










def say(word):
  def inner_say():
    print('Я - Декоратор')
    word()
  return inner_say

@say
def something():
  print('Я все сделал')
something()





a = int(input('Enter temperature: '))
def go_for_a_walk():
  def innner(word):
    def saying_permiton():
      print('Давай, пойдем погуляем на улице!')
      word()
    return saying_permiton
  return innner


@go_for_a_walk()

def temperature():
  try:
    if a >= 10:
      print('На улице тепло, давай погуляем, я непротив!')
    elif a >= 0 and a < 10:
      print("Прохладно.Надо одеться!")
    elif a > -10 and a < 0:
        print('Холодно. Потеплее оденься и пойдем!')
    elif a < -10:
        print('Мороз. Лучше давай дома посидим, фильм посмотрим!')
    else:
        print('No values')


  except ValueError as error: 
    print('Введите только числа')

temperature()
    
