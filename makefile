install:
	sudo mkdir -p /opt/face-authenticator/authorized
	sudo cp authenticate.py /opt/face-authenticator/authenticate.py
	sudo cp islocked.sh /opt/face-authenticator/islocked.sh
	sudo cp start.sh /opt/face-authenticator/start.sh
	sudo chmod +X /opt/face-authenticator/start.sh
	#greeter-setup-script=/opt/face-authenticator/start.sh
authorize:
	sudo cp $(image) /opt/face-authenticator/admin.jpg