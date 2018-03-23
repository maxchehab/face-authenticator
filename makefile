install:
	mkdir -p $(HOME)/.face-authenticator/authorized
	cp authenticate.py $(HOME)/.face-authenticator/authenticate.py
	cp start.sh $(HOME)/.face-authenticator/start.sh
	chmod +x $(HOME)/.face-authenticator/start.sh
	envsubst < face-authenticator.desktop > $(HOME)/.config/autostart/face-authenticator.desktop 
	chmod +x $(HOME)/.config/autostart/face-authenticator.desktop 

authorize:
	cp $(image) $(HOME)/.face-authenticator/admin.jpg