# import some libraries ( modules) that we need!
import serial
import sys

def main():
    s = serial.Serial('/dev/ttyACM1', 115200, timeout=2) # (port, baudrate, set timeout 2 seconds)
    print("Waiting for boot signal")
    print(s.read()) # read serial data
    print("Writing sway command")
    s.write("".join(map(chr, [0x55, 0x0, 0x3, 0, 2, 72]))) # convert the list of asci to string character [U, null, end of text, null, ]
    # Ux00x03x00x02H'   
    print(s.read())
    print("Reading motor encoders")
    s.write("".join(map(chr, [0x55, 0x1, 0x12]))) # Ux01x12
    print(["0x%.02x " % ord(x) for x in s.read(12)]) # 12 means number of bytes to read. #ord() converts the input to interger that represents unicode

if __name__ == '__main__': # when the code is executed
    sys.exit(main())