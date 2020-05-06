#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc, tripper;

	size = Py_SIZE(p);
	alloc = ((PyListObject *) p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (tripper = 0; tripper < size; tripper++)
		printf("Element %d: %s\n", tripper,
		       Py_TYPE(PyList_GetItem(p, tripper))->tp_name);
}
