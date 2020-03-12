import sys, time, platform
from numba import jit
from numba import njit 
stdout = sys.stdout

BAILOUT = 16
MAX_ITERATIONS = 10000

@njit(fastmath=True)
def mandelbrot(x, y):
    cr = y - 0.5
    ci = x
    zi = 0.0
    zr = 0.0
    i = 0

    while True:
      i += 1
      temp = zr * zi
      zr2 = zr * zr
      zi2 = zi * zi
      zr = zr2 - zi2 + cr
      zi = temp + temp + ci
 		  
      if zi2 + zr2 > BAILOUT:
        return i
      if i > MAX_ITERATIONS:
        return 0

def run():
    output = ''
    for y in range(-99, 99):
        for x in range(-99, 99):
            i = mandelbrot(x/100.0, y/100.0)
        
            if i == 0:
                output += '*'
            else:
                output += ' '

        output += '\n'
    print(output)


if __name__ == "__main__":
    t = time.time()
    run()
    print('\nPython ' + platform.python_version() + ' Elapsed %.04f' % (time.time() - t))

