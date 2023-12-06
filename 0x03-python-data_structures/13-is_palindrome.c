#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: first node
 * Return: 1 if success, 0 in case it failed
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int content[2048];
	int i = 0;
	int idx, m;

	if (!head || !(*head))
		return (1);
	while (tmp)
	{
		content[i++] = tmp->n;
		tmp = tmp->next;
	}
	if (i % 2 == 0)
		m = i / 2;
	else
		m = (i + 1) / 2;
	for (idx = 0; idx < m; idx++)
	{
		if (content[idx] != content[i - 1 - idx])
			return (0);
	}
	return (1);
}