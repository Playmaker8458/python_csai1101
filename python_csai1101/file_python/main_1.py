schedule = {
    'หัวหน้าภาค': {
        'อังคาร': {"บ่าย" : '14:00-15:00'},
        'พฤหัส': {"บ่าย" : '13:00-15:00'}
    },
    'เลขาภาค': {
        'อังคาร': {"เช้า" : '10:00-11:00', "บ่าย" : '13:00-14:00'},
        'พฤหัส': {"บ่าย" : '14:00-15:00'}
    },
    'อาจารย์': {
        'อังคาร': {"บ่าย" : '13:00-14:00'},
        'พฤหัส': {"เช้า" : '09:00-10:00', "บ่าย" : '14:00-15:00'}
    }
}

position_input = input("Enter you position: ")
if position_input in list(schedule.keys()):

    day_input = input("Enter you day: ") 
    free_time = ", ".join(list(schedule[position_input][day_input].keys()))
    spare_time = ", ".join(list(schedule[position_input][day_input].values()))
    
    if position_input == "หัวหน้าภาค" and day_input in list(schedule['หัวหน้าภาค'].keys()):
        print(f"ตำแหน่ง : {position_input} | วันว่าง : {day_input}\nช่วงว่าง : {free_time} | เวลาว่าง : {spare_time}")
    elif position_input == "เลขาภาค" and day_input in list(schedule['เลขาภาค'].keys()):
        print(f"ตำแหน่ง : {position_input} | วันว่าง : {day_input}\nช่วงว่าง : {free_time} | เวลาว่าง : {spare_time}")
    elif position_input == "อาจารย์" and day_input in list(schedule['อาจารย์'].keys()):
        print(f"ตำแหน่ง : {position_input} | วันว่าง : {day_input}\nช่วงว่าง : {free_time} | เวลาว่าง : {spare_time}")
    else:
        print(f"ไม่มีวันว่างเพราะ วัน {day_input} เป็นวันที่ต้องทำงาน และ ประชุม")
else:
    print("ไม่มีตำแหน่งงานนี้อยู่ในฐานข้อมูล")