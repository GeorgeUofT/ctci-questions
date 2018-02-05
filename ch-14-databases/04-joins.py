# Explain the various types of database table joins.

# In SQL, the JOIN keyword is used to combine records in tables according to
# a specified field in each.  When the specified fields match, the records are
# joined together.  The different types of joins (INNER, LEFT, RIGHT, and
# OUTER) only differ in how they handle records that do not have a match in
# the other table.

# INNER joins ignore records that do not match.  OUTER joins include all records
# whether or not they matched with a record from the other table.  LEFT joins
# include records in the left table whether or not they match, but do not 
# include unmatched records in the right table.  RIGHT joins are the reverse
# of LEFT joins.  When a record is included that doe not match another record
# NULL values are used where a matching records' values would otherwise be.

# Consider the following two tables.  An inner join on the author's name
# would contain four rows for the combinations of Randall Munroe's comics
# and books and one row for Matthew Inman.  A left join with the Comic as the
# first table would additionally return a row for Zach Weinersmith with NULL
# values for the book.title, book.author, and book.year.  A full outer join
# would contain six rows.

# Comic Table
# +=============+==================+=============================+
# | Name        | Author           | URL                         |
# +=============+==================+=============================+
# | XKCD        | Randall Munroe   | https://www.xkcd.com/       |
# +-------------+------------------+-----------------------------+
# | What If?    | Randall Munroe   | https://what-if.xkcd.com/   |
# +--------------+-----------------+-----------------------------+
# | The Oatmeal | Matthew Inman    | http://theoatmeal.com/      |
# +-------------+------------------+-----------------------------+
# | SMBC        | Zach Weinersmith | http://www.smbc-comics.com/ |
# +-------------+------------------+-----------------------------+

# Book Table
# +=================================================+================+======+
# | Title                                           | Author         | Year |
# +=================================================+================+======+
# | What If?                                        | Randall Munroe | 2014 |
# +-------------------------------------------------+----------------+------+
# | Thing Explainer                                 | Randall Munroe | 2015 |
# +-------------------------------------------------+----------------+------+
# | How to Tell if Your Cat is Plotting to Kill You | Matthew Inman  | 2012 |
# +-------------------------------------------------+----------------+------+
# | The Hitchhiker's Guide to the Galaxy            | Douglas Adams  | 1978 |
# +-------------------------------------------------+----------------+------+

