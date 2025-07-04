#导入需要的库
from machine import UART
from fpioa_manager import fm

#将串口资源注册到某一个具体的引脚上
fm.register(24, fm.fpioa.UART1_TX, force=Ture)
fm.register(25, fm.fpioa.UART1_RX, force=Ture)

#构造函数，初始化一个串口对象
uart_A = UART(UART.UART1, 115200, 8, 0, 1, timeout=1000, read_buf_len=4096)
#数据宽度、奇偶校验位、停止位可以省略不写，默认为8,0,1

#进入程序死循环
while(1):
    read_data = uart_A.read()#读取串口字节类型的数据
    if read_data:
        read_str = read_data.decode('utf-8')#将字节类型数据解码成字符串数据
        uart_A.write(read_str)#将解码后的数据复制到read_str，并发送给上位机
