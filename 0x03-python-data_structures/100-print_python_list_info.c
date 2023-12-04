#include <Python.h>

/**
 * print_python_list_info - print pytho
 * @p: list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int s, aoc, i;
	PyObject *o;

	s = Py_SIZE(p);
	aoc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", aoc);

	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);

		o = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
