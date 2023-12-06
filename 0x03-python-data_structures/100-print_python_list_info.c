#include <Python.h>
#include <stdio.h>

/**
 * print_item_info - Display the information of items of a python list
 * @prmItem: item of a python object
 * @prmItemIndex: item index
 */
void print_info(PyObject *Item, int idx)
{
	char *name;

	name = (char *)Py_TYPE(Item)->tp_name;

	printf("Element %d: %s\n", idx, name);
}	

/**
 * print_python_list_info - display all item informations from one python object
 * @p: Python object
 */
void print_python_list_info(PyObject *obj)
{
	int idx, nb = 0;
	PyObject *item;
	Py_ssize_t size = 0;

	if (PyList_Check(obj))
	{
		size = PyList_Size(obj);
		nb = ((PyListObject *)obj)->allocated;
		printf("[*] Size of the Python List = %d\n", (int) size);
		printf("[*] Allocated = %d\n", nb);
		for (idx = 0; idx < size; idx++)
		{
			item = PyList_GetItem(obj, idx);
			print_item_info(item, idx);
		}
	}
}
