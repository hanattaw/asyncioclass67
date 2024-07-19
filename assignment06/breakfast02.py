import time
import asyncio

class Coffee:
    pass

class Eggs:
    pass

class Bacon:
    pass

class Toast:
    pass        

class Juice:
    pass    

def PourCoffee():
    print(f"{time.ctime()} - Begin pour coffee...")
    time.sleep(2)  # รอ 2 วินาที
    print(f"{time.ctime()} - Finish pour coffee...")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} - Begin apply butter...")
    await asyncio.sleep(1)  # รอ 1 วินาที
    print(f"{time.ctime()} - Finish apply butter...")

async def FryEggs(egg_count):
    print(f"{time.ctime()} - Begin fry eggs...")
    print(f"{time.ctime()} - Heat pan to fry eggs")
    await asyncio.sleep(1)  # รอ 1 วินาที
    for egg in range(egg_count):
        print(f"{time.ctime()} - Frying egg {egg + 1}")
        await asyncio.sleep(1)  # รอ 1 วินาที
    print(f"{time.ctime()} - >>>>>>>> Fry eggs are ready...")
    return Eggs()

async def FryBacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    await asyncio.sleep(2)  # รอ 2 วินาที
    print(f"{time.ctime()} - Finish fry bacon...")
    print(f"{time.ctime()} - >>>>>>>> Fry bacon is ready...")
    return Bacon()

async def ToastBread(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread {slice + 1}")
        await asyncio.sleep(1)  # รอ 1 วินาที
        print(f"{time.ctime()} - Bread {slice + 1} toasted")
        await ApplyButter()
        print(f"{time.ctime()} - Toast {slice + 1} ready")
    print(f"{time.ctime()} - >>>>>>>>>> Toast is ready")
    return Toast()

async def PourJuice():
    print(f"{time.ctime()} - Begin pour juice...")
    await asyncio.sleep(1)  # รอ 1 วินาที
    print(f"{time.ctime()} - Finish pour juice...")
    return Juice()

async def main():
    start_time = time.perf_counter()
    
    PourCoffee()
    print(f"{time.ctime()} - >>>>>>>>>>> Coffee is ready\n")

    # เริ่มทอดไข่และเบคอน
    eggs_task = asyncio.create_task(FryEggs(2))
    bacon_task = asyncio.create_task(FryBacon())
    
    # เริ่มการทำขนมปัง
    toast_task = asyncio.create_task(ToastBread(2))
    
    # รอให้ไข่และเบคอนเสร็จสิ้น
    await asyncio.gather(eggs_task, bacon_task, toast_task)


    print(f"\n{time.ctime()} - >>>>>>>>>> Nearly finished...")
    await PourJuice()

    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"{time.ctime()} - Breakfast cooked in {elapsed:.10f} seconds.")

if __name__ == "__main__":   
    asyncio.run(main())