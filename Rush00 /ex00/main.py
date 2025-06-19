class FarmTask:
    def __init__(self, name: str, date: str, task_type: str):
        self.name = name
        self.date = date
        self.task_type = task_type

class TaskManager:
    def __init__(self):
        self.tasks: List[FarmTask] = []
    
    def add_task(self, name: str, date: str, task_type: str):
        """เพิ่มการจองโรงแรม"""
        new_task = FarmTask(name, date, task_type)
        self.tasks.append(new_task)
        print("จองสำเร็จ")
    
    def show_all_tasks(self):
        """แสดงรายการจอง"""
        if not self.tasks:
            print("ยังไม่มีการจอง")
            return
        
        print("\nรายการจองทั้งหมด:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.date} – {task.name} ({task.task_type})")
    
    def delete_task(self, task_index: int):
        """ยกเลิกการจองตามลำดับที่ระบุ"""
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"ยกเลิกการจอง: {removed_task.name} แล้ว")
        else:
            print("การจองไม่ถูกต้อง")
    
    def summarize_tasks(self):
        """สรุปจำนวนการจอง"""
        if not self.tasks:
            print("ยังไม่มีการจอง")
            return
        
        type_counts: Dict[str, int] = {}
        for task in self.tasks:
            type_counts[task.task_type] = type_counts.get(task.task_type, 0) + 1
        
        print("\nสรุปจำนวนการจองแต่ละห้อง:")
        for task_type, count in type_counts.items():
            print(f"- {task_type}: {count} จอง")

def display_menu():
    """แสดงการจอง"""
    print("\n" + "="*40)
    print("whoatreyou hotel")
    print("="*40)
    print("1. เพิ่มการจอง")
    print("2. แสดงรายการจองทั้งหมด")
    print("3. ยกเลิกการจอง")
    print("4. สรุปจำนวนการจองของแต่ละห้อง")
    print("5. เสร็จสิ้นการจอง")
    print("="*40)

def main():
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        
        if choice == "1":
            name = input("ป้อนเลขห้อง: ")
            date = input("ป้อนวันที่จอง (dd/mm/yyyy): ")
            task_type = input("ประเภทห้อง (เตียงเดี่ยว (01)/เตียงคู่ (02)/ห้องครอบครัว(03)): ")
            manager.add_task(name, date, task_type)
        
        elif choice == "2":
            manager.show_all_tasks()
        
        elif choice == "3":
            manager.show_all_tasks()
            if manager.tasks:
                try:
                    task_num = int(input("จำนวนห้องที่ต้องการยกเลิก: "))
                    manager.delete_task(task_num)
                except ValueError:
                    print("กรุณาป้อนเลขห้อง")
        
        elif choice == "4":
            manager.summarize_tasks()
        
        elif choice == "5":
            print("\nขอบคุณที่ใช้บริการ whoareyou hotel!")
            break
        
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()