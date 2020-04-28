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
	listint_t *tortoise, *rabbit;

	rabbit = tortoise = list;

	while (rabbit)
	{
		rabbit = rabbit->next->next;
		tortoise = tortoise->next;

		if (tortoise == rabbit)
			return (1);
	}

	return (0);
}
