install:
	mkdir -p $(HOME)/.face-authenticator/authorized
	cp authenticate.py $(HOME)/.face-authenticator/authenticate.py
	# sudo cp face-authentication.service /etc/systemd/system/face-authentication.service
	cp start.sh $(HOME)/.face-authenticator/start.sh
	chmod +x $(HOME)/.face-authenticator/start.sh
	# sudo systemctl daemon-reload
	# sudo systemctl enable face-authentication
	# sudo systemctl start face-authentication

authorize:
	cp $(image) $(HOME)/.face-authenticator/admin.jpg