from smbus import SMBus
import time
bus = SMBus(1)

DEVICE_ADDRESS = 0x54 # address of PIXY camera



while True:
    pixyPacket = bus.read_word_data(DEVICE_ADDRESS,0)
#     print(hex(pixyPacket))
    
    if pixyPacket == 0xaa55:
        pixyPacket = bus.read_word_data(DEVICE_ADDRESS,0)
#         print("1")
        if pixyPacket ==0xaa55:
            checksum = bus.read_word_data(DEVICE_ADDRESS,0)
            signature = bus.read_word_data(DEVICE_ADDRESS,0)
            xctr = bus.read_word_data(DEVICE_ADDRESS,0)
            yctr = bus.read_word_data(DEVICE_ADDRESS,0)
            width = bus.read_word_data(DEVICE_ADDRESS,0)
            height = bus.read_word_data(DEVICE_ADDRESS,0)
            
            print("Signature: ", signature)
            print("X center: ", xctr)
            print("y center: ", yctr)
            print("Width: ", width)
            print("Height: ", height)
            print("---------------------------")
#             print("2")
    time.sleep(0.1)