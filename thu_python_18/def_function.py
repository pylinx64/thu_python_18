def stext():
	print('Hello world')
	
stext()

def sum2(a, b):
	s = a + b
	return s

z = sum2(2, 2)
print(z)

def exp(a, b):
	s = a ** b
	return s
	

#print(exp(200000, 30000))

import time
def test_1(a, b):
	print('-------------test_1----------------')
	et = time.time()
	res = exp(a, b)
	st = time.time()
	dt = st - et
	print('#time: ', dt)
	time.sleep(3)
	print('#result: ', res)
	
test_1(1000000, 1000000)
	
	
