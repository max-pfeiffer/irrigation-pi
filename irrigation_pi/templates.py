"""Configuration file templates."""

# fmt: off
# ruff: noqa

from string import Template

SYSTEMD_SERVICE_TEMPLATE: Template = Template("""[Unit]
Description=Irrigation-Pi Backend Application
Requires=network.target

[Service]
Type=exec
User=$user
Environment="PATH=$virtual_environment_binary_path"
WorkingDirectory=$backend_path
ExecStart=$virtual_environment_binary_path/uvicorn --proxy-headers --forwarded-allow-ips='*' --uds /tmp/uvicorn.sock --workers 1 app.main:app

[Install]
WantedBy=multi-user.target

""")

NGINX_SITE_TEMPLATE: Template = Template("""map $$http_upgrade $$connection_upgrade {
    default upgrade;
    '' close;
  }

upstream uvicorn {
    server unix:/tmp/uvicorn.sock;
  }


server {
    listen $port default_server;
    server_name _;
    root $server_root;
    index index.html;

    location / {
        try_files $$uri $$uri/ /index.html;
    }
    
    location /api {
      proxy_set_header Host $$http_host;
      proxy_set_header X-Forwarded-For $$proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $$scheme;
      proxy_set_header Upgrade $$http_upgrade;
      proxy_set_header Connection $$connection_upgrade;
      proxy_redirect off;
      proxy_buffering off;
      proxy_pass http://uvicorn;
    }    
}

""")

APPLICATION_CONFIGURATION_TEMPLATE: Template = Template("""[backend]
# Possible options are: rpi_gpio, pigpio, native
pin_factory_type = "rpi_gpio"

# Possible options are: waveshare_rpi_relay_board
adapter_type = "waveshare_rpi_relay_board"

""")
