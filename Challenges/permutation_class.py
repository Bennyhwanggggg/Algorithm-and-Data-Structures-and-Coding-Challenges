# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by Benny Hwang 14/09/2017


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
    def __init__(self, *args, length = None):
        self.length = length

        if args:
            seen = set()
            arg_length = set([i for i in range(1,len(args)+1)])
            
            self.args = args
            for i in self.args:
                if i == 0:
                    raise PermutationError('Cannot generate permutation from these arguments')
                if not isinstance(i,int):
                    raise PermutationError('Cannot generate permutation from these arguments')
                if i in seen or i not in arg_length:
                    raise PermutationError('Cannot generate permutation from these arguments')
                seen.add(i)
               
        else:
            args = tuple()
            self.args = args
            
        if length:            
            if len(args) == 0:
                self.args=tuple([i for i in range(1,length+1)])
            if len(self.args) != self.length:
                raise PermutationError('Cannot generate permutation from these arguments')
            else:
                for n in self.args:
                    if n==0:
                        raise PermutationError('Cannot generate permutation from these arguments')

        
        
        L = self.args   
        self.nb_of_cycles = len(Permutation.find_cycles(L))
        
    def __len__(self):
        return len(self.args)

    def __repr__(self):
         
        return str('Permutation'+str(self.args))
        
    def __str__(self):
        if self.args:
            cycles = Permutation.find_cycles(self.args)
            self.cycles = Permutation.cycles_print(cycles)
        else:
            self.cycles = self.args
        
        return '{self.cycles}'.format(self=self)

    def __mul__(self, permutation):
        p1 = list(self.args)
        p2 = list(permutation.args)
        if len(p1) != len(p2):
            raise PermutationError('Cannot compose permutations of different lengths')

        inds = [i for i in range(1,len(p1)+1)]
        result = []
        for i in inds:
            temp = p1[i-1]
            result.append(p2[temp-1])

        result = tuple(result)
        return Permutation(*result)
        
    def __imul__(self, permutation):
        p1 = list(self.args)
        p2 = list(permutation.args)
        if len(p1) != len(p2):
            raise PermutationError('Cannot compose permutations of different lengths')

        inds = [i for i in range(1,len(p1)+1)]
        result = []
        for i in inds:
            temp = p1[i-1]
            result.append(p2[temp-1])

        p1 = tuple(result)
        return Permutation(*p1)

    def inverse(self):
        L = list(self.args)
        inds = [i for i in range(1,len(L)+1)]
        inverse_L = []
        for n in inds:
            inverse_L.append(L.index(n)+1)

        result = tuple(inverse_L)
        return Permutation(*result)
        
    def isInt(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False
        
    def rotate(L, n):
        return L[n:] + L[:n]

    def find_cycles(L):
        remain_index = set(L)
        result = []
        while len(remain_index) > 0:
            ind = remain_index.pop()
            cycle = [ind]
            while True:
                ind = L[ind-1]

                if ind not in remain_index:
                    break
            
                remain_index.remove(ind)
                cycle.append(ind)
                
            result.append(cycle)
        return result
            
    def cycles_print(result):
        result2 = []
        for i in result:
            if len(i) > 0:
                start = i.index(max(i))
                result2.append(tuple(Permutation.rotate(i,start)))
                    
        arranged = str(sorted(result2))
        ar = list(arranged)
        s = ""
        for i in ar:
                
            if i=='(' or i==')' or Permutation.isInt(i):
                s+=str(i)
            if i ==',' and prev != ')':
                s+=str(' ')
            prev = i

        k = ""
        prev2 = 0
        ss = list(s)
        for pos, n in enumerate(ss):
            if n != ss[-1]:
                if n == ' ' and Permutation.isInt(ss[pos-1])==True and ss[pos+1]==')':
                    continue
                k+=str(n)
                    
            else:
                k+=str(n)
        return k


        



                
        

