# Airbnb Clone - Web Framework Project

This project aims to create a simplified clone of Airbnb using the Flask web framework. It is designed to demonstrate the capabilities of Flask in building web applications and dynamically displaying data from a MySQL database.

## Overview

The project focuses on the back-end development with Flask, covering the creation of web routes, handling of dynamic content through Jinja templates, and interaction with a MySQL database to display properties, bookings, and user information in a web interface.

## Installation

To get started with this project, you'll need to have Python and Flask installed on your machine. You can install Flask using pip:

```bash
pip3 install Flask
```

Ensure you are using Ubuntu 20.04 LTS and Python 3.4.3 for compatibility.

## Features

- **Web Framework with Flask**: Utilizing Flask to handle HTTP requests, render templates, and serve dynamic content.
- **Dynamic Templating**: Using Jinja2 templating engine to create dynamic HTML pages based on the data fetched from the MySQL database.
- **Database Integration**: Demonstrates how to perform CRUD operations on a MySQL database from Flask.
- **Routing and URL Handling**: Defines routes to different parts of the web application, handling variable paths and rendering corresponding templates.

## Usage

To run the Flask application:

```bash
export FLASK_APP=your_main_script.py
export FLASK_ENV=development
flask run
```

## Project Structure

- `/app`: Main application directory containing Flask app and route definitions.
- `/templates`: Contains Jinja2 templates for HTML pages.
- `/static/styles`: CSS files for styling the web pages.
- `/static/images`: Images used in the web application.

## Contributing

Contributions are welcome! If you're interested in improving this Airbnb clone, please feel free to fork the repository and submit a pull request.

## License

[MIT](./LICENSE)

## Acknowledgments

- Flask Documentation
- Jinja2 Templating Engine
- MySQL Database Management
