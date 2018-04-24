# Face Authenticator
Script that unlocks your Gnome 3 desktop if your face is present.

## How it works
Using a python [face recognition](https://github.com/ageitgey/face_recognition) library the program queries d-bus to unlock your Gnome 3 desktop.

## Warning
This drasticaly increases the risk of a random stranger unlocking your computer. Although the face authentication algorithm may be sound, a simple image of your face will suffice to unlock your device.

## Installation

I can only confirm this program works with Ubuntu 17.10 and Gnome 3.

```
    git clone https://github.com/maxchehab/face-authenticator
    cd face-authenticator
    make install
```
This will install the neccessary files to run the authentication deamon.

You must now provide the program with an image of your face. 

```
    make authorize image="/path/to/your/face.jpg"
```

Finally, restart your computer or gdm.

## Uninstallation
To remove the authenticator simply:

```
    rm -rf $HOME/.face-authenticator
    rm $HOME/.config/autostart/face-authenticator.desktop
    reboot
```

## Contact
Feel free to reach out to me at [twitter](https://twitter.com/maxchehab) or report an [issue](https://github.com/maxchehab/face-authenticator/issues) if there are any problems.

