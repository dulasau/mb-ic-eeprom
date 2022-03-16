# Mercedes-Benz Instrument Cluster EEPROM read/write tool for Raspberry Pi

## Setup
```console
sudo apt-get install python3-smbus python-dev python3-dev python3-pip i2c-tools
```
```console
pip3 install progressbar
```
```console
sudo chmod +x eeprom.py
```

## Read EEPROM
```console
./eeprom.py -r output.bin
```

## Write EEPROM
```console
./eeprom.py -w input.bin
```

