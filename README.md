# RGB Daylight controlled by BLYNK via RPi

A Raspberry project for RGB LED strip control through smartphone with BLYNK IoT app

Uses 500Hz PWM signal with 0.1% steps (1000 resolution)

### Required repos
- [BlynkLib](https://github.com/vshymanskyy/blynk-library-python)
- [Astral](https://sffjunkie.github.io/astral/)
- [Pi-Blaster](https://github.com/sarfata/pi-blaster)
- [rgb-daylight](https://github.com/AkBKukU/rgb-daylight)

## Setup

```
sudo apt install python3-astral
sudo apt-get install autoconf pkg-config
git clone https://github.com/AkBKukU/rgb-daylight.git
cd rgb-daylight
git clone https://github.com/vshymanskyy/blynk-library-python.git https://github.com/sarfata/pi-blaster.git https://github.com/zserub/Daylight.git
cp pi-blaster.c ./pi-blaster
cd pi-blaster
./autogen.sh
./configure
make
```

Follow the introduction of [rgb-daylight](https://github.com/AkBKukU/rgb-daylight)
In rgb-daylight.service change the path for RGBdaylight_blynk_basic.py then `sudo cp rgb-daylight.service /systemd`
Write your token in the `blynk = BlynkLib.Blynk('asd')`

### Check astral for ideal sunshine
Go into settings.json and change latitude and longitude then start rgb-daylight.py and check the timings.