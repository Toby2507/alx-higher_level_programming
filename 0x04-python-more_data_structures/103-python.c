#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_bytes - prints python bytes objests
 * @p: byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size = PyBytes_Size(p), maxBytes = (size < 10) ? size : 10;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Python bytes object.\n");
		return;
	}
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %ld bytes: ", maxBytes);
	for (i = 0; i < maxBytes; i++)
		printf(" %02x", (unsigned char)PyBytes_AsString(p)[i]);
	printf("\n");
}

/**
 * print_python_list - prints pythons lists
 * @p: list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size = PyList_Size(p);

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Python list object.\n");
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the list = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);
		const char *itemType = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, itemType);
		if (strcmp(itemType, "bytes") == 0)
			print_python_bytes(item);
	}
}
