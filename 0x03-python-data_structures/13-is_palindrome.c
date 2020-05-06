#include "lists.h"

int n_nodes(listint_t *head);
int traverse_list(listint_t *head, int index);

/**
 * is_palindrome - Checks whether a list is palindrome or not.
 * @head: Head's linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	int is_pal = 1, tripper, mirror_1, mirror_2;
	int c_right, c_left, i;
	listint_t *right, *left;

	if (head && *head)
	{
		right = left = *head;
		tripper = n_nodes(*head);
		c_right = (tripper / 2);
		c_left = (tripper - 1);

		mirror_1 = traverse_list(right, 0);
		mirror_2 = traverse_list(left, c_left);

		for (i = 1; i <= c_right; i++)
		{
			if (mirror_1 != mirror_2)
			{
				is_pal = 0;
				break;
			}
			mirror_1 = traverse_list(right, i);
			mirror_2 = traverse_list(left, c_left - i);
		}
	}

	return (is_pal);
}

/**
 * traverse_list - It traverse the linked list until at given index.
 * @head: Head's linked list.
 * @index: Index for traverse.
 *
 * Return: The value in respective node.
 */

int traverse_list(listint_t *head, int index)
{
	for (; index > 0; index--)
		head = head->next;

	return (head->n);
}

/**
 * n_nodes - It counts the number of nodes in linked list.
 * @head: Head's linked list.
 *
 * Return: The number of nodes in linked list.
 */

int n_nodes(listint_t *head)
{
	int nodes;

	for (nodes = 0; head; head = head->next, nodes++)
		;

	return (nodes);
}
