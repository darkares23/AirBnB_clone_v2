#!/usr/bin/env bash
#Sets up your web servers for the deployment of web_static.
#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get -y update && sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo -e "<html>\n <head>\n </head>\n <body>\n Holberton School\n </body>\n/<html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '42i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
