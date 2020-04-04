# stock.ar-api
Web Service for the [stock.ar](https://github.com/leoelz/stock.ar) application

## First Steps
### Installing dependencies
First you need to have Python 3.7 and virtualenv installed on your computer, then in a terminal go 
to the root of the project and run:
```bash
make install
```
With this command all the dependencies required for the project will install.
### Running the project
For running on the API you have run:
```bash
make run
```
And the project will be running on `http://localhost:5000/`
### Testing
To run the test suite of the project you can run the following command:
```bash
make test
```
Or if you want the coverage of the project:
```bash
make test-coverage
```