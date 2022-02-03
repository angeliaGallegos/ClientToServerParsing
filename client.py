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

import ipaddress
import sys
import socket

# Function: createConnection
# Purpose: Establishes the connection with the server side
# Inputs: Address and port values from main
# Returns: None
def createConnection(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Starting up on {0} port {1}".format(address, port))
    print()

    # Connecting socket to address and port
    try:
        s.connect((address, port))

        # Opening the block.dd in read binary as mbr
        file1 = open("block.dd", "rb")
        # Setting up the bytearray
        mbr = bytearray()

        try:
            # Setting the array value to the first 512 bytes
            mbr = file1.read(512)
            # Sending mbr data to server
            s.send(mbr)
            print("Chunk sent!")
        finally:
            # Closing out the file
            file1.close()
        # Closing out the socket
        s.close()

    # Error handling exception
    except socket.error as errorMsg:
        print('Connection was unsuccessful. Error code : ' + str(errorMsg[0]) + 'Message' + errorMsg[1])
        sys.exit(1)

# Function: main
# Purpose: Main function of the program
# Inputs: None
# Returns: None
def main():
    # Creating a header for the program
    print("Week 4 Assignment - Client")
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

        # Calling on the connection function and passing the address and port values
        createConnection(address, port)

# Program starts here
main()
# Program ends here