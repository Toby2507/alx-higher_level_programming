#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int i, size = Py_SIZE(p);
	PyListObject *list = p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(list, i))->tp_name);
}
