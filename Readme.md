# Flask App with Nginx and SSL

This repository contains a Flask app that is configured to run with Nginx as a reverse proxy and HTTPS using SSL certificates generated with Certbot.

## Installation

Install Flask and other dependencies:
pip install flask gunicorn


Install Nginx on your server:

sudo apt-get update
sudo apt-get install nginx


## Flask App Configuration

Create a file named `app.py` and add your Flask app code to it.

Test your Flask app locally:


Verify that your Flask app is accessible at `http://localhost:8000`.

## Nginx Configuration

Create an Nginx configuration file for your Flask app, e.g., `/etc/nginx/conf.d/myapp.conf`.

Add the following Nginx configuration to the file, adjusting as necessary:

Refer myappnginx.conf


Test the Nginx configuration and restart Nginx:
sudo nginx -t
sudo systemctl restart nginx


## SSL Certificate Generation

Install Certbot to simplify the SSL certificate management process:

sudo apt-get install certbot python3-certbot-nginx


Obtain and install the SSL certificate using Certbot:
sudo certbot --nginx -d your_domain.com


Follow the interactive prompts to configure Certbot and generate the SSL certificate.

Verify automatic certificate renewal:
sudo certbot renew --dry-run


Set up a cron job or scheduled task to automatically run `certbot renew` periodically to renew the certificate.

## Usage

Deploy your Flask app and Nginx configuration to your server.

Access your Flask app at `http://your_domain.com` over HTTPS.

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.





