import sys

def flip(arr, i):
   arr[:i] = arr[:i][::-1]

def maximo(arr, n):
   max = 0
   for i in range(1, n):
       if arr[i] > arr[max]:
           max = i
   return max

def pancake(arr):
   n = len(arr)
   flips = []
   
   if arr == list(range(n, 0, -1)):
       flip(arr, n)
       return [0] 

   for tam in range(n, 1, -1):
       max = maximo(arr, tam)
       
       if max != tam - 1:
           if max != 0:
               flip(arr, max + 1)
               flips.append(max + 1)
           
           flip(arr, tam)
           flips.append(tam)
   
   if not flips:
       return ["ORDENADO"]
   else:
       flips.append(0)
   return flips

def main():
   input = sys.stdin.read
   data = input().splitlines()
   
   casos = int(data[0])
   ordenado = []
   
   for i in range(1, casos + 1):
       pancakes = list(map(int, data[i].split()))
       resp = pancake(pancakes)
       ordenado.append(" ".join(map(str, resp)) if isinstance(resp, list) else resp)
   
   for resp in ordenado:
       print(resp)

if __name__ == "__main__":
   main()

