print("l;ylfu")
#โปรแกรมคำนวณเลข ฐานสอง
def convert_to_binary(n):
    return bin(n).replace("0b", "")

number = int(input("กรุณาป้อนเลขฐานสิบ: "))
print(f"เลขฐานสองคือ: {convert_to_binary(number)}")
