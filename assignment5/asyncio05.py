from random import random
import asyncio

# ฟังก์ชันแบบ asynchronous สำหรับการทำอาหาร
async def cook_food(food_name):
    # สร้างเวลาการทำอาหารที่เป็นสุ่มระหว่าง 1 ถึง 2 วินาที
    cook_time = 1 + random()
    # แสดงข้อความว่าเริ่มทำอาหารและใช้เวลาเท่าไหร่
    print(f"Microwave ({food_name}): Cooking {cook_time} seconds...")
    # หยุดการทำงานของฟังก์ชันนี้เป็นเวลา cook_time วินาที
    await asyncio.sleep(cook_time)
    # แสดงข้อความว่าทำอาหารเสร็จแล้ว
    print(f"Microwave ({food_name}): Finished cooking")
    # คืนค่าเป็นชื่ออาหารและเวลาในการทำ
    return food_name, cook_time

# กำหนดฟังก์ชันหลักแบบ asynchronous
async def main():
    tasks = [
        asyncio.create_task(cook_food("Rice")),
        asyncio.create_task(cook_food("Noodle")), 
        asyncio.create_task(cook_food("Curry"))
    ]
    # รอจนกว่า tasks ทั้งหมดจะเสร็จ
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"Completed task:{len(done)}")
    # ดึง task ที่เสร็จแล้วออกจากชุด done
    completed_task = done.pop()
    # รอผลลัพธ์จาก task ที่เสร็จแล้ว
    meal, cook_time = await completed_task
    
    # แสดงชื่อและเวลาที่ใช้ในการทำอาหารที่เสร็จแล้ว
    print(f" - {meal} is completed in {cook_time} seconds")
    # แสดงจำนวน task ที่ยังไม่เสร็จ
    print(f"Uncompleted task: {len(pending)}")

# เริ่มต้น event loop และรันฟังก์ชันหลัก main
asyncio.run(main())
