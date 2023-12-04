#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print pytho
 * @p: list
 * Return: void                                  */
void print_python_list_info(PyObject *p)
{
	long int s = PyList_Size(p);
	int i;
	PyListObject *ob;
	(PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", ob->allocated);
	for (i = 0; i < s; i++)
		print("Element %i: %s\n", i, Py_TYPE(ob->ob_item[i])->tp_name);
}
