#!/usr/bin/env python3

import argparse
import smbus
from os.path import exists
import progressbar
import time


parser = argparse.ArgumentParser(description='Mercedes IC eeprom r/w tool')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-r', metavar='output-file-name', help='read eeprom')
group.add_argument('-w', metavar='file-name', help='write eeprom')
args = parser.parse_args()


addresses = [0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57]
bus = smbus.SMBus(1)
bar = progressbar.ProgressBar(maxval=2048, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

def read_eeprom(file_name=None, progress_message='Reading eeprom...', no_end_message=False):
  data = []

  print(progress_message)
  bar.start()
  progress = 0

  for address in addresses:
    for i in range(0, 256):
      data.append(bus.read_byte_data(address, i))
      time.sleep(0.005)
      progress = progress + 1
      bar.update(progress)
  bar.finish()

  if file_name:
    with open(file_name, 'wb') as binary_file:
      binary_file.write(bytes(bytearray(data)))

  if not no_end_message:
    print('Done! Read {} bytes'.format(len(data)))

  return bytearray(data)


def backup_eeprom():
  backup_file_name = 'backup.bin'
  i = 1

  while exists(backup_file_name):
    backup_file_name = 'backup{}.bin'.format(i)
    i = i + 1
  
  read_eeprom(backup_file_name, 'Backing up eeprom...')


def verify_eeprom(original_data):
  data = read_eeprom(progress_message='\nVerifying eeprom...', no_end_message=True)
  if original_data == data:
    print('\nVerification Ok')
  else:
    print('\nVerification Error')
  

def write_eeprom(file_name):
  if not exists(file_name):
    print('Can\'t fined {}'.format(file_name))
    return

  backup_eeprom()

  print("\nWriting eeprom...")
  bar.start()
  progress = 0

  with open(file_name, 'rb') as binary_file:
    data = bytearray(binary_file.read())
    data_index = 0

    for address in addresses:
      for i in range(0, 256):
        bus.write_byte_data(address, i, data[data_index])
        time.sleep(0.005)
        data_index = data_index + 1
        bar.update(data_index)
  bar.finish()

  print('\nDone! Wrote {} bytes'.format(len(data)))
  verify_eeprom(data)


if args.r:
  print(args.r)
  read_eeprom(args.r)
else:
  write_eeprom(args.w)

