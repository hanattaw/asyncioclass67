import asyncio
import time

async def make_coffee():
    print("Start making coffee...")
    await asyncio.sleep(1)  # Simulate waiting 1 second
    print("Coffee is brewing...")
    await asyncio.sleep(5)  # Simulate brewing coffee for 5 seconds
    print("Coffee is ready!")

async def fry_eggs():
    print("Start frying eggs...")
    await asyncio.sleep(1)  # Simulate waiting 1 second
    print("Eggs are frying...")
    await asyncio.sleep(3)  # Simulate frying eggs for 3 seconds
    print("Eggs are ready!")


async def main():
    start_time = time.time()
    await asyncio.gather(
        make_coffee(),
        fry_eggs()
    )
    end_time = time.time()
    total_time = end_time - start_time
    print(f"breakfast is ready in: {total_time:.2f} min")


# async def tose_base():
#     print("Start frying eggs...")
#     await asyncio.sleep(1)  # Simulate waiting 1 second
#     print("Eggs are frying...")
#     await asyncio.sleep(3)  # Simulate frying eggs for 3 seconds
#     print("Eggs are ready!")

# Run the asynchronous main function
asyncio.run(main())
