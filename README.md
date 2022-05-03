# Educational research of a Danfoss ECO2 thermostat that uses Bluetooth Low Energy 4.2


## Info
The hardware has the SWD port disabled

The firmware seems to be in two parts, one bootloader with BLE firmware downloading capability and one application part.

The application part is running uC OS-III.

It seems like both the bootloader and application is sharing the same BLE software component.

## Programming header
```
                          ********
                     XRES *      * GND
                    SWDIO *      * P0.5 (RX/TX ?) like output
                   SWDCLK *      * VCC (3 V)
like input (RX/TX ?) P0.4 *      * VCC (3 V)
                           ******
```
              
              
## Links

https://blog.attify.com/the-practical-guide-to-hacking-bluetooth-low-energy/

https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-4-32-bit-arm-cortex-m0-mcu/cy8c4128lqi-bl563/

https://community.infineon.com/t5/Knowledge-Base-Articles/Format-of-cyacd-File-for-PSoC-3-or-PSoC-5LP-Bootloader-KBA216138/ta-p/249707

https://github.com/UnifiedEngineering/bootloaderhost/tree/master/cybootloaderutils

https://github.com/weston-embedded/uC-OS3

https://github.com/dreamscaperia/CYACDtoBIN_release

https://www.youtube.com/watch?v=q4CxE5P6RUE

## Endpoints found in android app:

https://simplesoftwaredownloadeco2endpoint.azurewebsites.net/api/eco2software/getbydeviceinfo

https://simplesoftwaredownloadeco2endpoint.azurewebsites.net/api/eco2software/getbymac

Firmware download basic authentication
```
eco2danfoss:biRbjCtsWjLk27
```
        
## OS
https://github.com/weston-embedded/uC-OS3


## CPU
```
Family 			PSOC4 4100-BLE 4.2
Parametrics			CY8C4128LQI-BL563
ADC 				SAR (1, 12-bit @ 806 ksps)
Analog Blocks (Universal) 	-
CAN 				0
CPU 				ARM Cortex-M0
CapSense 			N
Comparators 			2 
Continuous Time Blocks 	1 
DMA Channels 			8
EEPROM 			-
Family 			PSoC 4100BL
Flash 	256 kByte
Frequency   max 		24 MHz
GPIOs 				36 
I/O Pins (SIO) 		-
I/O Pins 			36 
JTAG and Si ID 		0x1A0811AA
LCD Direct Drive 		Y
Lead Ball Finish 		Pure Sn
On-chip Clock Generation (PLL) N
Operating Temperature min  max -40 °C   85 °C
Operating Voltage   min  max 	1.9 V   5.5 V
Operational Amplifier 		2
Peak Reflow Temp 		260 °C
Publish in NPSG 		Y
Publish in PSG 		Y
Required Kit 			None
SRAM 				32 kByte
Serial Communication Blocks 	2 
Timer/Counter/PWM Blocks 	4 
USB I/O 			-
USB Type 			None
Universal Digital Blocks 	- 
```

## cyacd converter:
```
cat v2.08.cyacd | cut -c 12- | rev | cut -c 4- | rev | xxd -r -p > v2.08.bin
```

## Bluetooth

Bluetooth crypto XXTEA, big endian, setup secret is the key

Bluetooth UUIDs
```
00002902-0000-1000-8000-00805f9b34fb client characteristic config

00060000-F8CE-11E4-ABF4-0002A5D5C51B ota
00060001-F8CE-11E4-ABF4-0002A5D5C51B ota writer

10020000-2749-0001-0000-00805F9B042F eco2service
10020001-2749-0001-0000-00805F9B042F pin
10020002-2749-0001-0000-00805F9B042F thermostat code
10020003-2749-0001-0000-00805F9B042F settings
10020004-2749-0001-0000-00805f9b042f undefined4
10020005-2749-0001-0000-00805F9B042F manual temperature
10020006-2749-0001-0000-00805F9B042F device name
10020007-2749-0001-0000-00805F9B042F bootloader
10020008-2749-0001-0000-00805F9B042F epoc time
10020009-2749-0001-0000-00805F9B042F error code
1002000A-2749-0001-0000-00805F9B042F language
1002000B-2749-0001-0000-00805F9B042F setup secret
1002000C-2749-0001-0000-00805F9B042F update token
1002000D-2749-0001-0000-00805F9B042F schedule1
1002000E-2749-0001-0000-00805F9B042F schedule2
1002000F-2749-0001-0000-00805F9B042F schedule3
10020010-2749-0001-0000-00805F9B042F undefined1
10020011-2749-0001-0000-00805F9B042F undefined2
10020012-2749-0001-0000-00805f9b042f undefined3

select-attribute 10020000-2749-0001-0000-00805F9B042F
read
select-attribute 10020001-2749-0001-0000-00805F9B042F
read
select-attribute 10020002-2749-0001-0000-00805F9B042F
read
select-attribute 10020003-2749-0001-0000-00805F9B042F
read
select-attribute 10020004-2749-0001-0000-00805f9b042f
read
select-attribute 10020005-2749-0001-0000-00805F9B042F
read
select-attribute 10020006-2749-0001-0000-00805F9B042F
read
select-attribute 10020007-2749-0001-0000-00805F9B042F
read
select-attribute 10020008-2749-0001-0000-00805F9B042F
read
select-attribute 10020009-2749-0001-0000-00805F9B042F
read
select-attribute 1002000A-2749-0001-0000-00805F9B042F
read
select-attribute 1002000B-2749-0001-0000-00805F9B042F
read
select-attribute 1002000C-2749-0001-0000-00805F9B042F
read
select-attribute 1002000D-2749-0001-0000-00805F9B042F
read
select-attribute 1002000E-2749-0001-0000-00805F9B042F
read
select-attribute 1002000F-2749-0001-0000-00805F9B042F
read
select-attribute 10020010-2749-0001-0000-00805F9B042F
read
select-attribute 10020011-2749-0001-0000-00805F9B042F
read
select-attribute 10020012-2749-0001-0000-00805f9b042f
read

select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service000a
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service000a/char000b
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service000a/char000b/desc000d
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013/char0014
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013/char0016
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013/char0018
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013/char001a
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013/char001c
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013/char001e
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0013/char0020
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0023
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0023/desc0025
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0026
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0026/desc0028
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0029
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0029/desc002b
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char002c
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char002c/desc002e
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char002f
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char002f/desc0031
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0032
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0032/desc0034
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0035
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0035/desc0037
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0038
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0038/desc003a
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char003b
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char003b/desc003d
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char003e
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char003e/desc0040
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0041
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0041/desc0043
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0044
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0044/desc0046
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0047
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char0047/desc0049
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char004a
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service0022/char004a/desc004c
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service004d
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service004d/char004e
attribute-info
select-attribute /org/bluez/hci0/dev_00_04_2F_5F_XX_XX/service004d/char004e/desc005attribute-info


Device 00:04:2F:5F:XX:XX (public)
        Name: 2;0:04:2F:5F:XX:XX;eTRV
        Alias: 2;0:04:2F:5F:XX:XX;eTRV
        Paired: no
        Trusted: yes
        Blocked: no
        Connected: yes
        LegacyPairing: no
        UUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)
        UUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)
        UUID: Device Information        (0000180a-0000-1000-8000-00805f9b34fb)
        UUID: Battery Service           ()
        UUID: Vendor specific           (10010000-2749-0001-0000-00805f9b042f)
        UUID: Vendor specific           (10020000-2749-0001-0000-00805f9b042f)
```

