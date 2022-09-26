server {
    listen 443 ssl;
    ssl_certificate /PATH/example.com.crt;
    ssl_certificate_key /PATH/example.com.key;
    ssl_protocols       TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    ssl_ciphers         HIGH:!aNULL:!MD5;
    server_name example.com;

    location /static {
        alias /vol/static;
    }

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
        proxy_read_timeout 86400;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}