#!/usr/bin/env python3

import argparse
import smbus
import progressbar
import time


parser = argparse.ArgumentParser(description='Mercedes IC eeprom r/w tool')
group = parser.add_mutually_exclusive_group(required=True)
#parser.add_argument('-n', type=int, help='Number of attempts')
group.add_argument('-r', action='store_true', help='Read eeprom')
group.add_argument('-w', action='store_true', help='Write eeprom')
parser.add_argument('-f', default='output.bin', help='Output file name')

args = parser.parse_args()

if args.w:
  parser.error('Write is not supported yet')

addresess = [0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57]
bus = smbus.SMBus(1)
bar = progressbar.ProgressBar(maxval=2048, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

def read_eeprom():
  data = []

  print('Reading eeprom...')
  bar.start()
  progress = 0

  for address in addresess:
    for i in range(0, 256):
      data.append(bus.read_byte_data(address, i))
      time.sleep(0.005)
      progress = progress + 1
      bar.update(progress)
  bar.finish()

  with open(args.f, 'wb') as binary_file:
    binary_file.write(bytes(bytearray(data)))

  print('Done! Read {} bytes'.format(len(data)))


if args.r:
  read_eeprom()
