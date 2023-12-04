#include <Python.h>

/**
 * print_python_list_info - print list
 * @p: pointer
 */
void print_python_list_info(PyObject *p)
{
	int i, s, alloc;
	PyObjectt *object;

	s = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);

		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
