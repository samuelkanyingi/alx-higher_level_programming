**0x0F. Python - Object-relational mapping**

**Learning Objectives**

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment

### More Info

#### Install and Activate Virtual Environment

To create a Python Virtual Environment, allowing you to install specific dependencies for this Python project, follow these steps:

1. Install venv:
    ```bash
    $ sudo apt-get install python3.8-venv
    ```

2. Create a virtual environment named 'venv':
    ```bash
    $ python3 -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    $ source venv/bin/activate
    ```

Once activated, you can install project-specific dependencies within this virtual environment without affecting your system-wide Python installation.

### Install MySQLdb module version 2.0.x

For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

```bash
Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Also, you can have this warning message:

```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```

You can ignore it.
