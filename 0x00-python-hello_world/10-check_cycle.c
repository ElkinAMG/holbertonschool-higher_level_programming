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
	listint_t *tortoise = NULL;
	listint_t *bunny = NULL;
	int bool = 0;

	if (!list)
		return (bool);

	tortoise = list;
	bunny = list->next->next;

	while (bunny)
	{
		if (bunny == tortoise)
		{
			bool = 1;
			break;
		}

		bunny = bunny->next->next;
		tortoise = tortoise->next;
	}

	return (bool);
}
