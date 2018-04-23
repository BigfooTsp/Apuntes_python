http://pybonacci.org/2012/06/11/como-crear-matrices-en-python-con-numpy/
http://pybonacci.org/2012/08/17/como-leer-y-escribir-datos-en-archivos-con-numpy/
https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html

Ones and zeros
empty(shape[, dtype, order])	Return a new array of given shape and type, without initializing entries.
empty_like(a[, dtype, order, subok])	Return a new array with the same shape and type as a given array.
eye(N[, M, k, dtype])	Return a 2-D array with ones on the diagonal and zeros elsewhere.
identity(n[, dtype])	Return the identity array.
ones(shape[, dtype, order])	Return a new array of given shape and type, filled with ones.
ones_like(a[, dtype, order, subok])	Return an array of ones with the same shape and type as a given array.
zeros(shape[, dtype, order])	Return a new array of given shape and type, filled with zeros.
zeros_like(a[, dtype, order, subok])	Return an array of zeros with the same shape and type as a given array.
full(shape, fill_value[, dtype, order])	Return a new array of given shape and type, filled with fill_value.
full_like(a, fill_value[, dtype, order, subok])	Return a full array with the same shape and type as a given array.
From existing data
array(object[, dtype, copy, order, subok, ndmin])	Create an array.
asarray(a[, dtype, order])	Convert the input to an array.
asanyarray(a[, dtype, order])	Convert the input to an ndarray, but pass ndarray subclasses through.
ascontiguousarray(a[, dtype])	Return a contiguous array in memory (C order).
asmatrix(data[, dtype])	Interpret the input as a matrix.
copy(a[, order])	Return an array copy of the given object.
frombuffer(buffer[, dtype, count, offset])	Interpret a buffer as a 1-dimensional array.
fromfile(file[, dtype, count, sep])	Construct an array from data in a text or binary file.
fromfunction(function, shape, **kwargs)	Construct an array by executing a function over each coordinate.
fromiter(iterable, dtype[, count])	Create a new 1-dimensional array from an iterable object.
fromstring(string[, dtype, count, sep])	A new 1-D array initialized from raw binary or text data in a string.
loadtxt(fname[, dtype, comments, delimiter, ...])	Load data from a text file.
Creating record arrays (numpy.rec)
Note
numpy.rec is the preferred alias for numpy.core.records.

core.records.array(obj[, dtype, shape, ...])	Construct a record array from a wide-variety of objects.
core.records.fromarrays(arrayList[, dtype, ...])	create a record array from a (flat) list of arrays
core.records.fromrecords(recList[, dtype, ...])	create a recarray from a list of records in text form
core.records.fromstring(datastring[, dtype, ...])	create a (read-only) record array from binary data contained in
core.records.fromfile(fd[, dtype, shape, ...])	Create an array from binary file data
Creating character arrays (numpy.char)
Note
numpy.char is the preferred alias for numpy.core.defchararray.

core.defchararray.array(obj[, itemsize, ...])	Create a chararray.
core.defchararray.asarray(obj[, itemsize, ...])	Convert the input to a chararray, copying the data only if necessary.
Numerical ranges
arange([start,] stop[, step,][, dtype])	Return evenly spaced values within a given interval.
linspace(start, stop[, num, endpoint, ...])	Return evenly spaced numbers over a specified interval.
logspace(start, stop[, num, endpoint, base, ...])	Return numbers spaced evenly on a log scale.
geomspace(start, stop[, num, endpoint, dtype])	Return numbers spaced evenly on a log scale (a geometric progression).
meshgrid(*xi, **kwargs)	Return coordinate matrices from coordinate vectors.
mgrid	nd_grid instance which returns a dense multi-dimensional “meshgrid”.
ogrid	nd_grid instance which returns an open multi-dimensional “meshgrid”.
Building matrices
diag(v[, k])	Extract a diagonal or construct a diagonal array.
diagflat(v[, k])	Create a two-dimensional array with the flattened input as a diagonal.
tri(N[, M, k, dtype])	An array with ones at and below the given diagonal and zeros elsewhere.
tril(m[, k])	Lower triangle of an array.
triu(m[, k])	Upper triangle of an array.
vander(x[, N, increasing])	Generate a Vandermonde matrix.
The Matrix class¶
mat(data[, dtype])	Interpret the input as a matrix.
bmat(obj[, ldict, gdict])	Build a matrix object from a string, nested sequence, or array.








# CREACIÓN BÁSICA DE MATRICES.
np.empty((2, 3))  # (filas, columnas) Matriz vacía, con valores residuales de la memoria
np.zeros((3, 1))  # Matriz de ceros
np.ones((3, 2))  # Matriz de unos

In [5]: a = np.zeros((3, 2))
In [6]: np.ones_like(a)  # Matriz de unos con la forma de a
Out[6]:
array([[ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.]])

n [9]: np.identity(3)  # Matriz identidad de tamaño 3
Out[9]:
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

In [12]: np.eye(4, 3, k=-1)  # Con el parámetro k podemos controlar qué diagonal está llena de unos
Out[12]:
array([[ 0.,  0.,  0.],
       [ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

In [4]: np.array([[1, -1], [2, 0]]) # Lista de listas
Out[4]:
array([[ 1, -1],
       [ 2,  0]])

n [8]: np.array(range(5))
Out[8]: array([0, 1, 2, 3, 4])

In [15]: np.arange(2, 10, 3)
Out[15]: array([2, 5, 8])

In [16]: np.linspace(0, 1, 11)  # 11 puntos equiespaciados entre 0 y 1
Out[16]: array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ])
In [22]: np.logspace(2, 5, 4, base=10)  # 4 puntos equiespaciados según una escala logarítmica entre 10^2 y 10^5
Out[22]: array([    100.,    1000.,   10000.,  100000.])
