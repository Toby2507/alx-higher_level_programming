#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int i, size = PyList_Size(p);
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
