import serial
import struct
import matplotlib.pyplot as plt
import time

def writeSettings(p_pacingMode: int, p_lowrateInterval: float, p_vPaceWidth: float, p_VRP: int, p_aPaceWidth: float, p_ARP:int, p_BPM: float, p_upperrateInterval: float, p_AV: float, p_isAdaptive: int, p_MSR: int, p_aPaceAmp: float, p_vPaceAmp: float, p_hysteresis: int,p_hystInterval: float):
    debug = False
    error_counter = 0
    
    byte_values = b''

    start = b'\x16'
    function = b'\x55'

    # Start Byte
    byte_values += start

    # Writing Byte
    byte_values += function

    # Pacing Mode int8
    if 0 <= p_pacingMode <= 5:
        byte_values += p_pacingMode.to_bytes(1, 'little')
        if debug:
            print("Pacing Mode: ", p_pacingMode)
    else:
        error_counter += 1
        
        p_pacingMode = 0
        byte_values += p_pacingMode.to_bytes(1, 'little')
        if debug:
            print("Pacing Mode out of range: ", p_pacingMode)

    # Low Rate Interval single
    if (30 <= p_lowrateInterval <= 175) and (p_lowrateInterval < p_upperrateInterval):
        byte_values += bytearray(struct.pack('f', p_lowrateInterval))
        if debug:
            print("Low Rate Interval: ", p_lowrateInterval)
    else:
        error_counter += 1

        p_lowrateInterval = 60
        byte_values += bytearray(struct.pack('f', p_lowrateInterval))
        if debug:
            print("Low Rate Interval out of range: ", p_lowrateInterval)

    # V Pace Width single
    if 0.05 <= p_vPaceWidth <= 1.9:
        byte_values += bytearray(struct.pack('f', p_vPaceWidth))
        if debug:
            print("V Pace Width: ", p_vPaceWidth)
    else:
        error_counter += 1
        
        p_vPaceWidth = 1.0
        byte_values += bytearray(struct.pack('f', p_vPaceWidth))
        if debug:
            print("vPaceWidth out of range: ", p_vPaceWidth)

    # VRP int16
    if 150 <= p_VRP <= 500:
        byte_values += p_VRP.to_bytes(2, 'little')
        if debug:
            print("VRP: ", p_VRP)
    else:
        error_counter += 1

        p_VRP = 320
        byte_values += p_VRP.to_bytes(2, 'little')
        if debug:
            print("VRP out of range: ", p_VRP)

    # A Pace Width single
    if 0.05 <= p_aPaceWidth <= 1.9:
        byte_values += bytearray(struct.pack('f', p_aPaceWidth))
        if debug:
            print("A Pace Width: ", p_aPaceWidth)
    else:
        error_counter += 1

        p_aPaceWidth = 1.0
        byte_values += bytearray(struct.pack('f', p_aPaceWidth))
        if debug:
            print("aPaceWidth out of range: ", p_aPaceWidth)

    # ARP int16
    if 150 <= p_ARP <= 500:
        byte_values += p_ARP.to_bytes(2, 'little')
        if debug:
            print("Low Rate Interval: ", p_ARP)
    else:
        error_counter += 1

        p_ARP = 250
        byte_values += p_ARP.to_bytes(2, 'little')
        if debug:
            print("ARP out of range: ", p_ARP)
    
    # BPM single
    if 0 <= p_BPM <= 255:
        byte_values += bytearray(struct.pack('f', p_BPM))
        if debug:
            print("BPM: ", p_BPM)
    else:
        error_counter += 1

        p_BPM = 60
        byte_values += bytearray(struct.pack('f', p_BPM))
        if debug:
            print("BPM out of range: ", p_BPM)    

    # Upper Rate Interval single
    if (50 <= p_upperrateInterval <= 175) and (p_upperrateInterval > p_lowrateInterval):
        byte_values += bytearray(struct.pack('f', p_upperrateInterval))
        if debug:
            print("Upper Rate Interval: ", p_upperrateInterval)
    else:
        error_counter += 1

        p_upperrateInterval = 120
        byte_values += bytearray(struct.pack('f', p_upperrateInterval))
        if debug:
            print("Upper Rate Interval out of range: ", p_upperrateInterval)

    # AV single
    if 70 <= p_AV <= 300:
        byte_values += bytearray(struct.pack('f', p_AV))
        if debug:
            print("AV: ", p_AV)
    else:
        error_counter += 1

        p_AV = 150
        byte_values += bytearray(struct.pack('f', p_AV))
        if debug:
            print("AV out of range: ", p_AV)

    # isAdaptive uint8
    if 0 <= p_isAdaptive <= 1:
        byte_values += p_isAdaptive.to_bytes(1, 'little')
        if debug:
            print("isAdaptive: ", p_isAdaptive)
    else:
        error_counter += 1

        p_isAdaptive = 0
        byte_values += p_isAdaptive.to_bytes(1, 'little')
        if debug:
            print("isAdaptive out of range: ", p_isAdaptive)

    # MSR uint8
    if 0 <= p_MSR <= 175:
        byte_values += p_MSR.to_bytes(1, 'little')
        if debug:
            print("MSR: ", p_MSR)
    else:
        error_counter += 1

        p_MSR = 120
        byte_values += p_MSR.to_bytes(1, 'little')
        if debug:
            print("MSR out of range: ", p_MSR)

    # Atrium Pace Amplitude single
    if 500 <= p_aPaceAmp <= 5000:
        byte_values += bytearray(struct.pack('f', p_aPaceAmp))
    else:
        byte_values += bytearray(struct.pack('f', 3500))

    # Ventricle Pace Amplitude single
    if 500 <= p_vPaceAmp <= 5000:
        byte_values += bytearray(struct.pack('f', p_vPaceAmp))
    else:
        byte_values += bytearray(struct.pack('f', 3500))

    #Hysteresis uint8
    if 0 <= p_hysteresis <= 1:
        byte_values += p_hysteresis.to_bytes(1, 'little')
    else:
        p_hysteresis = 0
        byte_values += p_hysteresis.to_bytes(1, 'little')

    #Hysteresis Interval single
    if 0 <= p_hystInterval <= 200:
        byte_values += bytearray(struct.pack('f', p_hystInterval))
    else:
        byte_values += bytearray(struct.pack('f', 100))


    # Send message
    baud_rate = 115200
    
    ser = serial.Serial('COM4', baud_rate)
    if debug:
        print(f"Serial port {'COM4'} opened at {baud_rate} baud")
    
    #print(ser.write(byte_values))
    ser.write(byte_values)
    if debug:
        print(["0x%02x" % b for b in byte_values])

    ser.close()

    print(readSettings(115200))
    if debug:
        print("Serial port closed")
    
    return error_counter

def readSettings(baud_rate):
    byte_values = b'\x16\x22'

    for i in range(44):
        byte_values += b'\x00'

    #print(["0x%02x" % b for b in byte_values])

    ser = serial.Serial('COM4', baud_rate, timeout=2)
    ser.write(byte_values)
    
    #time.sleep(0.3)
    BytesRead = ser.read(60)
    #time.sleep(0.3)
    
    p_pacingMode = BytesRead[0]
    p_lowrateInterval = struct.unpack('f', BytesRead[1:5])[0]
    p_vPaceWidth = struct.unpack('f', BytesRead[5:9])[0]
    p_VRP = int.from_bytes(BytesRead[9:11], 'little')
    p_aPaceWidth = struct.unpack('f', BytesRead[11:15])[0]
    p_ARP = int.from_bytes(BytesRead[15:17], 'little')
    p_BPM = struct.unpack('f', BytesRead[17:21])[0]
    p_upperrateInterval = struct.unpack('f', BytesRead[21:25])[0]
    p_AV = struct.unpack('f', BytesRead[25:29])[0]
    p_isAdaptive = BytesRead[29]
    p_MSR = BytesRead[30]
    p_aPaceAmp =  struct.unpack('f', BytesRead[31:35])[0]
    p_vPaceAmp = struct.unpack('f', BytesRead[35:39])[0]
    p_hysteresis = BytesRead[39]
    p_hystInterval = struct.unpack('f', BytesRead[40:44])[0]

    ser.close()

    return [p_pacingMode, p_lowrateInterval, p_vPaceWidth, p_VRP, p_aPaceWidth, p_ARP, p_BPM, p_upperrateInterval, p_AV, p_isAdaptive, p_MSR, p_aPaceAmp, p_vPaceAmp, p_hysteresis,p_hystInterval]

def get_egram():

    byte_values = b'\x16\x22'

    for i in range(44):
        byte_values += b'\x00'

    ser = serial.Serial('COM4', 115200, timeout=1)
    
    ser.write(byte_values)

    BytesRead = ser.read(60)

    v_SIGNAL = struct.unpack('d', BytesRead[44:52])[0]
    a_SIGNAL = struct.unpack('d', BytesRead[52:60])[0]

    ser.reset_input_buffer()

    ser.close()

    return [v_SIGNAL, a_SIGNAL]

def plot_egram(chamber: int):
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []
    count = 0
    start_time = time.time()

    while(True):
        v_val = get_egram()[chamber]

        xs.append(time.time() - start_time)
        count = count + 1
        ys.append(5.0*(-v_val + 0.6))
            
        xs = xs[-50:]
        ys = ys[-50:]

        ax.clear()
        ax.plot(xs, ys)
        fig.canvas.draw()
        fig.canvas.flush_events()

        time.sleep(0.001)

    

#print(readSettings(115200))

#writeSettings(5, 60.0, 1.0, 320, 1.0, 250, 80, 120, 80, 1, 175, 3500, 3500, 0, 100)
#print(readSettings(115200))

#plot_egram()
