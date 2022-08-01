server {
	listen 80;

	server_name Slope_Stability_Predictor;

	root /home/ubuntu/Slope_Stability_Predictor/client;
	index app.html;

	location /api/ {
		rewrite ^/api(.*) $1 break;
		proxy_pass http://127.0.0.1:5000;
	}
}