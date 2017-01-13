DB tools
==
## Some scripts to help investigate Databases

### Setting up Drivers
All these scripts rely on having ODBC drivers registered on your computer to allow the connection to the database in question. This is done differently for different OS:-

- **UNIX** - [unixODBC](http://www.unixodbc.org/), where registered files are managed in the [odbcinst.ini](http://www.unixodbc.org/odbcinst.html) file.
- **Mac** - There is a native solution called iODBC but it is often advised to download and use unixODBC instead.
- **Windows** - There's an ODBC manager with a wizard already on IIRC.

#### odbcinst.ini Example
```
[Name to be used when calling the ODBC driver]
Description=Description of driver
Driver=/location/of/driver
Setup=/location/of/driver
UsageCount=1
```
Usage count defines the max number of connections allowed (I think).
### Scripts
Each script can be called with the following options:

|Option<sup>†</sup>|Option<sup>‡</sup>|Description|
|---|---|---|
|-h|--help|get help information (to be used on it's own)
| -d|--driver|Set the registered driver|
| -s|--server|Set the location of the server holding the database|
| -p|--port|Set the port to connect to the server with|
| -b|--database|Set the database (or schema) within the database instance|
| -u|--user|Set the user to log in with|
Any missing parameters are then requested by the programme. The password is entered when the connection is made.

† - Short form
‡ - Long form
#### linecount.py
Takes a line count of each table within the given database.
- TODO: sort out output
