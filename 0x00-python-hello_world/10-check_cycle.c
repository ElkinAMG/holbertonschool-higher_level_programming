#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks whether a linked list have a cycle or not.
 * @list: Given linked list to check.
 *
 * Return: It returns 0 if there is no cycle, otherwise 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *bunny;

	bunny = tortoise = list;

	while (bunny)
	{
		bunny = bunny->next->next;
		tortoise = tortoise->next;

		if (bunny == tortoise)
			return (1);
	}

	return (0);
}
