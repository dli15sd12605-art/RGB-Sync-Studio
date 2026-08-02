import asyncio
from bleak import BleakScanner

async def scan():
    print("Scanning for Bluetooth devices...\n")

    devices = await BleakScanner.discover(timeout=8)

    if not devices:
        print("No Bluetooth devices found.")
        return

    for device in devices:
        print(f"{device.name or 'Unknown'}")
        print(f"Address : {device.address}")
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(scan())
