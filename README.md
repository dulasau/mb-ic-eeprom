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

## Connection
| 24c16/24u17   | Raspberry Pi |
| ------------- | ------------ |
| GND (#4)      | GND (#6)     |
| VCC (#8)      | 3V3 (#1)     |
| SCL (#6)      | SCL (#5)     |
| SDA (#5)      | SDA (#3)     |

![PXL_20220315_044212041](https://user-images.githubusercontent.com/7697859/158518567-923fd7b8-71a3-4009-978f-6a09aadaf5f4.jpg)

## Read EEPROM
```console
./eeprom.py -r output.bin
```

## Write EEPROM
```console
./eeprom.py -w input.bin
```

