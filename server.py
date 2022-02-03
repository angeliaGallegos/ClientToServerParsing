#################################################
#
#
# NAME: Angelia Gallegos-Loveland
#
# COURSE: CYBER 260-40
#
# SECTION: 2021F7A
#
# DATE: 9/25/2021
#
# PURPOSE: Extract the first partition entry from the MBR that is contained in the block.dd file
# The first partition entry starts at offset 0x1BE and ends at 0x1CD
# Server listens for chunk of data from client side and will then print out the status of the drive,
# the partition type and the starting address of the partition as an integer
#
#################################################


import socket
import ipaddress
import sys
import struct

# Function: connection
# Purpose: Connect / listen to the client side as well as parse the data
# Inputs: Address and port values from main
# Returns: Socket
def connection(address, port):

    # Setting up the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding address and port
    s.bind((address, port))
    print("Starting up on {0} port {1}".format(address, port))
    print()

    # Socket begins listening
    s.listen(15)
    print("Currently listening for data....")
    print()

    # Calling on the getData function and passing socket into it
    getData(s)
    return s

# Function: getData
# Purpose: Parse data from client side
# Inputs: Socket
# Returns: None
def getData(s):
    len = 512
    while True:
        c, address = s.accept()
        # Setting the variable data to the received length
        data = c.recv(len)
        # Setting mbr as the bytearray for the received data in which to parse
        mbr = bytearray(data)

        # Gathering the status byte
        status = mbr[0x1BE]

        # Gathering the partition type from address 0x1BE+4
        pType = mbr[0x1BE+4]

        # Unpacking the data for first section in partition
        section = struct.unpack("<i", mbr[0x1BE + 8:0x1BE + 12])

        # Making a neat output of parsed data
        print("Parsed information from client side")
        print("-----------------------------------")
        print()
        print("Status or Physical Drive: ", status)
        print("Partition Type: ", pType)
        print("First absolute section in partition: ", section[0])

        # Closing the connection
        c.close()
        sys.exit()

# Function: main
# Purpose: Main function of the program
# Inputs: None
# Returns: None
def main():
    # Creating a header for the program
    print("Week 4 Assignment - Server")
    print("--------------------------")
    print()

    # Gathering the address to be used
    try:
        address = str(ipaddress.ip_address(input("What IP address do you want to use [127.0.0.1]: ")))
    except:
        print("Default address set to 127.0.0.1")
        address = '127.0.0.1'
        print()

    # Gathering the port to be used
    try:
        port = int(input("What port would like to use [1530]: "))

    except:
        print("Default port set to 1530")
        port = 1530
        print()

    # Calling on the connection function and passing the address and the port values
    connection(address, port)

# Program starts here
main()
# Program ends here