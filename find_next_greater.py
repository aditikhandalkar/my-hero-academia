    from collections import deque
     
     
    def findNextGreater(input):
     
        n = len(input)
        out = [-1] * n
        #print("out is = ", out)
        s = deque()
     
        for i in reversed(range(2*n)):
        	#print("i = ", i)
          print("s[-1], inputs", len(s), i, n, i % n, input[i % n])
          while s:
              if s[-1] <= input[i % n]:
                  print("This is true s[-1] <= input[i % n]", s[-1] , input[i % n])
                  s.pop()
              else:
                  out[i % n] = s[-1]
                  print("s[-1] is = ", s[-1])
                  break

          s.append(input[i % n])
     
        return out
     
     
    if __name__ == '__main__':
     
        input = [3, 5, 2, 4]
        print(findNextGreater(input))
