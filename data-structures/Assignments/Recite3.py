# Imagiinary numbers class
class Complex():
    def __init__(self, r, i):
        self._real = r
        self._imag = i

    def __str__(self):
        # To display complex number in string represemtation
        if self._imag >= 0:
            return f"{self._real} + {self._imag}i"
        else:
            return f"{self._real} - {abs(self._imag)}i"
        
    __repr__ = __str__ # to also affect return values

    def conjugate(self):
        conj = Complex(self._real, -self._imag)
        return conj
    
# x = Complex(5,-6)
# print(x)
# y = x.conjugate()
# print(y)
# print(isinstance(y, Complex))

    def __mul__(self, other):
        #multiplication between two complex numbers
        if isinstance(other, Complex):
            real_part = (self._real*other._real) - (self._imag*other._imag)
            # print(real_part)
            imag_part = (self._real*other._imag) + (self._imag*other._real)
            # print(imag_part)
            ans = Complex(real_part, imag_part)
            return ans
        else:
            real_part = self._real*other
            imag_part = self._imag*other
            ans = Complex(real_part, imag_part)
            return ans
    def __rmul__(self, other):
        return self*other
    
    
# x = Complex(5,-6)
# y = Complex(1,2)
# result = x*y
# print(result)
# z = Complex(3,1)
# result = z*2
# print(result)
# x = Complex(3,1)
# result = 2 * x
# print(result)
class Real(Complex):

    def __init__(self, value):
        super().__init__(value, 0)

    def __mul__(self, other):
        if isinstance(other, Real):
            return Real(self._real * other._real)
        elif isinstance(other, (int, float)):
            return Real(self._real * other)
        elif isinstance(other, Complex):
            return other * self # should return a complex, MAKE SURE COMPLEX IS ON LEFT SIDE, THIS WILL ENSURE THAT THE COMPLEX MULTIPLICATION IS BEING CALLED.

    def __eq__(self, other):

        ''' Returns True if other is a Real object that has the same value or if other is
            a Complex object with _imag=0 and same value for _real, False otherwise

            >>> Real(4) == Real(4)
            True
            >>> Real(4) == Real(4.0)
            True
            >>> Real(5) == Complex(5, 0)
            True
            >>> Real(5) == Complex(5, 12)
            False
            >>> Real(5) == 5.5
            False
        '''
        # YOUR CODE STARTS HERE
        if isinstance(other, (int, float)):
            return self._real == other
        elif isinstance(other, Real):
            return self._real == other._real
        elif isinstance(other, Complex):
            if other._imag == 0 or other._imag == 0.0:
                return self._real == other._real
            else:
                return False
            
    def __int__(self):
        return int(self._real)
    def __float__(self):
        return float(self._real)
    


# x = Real(3)
# y = Real(8) 
# z = Complex(2, 5) 
# op1 = x * y  
# print(op1) 
    
# print(type(op1))

# op2 = x * 2 
# print(op2) 
# print(type(op2))  
# op3 = 2 * y 
# print(op3) 

# print(type(op3))  
# op4 = x * z 
# print(op4) 

# print(type(op4))
# print(Real(4) == Real(4))
# print(Real(4) == Real(4.0))
# print(Real(5) == Complex(5, 0))
# print(Real(5) == Complex(5, 12))
# print(Real(5) == 5.5)
# print(Real(5) == 5.0)

# print(int(x) * [1,2,3])
# print(isinstance(float(x),float))
